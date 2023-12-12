from fastapi import FastAPI
import uvicorn
from core.database import manga_collection
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI(
    docs_URL = '/docs'
)

@app.get('/')
async def get():
    data = list(manga_collection.find())
    for item in data:
        if isinstance(item.get('_id'), ObjectId):
            item['id'] = str(item.pop('_id'))
    return {'data': data}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
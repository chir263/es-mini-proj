from fastapi import APIRouter, Depends
from models.add import AddMessageRequest
from elasticsearch import Elasticsearch, NotFoundError
from fastapi.responses import JSONResponse
from helpers.es_client import get_es_client

add_router = APIRouter()


@add_router.post("/")
def add_data(request: AddMessageRequest, es_client: Elasticsearch = Depends(get_es_client)):
    res = es_client.index(index="messages", body={"message": request.message})
    return {"message": "Message added successfully", "id": res['_id']}


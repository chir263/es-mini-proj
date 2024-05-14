from fastapi import APIRouter, Depends
from elasticsearch import NotFoundError, Elasticsearch
from helpers.es_client import get_es_client

search_router = APIRouter()

@search_router.get("/{query}")
def search_data(query: str, es_client: Elasticsearch = Depends(get_es_client)):
    try:
        res = es_client.search(index="messages", body={"query": {"match": {"message": query}}})
        hits = res['hits']['hits']

        if not hits:
            return {"message": f"No messages found with keyword: {query}", "hits": []}

        messages = [{"id": hit['_id'], "message": hit['_source']['message']} for hit in hits]
        return {"message": f"Messages found with keyword: {query}", "hits": messages}
    except NotFoundError:
        return {"message": "Index 'messages' not found. No messages indexed yet.", "hits": []}


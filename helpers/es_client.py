from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os
import json

load_dotenv()


def create_index_if_not_exist(es_client: Elasticsearch):
    index_name = "messages"
    if not es_client.indices.exists(index=index_name):
        es_client.indices.create(index=index_name)
    return es_client


def get_es_client():
    client = Elasticsearch(
        os.getenv("ES_URL"),
        api_key=os.getenv("ES_API_KEY")
    )
    return create_index_if_not_exist(client)

from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Elasticsearch(
  os.getenv("ES_URL"),
  api_key=os.getenv("ES_API_KEY")
)
resp = client.info()
print(resp)
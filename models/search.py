from pydantic import BaseModel

class SearchMessageRequest(BaseModel):
    query: str
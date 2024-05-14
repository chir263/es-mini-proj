from pydantic import BaseModel

class AddMessageRequest(BaseModel):
    message: str

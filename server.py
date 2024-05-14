from fastapi import FastAPI
from fastapi import APIRouter
from routers.add import add_router
from routers.search import search_router

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}

app.include_router(add_router, prefix="/add", tags=["add"])
app.include_router(search_router, prefix="/search", tags=["search"])

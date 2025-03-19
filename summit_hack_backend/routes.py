# app/routes.py
from fastapi import APIRouter
from service import get_response

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@router.get("/fetch-data")
async def get_data():
    """Fetches data from an external API and returns it."""
    data = await get_response("query")
    return {"message": "Data retrieved successfully", "data": data}

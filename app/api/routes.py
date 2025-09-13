from fastapi import APIRouter
from app.models.schemas import Item

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/items", response_model=Item)
def create_item(item: Item):
    return item

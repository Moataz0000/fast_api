from fastapi import APIRouter
from app.schemas import Item



router = APIRouter()


@router.post('/items/')
async def create_item(item: Item):
    return {"message": "Item created successfully!", 'Item': item}
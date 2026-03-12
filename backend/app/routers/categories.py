from fastapi import HTTPException,status,Query,APIRouter
from app.schemas.categories import CategoryCreate

from typing import Annotated
from pydantic import BaseModel
from datetime import date
from enum import Enum

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/categories",status_code=status.HTTP_200_OK,response_model=list[str])
async def getCategories():
    for expense in expenses:
        categories.add(expense.category)
    return categories
    

@router.post("/categories",status_code=status.HTTP_201_CREATED)
async def update_categories(newCategory: CategoryCreate):
    categories.add(newCategory.name)
    return categories
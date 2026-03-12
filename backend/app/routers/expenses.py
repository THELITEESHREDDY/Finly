from fastapi import HTTPException,status,Query,APIRouter
from app.schemas.expenses import ExpenseResponse, ExpenseUpdate, ExpenseCreate
from app.schemas.categories import 

from fastapi.responses import RedirectResponse
from dateutil.relativedelta import relativedelta
from collections import defaultdict
from typing import Annotated
from pydantic import BaseModel
from datetime import date
from enum import Enum

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.get("/expenses", status_code=status.HTTP_200_OK,response_model=list[ExpenseResponse])


@router.post("/expenses",status_code=status.HTTP_201_CREATED)



@router.get("/expenses/{id}",status_code=status.HTTP_200_OK,response_model=ExpenseResponse)



@router.put("/expenses/{id}",status_code=status.HTTP_202_ACCEPTED,response_model=ExpenseResponse)




@router.delete("/expenses/{id}")



    
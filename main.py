from fastapi import FastAPI,HTTPException,status,Query
from fastapi.responses import RedirectResponse
from dateutil.relativedelta import relativedelta
from collections import defaultdict
from typing import Annotated
from pydantic import BaseModel
from datetime import date
from enum import Enum

class ExpenseCreate(BaseModel):
    name: str
    category: str
    amount: float
    date: date

class ExpenseUpdate(BaseModel):
    id: int
    name:str
    category:str
    amount: float
    date: date

class ExpenseResponse(BaseModel):
    id:int
    name: str
    category: str
    amount: float
    date:date

class CategoryCreate(BaseModel):
    name: str


expenses=[]
categories={}

app= FastAPI()

@app.get("/")
async def getHome():
    return {"message":"Welcome to Finance Manager"}

@app.get("/expenses", status_code=status.HTTP_200_OK,response_model=list[ExpenseResponse])
async def getAllExpenses():
    return expenses


@app.post("/expenses",status_code=status.HTTP_201_CREATED)
async def addExpense(expense: ExpenseCreate):
    try:
        new_expense= ExpenseResponse(
            id=len(expenses)+1,
            **expense.model_dump()
        )
        expenses.append(new_expense)
        return new_expense
    except:
        raise HTTPException(status_code=500,detail="failed to create")



@app.get("/expenses/{id}",status_code=status.HTTP_200_OK,response_model=ExpenseResponse)
async def getExpense(id: int):
    
    for expense in expenses:
        if expense.id==id:
            return expense
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="can't find the expense")

@app.put("/expenses/{id}",status_code=status.HTTP_202_ACCEPTED,response_model=ExpenseResponse)
async def getExpense(id: int, updated_expense: ExpenseUpdate):
    try:
        for i,expense in enumerate(expenses):
            if expense.id == id:
                expenses[i]=ExpenseResponse(**updated_expense.model_dump())
        return updated_expense
    except:
        raise HTTPException(status_code=404, detail="Expense not Found")


@app.delete("/expenses/{id}")
async def delete_expense(id: int):
    try:
        expense_to_remove=next((index for index,expense in enumerate(expenses) if expense.id==id),-1)
        if expense_to_remove!=-1:
            removed_expense=expenses.pop(expense_to_remove)
            return removed_expense
    except:
        raise HTTPException(status_code=404, detail="Expense not Found")
    
categories=set()
category_wise_cal={}
class SummaryType(str, Enum):
    summary_type: int

class SummaryTrend(BaseModel):
    trend:int

@app.get("/categories",status_code=status.HTTP_200_OK,response_model=list[str])
async def getCategories():
    categories={expense.category for expense in expenses}
    return categories
    

@app.post("/categories",status_code=status.HTTP_201_CREATED)
async def update_categories(newCategory: CategoryCreate):
    categories.add(newCategory.name)
    return RedirectResponse("/categories")


@app.get("/summary/",status_code=status.HTTP_200_OK)
async def get_summary(wanted_months: Annotated[int|None, Query(ge=1 , le=12)]=1):
   
    start_date= date.today()-relativedelta(months=wanted_months)

    for category in categories:
        category_wise_cal[category]=0

    for expense in expenses: 
            if expense.date >= start_date:
                category_wise_cal[expense.category]+= expense.amount

    return category_wise_cal
    

@app.get("/summary/trend/",status_code=status.HTTP_200_OK)
async def get_summary_trend(months: Annotated[int | None, Query(ge=1 , le=12)]=6):

    category_wise_trend={category: [] for category in categories}
    today= date.today()

    for i in range(months):
        start_month=today-relativedelta(months=i+1)
        end_month=today-relativedelta(months=i)

        monthly_sum=defaultdict(float)

        for expense in expenses:
            if start_month <=expense.date < end_month:
                monthly_sum[expense.category]+=expense.amount   

        for category in categories:
            category_wise_trend[category].append(monthly_sum.get(category,0)) 
    
    for category in category_wise_trend:
        category_wise_trend[category].reverse()
    
    return dict(category_wise_trend)
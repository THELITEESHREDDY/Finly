from fastapi import FastAPI
from app.routers import expenses
from app.routers import categories
from app.routers import summary

app= FastAPI(title="Finly")

@app.get("/")
async def getHome():
    return {"message":"Welcome to Finance Manager"}


app.include_router(expenses.router)
app.include_router(categories.router)
app.include_router(summary.router)
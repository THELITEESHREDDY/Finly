
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

# get all expense
async def getAllExpenses():
    return expenses

# recieves a expense 
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
    


# send some expense with id
async def getExpense(id: int):
    
    for expense in expenses:
        if expense.id==id:
            return expense
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="can't find the expense")


# edit some expense with that paticular id
async def getExpense(id: int, updated_expense: ExpenseUpdate):
    try:
        for i,expense in enumerate(expenses):
            if expense.id == id:
                expenses[i]=ExpenseResponse(**updated_expense.model_dump())
        return updated_expense
    except:
        raise HTTPException(status_code=404, detail="Expense not Found")


# delete some expense with some id
async def delete_expense(id: int):
    try:
        expense_to_remove=next((index for index,expense in enumerate(expenses) if expense.id==id),-1)
        if expense_to_remove!=-1:
            removed_expense=expenses.pop(expense_to_remove)
            return removed_expense
    except:
        raise HTTPException(status_code=404, detail="Expense not Found")
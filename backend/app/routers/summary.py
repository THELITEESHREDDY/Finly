from fastapi import HTTPException,status,Query,APIRouter


router = APIRouter(prefix='/summary', tags=["summary"])
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
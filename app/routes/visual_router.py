from fastapi import APIRouter
import matplotlib.pyplot as plt
from app.routes import user_action_router
visual_router=APIRouter()
@visual_router.get('/get/{user_id}/{year}')
async def get_user_graf(user_id:int,year:int):
    month = [1,2,3,4,5,6,7,8,9,10,11,12]
    sum = []
    for m in month:
        u_a_m=await user_action_router.get_user_actions_by_month(user_id,year,m)
        s = 0
        for u in u_a_m:
            if(u.type=='revenue'):
                s-=u.amount
            else:
                s+=u.amount
        sum.append(s)
    print(month)
    print(sum)
    plt.plot(month,sum)
    return plt.show()


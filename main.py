import uvicorn as uvicorn
from fastapi import FastAPI
from app.routes.user_router import user_router
from app.routes.user_action_router import user_action_router
app = FastAPI()
app.include_router(user_router, prefix='/users')
app.include_router(user_action_router, prefix='/users_action')
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1")
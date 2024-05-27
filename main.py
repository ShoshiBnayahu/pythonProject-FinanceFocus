import uvicorn as uvicorn
from fastapi import FastAPI


"""
This script creates a FastAPI application and runs it using Uvicorn.

- `app`: The FastAPI application instance.
- `user_router`: Router for user-related endpoints.
- `user_action_router`: Router for user action-related endpoints.
- `visual_router`: Router for visualization-related endpoints.

The application includes routers for different functionalities and is run using Uvicorn on localhost.
"""


from app.routes.user_action_router import user_action_router
from app.routes.user_router import user_router
from app.routes.visual_router import visual_router

app = FastAPI()
app.include_router(user_router, prefix='/user')
app.include_router(user_action_router, prefix='/user_action')
app.include_router(visual_router, prefix="/visual")

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
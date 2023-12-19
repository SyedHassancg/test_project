from fastapi import FastAPI

from routes.callback import callback_router

app = FastAPI()

app.include_router(callback_router, prefix="/upwork")

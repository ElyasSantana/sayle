from fastapi import FastAPI

from .routes import conversations


app = FastAPI()

app.include_router(conversations.router)

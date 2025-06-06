from fastapi import FastAPI
from .api import router as auth_router
from .config import settings

app = FastAPI(title="Authentication Service")

app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Authentication Service"}

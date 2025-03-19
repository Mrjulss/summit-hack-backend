# app/main.py
from fastapi import FastAPI
app = FastAPI(title="FastAPI External API Example")


# Include routes
@app.get("/")
async def root():
    return {"message": "Hello World"}

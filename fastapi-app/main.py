import os

from fastapi import FastAPI

app = FastAPI()

level = os.getenv("LEVEL", "NO LEVEL")

@app.get("/")
async def root():
    return {"message": f"{level}"}
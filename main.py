import random

from fastapi import FastAPI

app = FastAPI()

app.ticket = 0


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ticket")
async def root():
    random.sample(range(10, 30_000_000), 500_000).sort() # Make it more CPU bound
    app.ticket += 1
    return f"Your ticker number is: {app.ticket}"
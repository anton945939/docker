from fastapi import FastAPI

app = FastAPI()

app.ticket = 0


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ticket")
async def root():
    app.ticket += 1
    return f"Your ticker number is: {app.ticket}"
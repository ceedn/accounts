from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def read_root(request: Request):
    return {"message": "Hello World!!!!"}

@app.get("/measurements")
async def read_root(request: Request):
    return {"success": True}
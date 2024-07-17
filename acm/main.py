from fastapi import FastAPI, Request
import datetime

app = FastAPI()
start_time = datetime.datetime.now()

@app.get("/")
async def read_root(request: Request):
    return {"message": "Hello World!!!!"}

@app.get("/measurements")
async def read_uptime(request: Request):
    uptime = datetime.datetime.now() - start_time
    return {"uptime": uptime}
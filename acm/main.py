from fastapi import FastAPI, Request
import datetime
from utils import utils
from schemas import schemas
from models import models
from fastapi.responses import JSONResponse
import sys, os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import desc

app = FastAPI()
start_time = datetime.datetime.now()

@app.get("/",
         status_code=200,
         name="API - Root",
         description="Return an error message on the root of the API, since nothing should be performed here.",
         tags=["Information"],
         response_model=schemas.APIRootResponse,
         )
async def root():
    print("Root endpoint called.")
    return {
        "success": False,
        "detail": "This is the root of the API. Nothing should be performed here.",
    }


@app.get("/accounts/measurements")
async def read_uptime(request: Request):
    uptime = datetime.datetime.now() - start_time
    return {"uptime": uptime}
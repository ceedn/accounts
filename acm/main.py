from fastapi import FastAPI, Request
import datetime
from utils import utils
from schemas import schemas as schemas
from models import models as models
from fastapi.responses import JSONResponse
import sys, os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import desc
from uuid import uuid4

# Initialize the database engine
try:
    DatabaseURL = os.environ.get("DB_URL")
    engine = create_engine(DatabaseURL)
    database = Session(engine)
    databaseModel = models.metadata
    databaseModel.bind = engine
    print("Initilized database engine.")
except Exception as err:
    raise
    sys.exit(1)

# Generate tables in the database if they don't exist
if os.environ.get("DB_INIT") == "True":
    try:
        databaseModel.create_all(bind=engine)
    except Exception as err:
        raise
        sys.exit(1)

# Get root path of the API
rootPath = os.environ.get("API_ROOT_PATH")
if rootPath == None:
    rootPath = "/"

app = FastAPI()
start_time = datetime.datetime.now()
instanceID = str(uuid4())

@app.get(rootPath,
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


@app.get(rootPath + "measurements")
async def read_uptime(request: Request):
    return {f"{instanceID}"}
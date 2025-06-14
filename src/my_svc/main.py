import logging
import os

from fastapi import FastAPI

from my_svc.logging_utils import add_logging_middleware, setup_logging

setup_logging()

app = FastAPI()
add_logging_middleware(app)

logger = logging.getLogger(__name__)


@app.get("/")
async def root(name: str = "World"):
    logger.info(f"Received request with name: {name}")
    logger.debug(f"Debugging info for name: {name}")
    return {"message": f"Hello, {name}, from FastAPI!", "os": os.name}


@app.get("/error")
async def error():
    logger.error("This is a test error log")
    raise Exception("This is a test exception")


# UNCOMMENT THIS SECTION TO TEST ENVIRONMENT VARIABLES
@app.get("/settings")
async def settings():
    return {
        "API_KEY": os.environ.get("API_KEY", "NOT SET"),
        "DB_HOSTNAME": os.environ.get("DB_HOSTNAME", "NOT SET"),
        "DB_USERID": os.environ.get("DB_USERID", "NOT SET"),
        "DB_PASSWORD": os.environ.get("DB_PASSWORD", "NOT SET"),
    }

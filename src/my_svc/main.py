import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(name: str = "World"):
    return {"message": f"Hello, {name}"}


# UNCOMMENT THIS SECTION TO TEST ENVIRONMENT VARIABLES
# @app.get("/settings")
# async def settings():
#     return {
#         "API_KEY": os.environ.get("API_KEY", "NOT SET"),
#         "DB_HOSTNAME": os.environ.get("DB_HOSTNAME", "NOT SET"),
#         "DB_USERID": os.environ.get("DB_USERID", "NOT SET"),
#         "DB_PASSWORD": os.environ.get("DB_PASSWORD", "NOT SET"),

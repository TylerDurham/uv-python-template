from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(name: str = "World"):
    return {"message": f"Hello, {name}"}

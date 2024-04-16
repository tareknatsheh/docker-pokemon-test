from fastapi import FastAPI
from routes import api

app = FastAPI()

app.include_router(api.router, tags=["API endpoint"])

@app.get("/")
def home():
    """This is for sanity check. Just to make sure that the server is up and running
    """
    return "all is good"
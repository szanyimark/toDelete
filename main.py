from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

@app.get("/hello")
def read_root():
    return {"Hello": "World"}

@app.get("/hello2")
def read_root():
    return {"Hello": "World, again"}


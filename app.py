from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI on Azure!"}

@app.get("/ping")
def ping():
    return {"ping": "pong"}

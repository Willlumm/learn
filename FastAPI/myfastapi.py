from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/my-first-api")
def hello(name):
  return {f"Hello {name}!"} 

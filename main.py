from fastapi import FastAPI
from typing import Any

app = FastAPI(title="HBS")

@app.get('/')
def index():
    return "HBS School home function details"

@app.get('/student/{id}')
def student(id:int):
    data :dict[int,str] = {1:'Qasim',2:'Zia Khan'}
    found_data: dict[Any,Any] = {"id":id, "student":data[id]}
    return found_data
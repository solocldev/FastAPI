from typing import Union
from translate import *
from queryhandler import *
from pydantic import BaseModel
from transliterate import *
from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
queries=  []

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

class User_input(BaseModel):
    q: str
    source_language : str
    destination_language: str

@app.get("/query")
def read_item(input:User_input):
    result = preprocess_query(input.q,input.source_language,input.destination_language)
    print(result)
    return {"result":result}

"""
{"source": source, "input": input, "destination language": destn_language}
another api for voice input and interface
"""
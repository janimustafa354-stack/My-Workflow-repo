from fastapi import FastAPI,Header
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get('/')
def read_root():
    return {"message":"Mudassir"}

@app.get('/about')
def get_name():
    return("Mustafa")



@app.get('/greet')
def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
    return {"message": f"{name}", "age": age}

class BookCreateModel(BaseModel):
    title: str  
    author: str 

@app.post('/create_book',status_code=202)  
def create_book(book_data: BookCreateModel): 
    return {
        'title': book_data.title,
        'author': book_data.author
    }

@app.get('/get_headers')
def get_headres(
    accept: str = Header(None),
    content_type:str=Header(None),
    user_agent:str=Header(None),
    host:str=Header(None),
    postal_address:str=Header(None)
    ):
    request_header = {}

    request_header["Accept"] = accept
    request_header["Content_Type"] = content_type
    request_header["User_Agent"] = user_agent
    request_header["Host"] = host
    request_header["Postal_Address"]=postal_address
    return request_header

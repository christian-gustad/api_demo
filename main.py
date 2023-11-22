import fastapi
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, status, Header, Request
from queries import my_query

app = FastAPI()
load_dotenv()

@app.get("/")
async def test_connection(request: Request):
    return {"Connection": "Success"}


@app.get("/query/{parameter}")
async def query_with_paramter(parameter: str,
                              request: Request):
    return_value = my_query(parameter)
    return return_value

from dotenv import load_dotenv
from fastapi import FastAPI
from queries import my_query, my_query_with_body
from pydantic import BaseModel


class Item(BaseModel):
    string_parameter: str | None = None
    numeric_parameter: int | None = None


app = FastAPI()
load_dotenv()


@app.get("/")
async def test_connection():
    """
    This is a test if the connection works!
    """
    return {"Connection": "Success"}


@app.get("/query/{parameter}")
async def query_with_paramter(parameter: str):
    """
    This is a request against the endpoint, with a string parameter.
    Runs a query against the database
    """
    return_value = my_query(parameter)
    return return_value


@app.post("/querywithbody/")
async def query_with_body(items: Item):
    """
    This is a request against the endpoint where we refer to the supplied body/payload
    """
    return_value = my_query_with_body(items)
    return {"Returned" : return_value}

from fastapi import FastAPI
from pydantic import BaseModel
from calculator import calculate

class user_input(BaseModel):
    operation : str
    x : float
    y : float

app = FastAPI()

@app.post("/calculate")
def operate(input:user_input):
    result = calculate(input.operation, input.x, input.y)
    return result



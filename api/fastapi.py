from fastapi import FastAPI



# FastAPI instance
app = FastAPI()


# Root endpoint
@app.get("/")
def root():
    """Root endpoint returning a greeting."""
    return {"greeting": "hello"}


# Dummy endpoint
@app.get("/dummy")
def dummy(number: int):
    """Dummy endpoint that returns the square of the input number."""
    return {"result": number ** 2}


@app.get("/predict")
def predict_pinguins(number_a:float ,
            number_b:float ,
            value_n:int):
    #The function makes (a*b)^n
    number = (number_a * number_b)**value_n

    return {"(a*b)^n" : number}

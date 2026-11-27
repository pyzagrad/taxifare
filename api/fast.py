from fastapi import FastAPI

from taxifare.predict import load_model, predict

# FastAPI instance
app = FastAPI()

model = load_model("models/linreg_pipeline.joblib")

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
def predict_model(passenger_number:int):

    number = passenger_number * 2.5

    return {"number of passenger * 2.5" : number}

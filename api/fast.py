from fastapi import FastAPI
# import the load model and predict functions from predict.py file
from taxifare.predict import load_model, predict
import pandas as pd

# FastAPI instance
app = FastAPI()

#load the model (model imported using the notebook)
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
def predict_model(pickup_datetime:str ,
            pickup_longitude:float ,
            pickup_latitude:float ,
            dropoff_longitude:float,
            dropoff_latitude:float,
            passenger_count:int):

    X = pd.DataFrame([{
          'pickup_datetime': pickup_datetime,
          'pickup_longitude': pickup_longitude,
          'pickup_latitude': pickup_latitude,
          'dropoff_longitude': dropoff_longitude,
          'dropoff_latitude': dropoff_latitude,
          'passenger_count': passenger_count
    }])

    prediction = predict(model,X)

    return {"prediction" : prediction[0]}

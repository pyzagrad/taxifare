"""
This module loads a trained machine learning model and makes predictions on new data.
"""

# Import necessary libraries
import joblib
import pandas as pd
from sklearn import set_config

set_config(transform_output="pandas")

MODEL_PATH = "models/linereg_pipeline.joblib"


def load_model(model_path: str):
    """Load a trained model from the specified file path."""
    with open(model_path, "rb") as f:
        return joblib.load(f)


def predict(model, data):
    """Make predictions using the loaded model and input data."""
    return model.predict(data)

if __name__ == "__main__":
    X_dummy = pd.DataFrame([{
          'pickup_datetime': '2013-07-06 17:18:00 UTC',
          'pickup_longitude': -73.950655,
          'pickup_latitude': 40.783282,
          'dropoff_longitude': -73.984365,
          'dropoff_latitude': 40.769802,
          'passenger_count': 1
    }])

    model = load_model("models/linreg_pipeline.joblib")

    print(predict(model, X_dummy))

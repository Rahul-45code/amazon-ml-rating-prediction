from fastapi import FastAPI
import joblib
import numpy as np


app = FastAPI()

model = joblib.load("model/model.pkl")
features = joblib.load("model/features.pkl")


@app.get("/")
def home():
    return {"message": "Welcome to the Amazon Price Prediction API"}

@app.post("/predict")
def predict(input_data: dict):
    # Create zero array for all features
    data = np.zeros(len(features))

    # Fill values from user input
    for key, value in input_data.items():
        if key in features:
            index = features.index(key)
            data[index] = value

    prediction = model.predict([data])

    return {
        "predicted_rating": float(prediction[0])
    }
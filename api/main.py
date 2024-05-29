import numpy as np
import pandas as pd
from fastapi import FastAPI
import joblib
import os
import uvicorn

from utils.custom_transformer import AgeGroupTransformer, BMICalculator, BMICategoryTransformer, HeightToWeightRatio
from utils.size_recommender import size_recommender

app = FastAPI()

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(ROOT_PATH, 'api', 'models', 'model.pkl')

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'ok': 'Hello '}

# @app.get('/predict')
@app.get("/predict")
def predict(gender, age, height, weight):
    model = joblib.load(MODEL_PATH)
    
    height = float(height)
    df = pd.DataFrame({
        "gender": gender,
        "age": float(age),
        "height": height,
        "weight": float(weight)
    }, index=[0])
    
    # bust_circumference 	waist_circumference 	hip_circumference
    pred = model.predict(df)

    # Convert from mm to cm
    bust_size = round(pred[0][0] / 10, 2)
    waist_size = round(pred[0][1] / 10, 2)
    hip_size = round(pred[0][2] / 10, 2)
    height = round(height / 10, 2)
    
    # Size recommendation logic
    rec_size = size_recommender(bust_size, waist_size, hip_size, height, gender)
    
    return {'rec_size': rec_size}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)

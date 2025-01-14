from fastapi import FastAPI
from pydantic import BaseModel
from .model1 import predict_genre
from .model2 import predict_emotion

# FastAPI app instance
app = FastAPI()

# Input model for validation
class PredictionInput(BaseModel):
    text: str


# Prediction endpoint (model 2)
@app.post("/predict_emotion_endpoint")
def predict_emotion_endpoint(first_chunks: PredictionInput):
    prediction = predict_emotion(first_chunks.text)
    return {"input": first_chunks.text, "prediction": prediction}


# Prediction endpoint (model 1)
@app.post("/predict_genre_endpoint")
def predict_genre_endpoint(first_chunks: PredictionInput):
    prediction = predict_genre(first_chunks.text)
    return {"input": first_chunks.text, "prediction": prediction}


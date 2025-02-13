from fastapi import FastAPI
from pydantic import BaseModel
from .emotion_predictor import predict_emotion
import pickle

# FastAPI app instance
app = FastAPI()

# Input model for validation
class PredictionInput(BaseModel):
    text: str

# Model initialization
with open('artifacts/emotion/model_emotion.pkl', 'rb') as file:
    model_emotion = pickle.load(file)

# Prediction endpoint
@app.post("/predict_emotion_endpoint")
def predict_emotion_endpoint(first_chunks: PredictionInput):
    prediction = predict_emotion(first_chunks.text, model_emotion)
    return {"input": first_chunks.text, "prediction": prediction}

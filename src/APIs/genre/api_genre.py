from fastapi import FastAPI
from pydantic import BaseModel
from .genre_predictor import predict_genre
import pickle

# FastAPI app instance
app = FastAPI()

# Input model for validation
class PredictionInput(BaseModel):
    text: str

# Model initialization
with open('artifacts/genre/pipeline_logistic_genre.pkl', 'rb') as file:
    model_genre = pickle.load(file)

# Prediction endpoint
@app.post("/predict_genre_endpoint")
def predict_genre_endpoint(first_chunks: PredictionInput):
    prediction = predict_genre(first_chunks.text, model_genre)
    return {"input": first_chunks.text, "prediction": prediction}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

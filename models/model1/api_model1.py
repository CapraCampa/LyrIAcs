from fastapi import FastAPI
from pydantic import BaseModel
from .model1 import predict_genre

# FastAPI app instance
app = FastAPI()

# Input model for validation
class PredictionInput(BaseModel):
    text: str


# Prediction endpoint
@app.post("/predict_genre_endpoint")
def predict_genre_endpoint(first_chunks: PredictionInput):
    prediction = predict_genre(first_chunks.text)
    return {"input": first_chunks.text, "prediction": prediction}

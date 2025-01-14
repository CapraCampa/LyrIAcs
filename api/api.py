from fastapi import FastAPI
from pydantic import BaseModel
from .model1 import predict_genre
from .model2 import predict_emotion

# FastAPI app instance
app = FastAPI()

# Input model for validation
class PredictionInput(BaseModel):
    text: str



# Prediction endpoint (model 1)
@app.post("/predict_genre")
def predict_emotion(data: PredictionInput):
    prediction = predict_genre(data.text)
    return {"input": data.text, "prediction": prediction}


# Prediction endpoint (model 2)
@app.post("/predict_emotion")
def predict_emotion(data: PredictionInput):
    prediction = predict_emotion(data.text)
    return {"input": data.text, "prediction": prediction}

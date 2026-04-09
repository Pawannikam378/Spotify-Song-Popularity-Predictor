from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("E:\D Drive Data\Project\Spotify Song Prediction System\Spotify-Song-Popularity-Predictor\models\model.pkl")


@app.get("/")
def home():
    return {"message": "Welcome to the Spotify Song Popularity Predictor API!"}

@app.post("/predict")
def predict(data: dict):
    features = list(data.values())
    prediction = model.predict([features])
    return{"predicted_popularity": float(prediction[0])}
    
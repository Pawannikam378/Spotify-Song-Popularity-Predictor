# 🎵 Spotify Song Popularity Predictor

## 🚀 Overview
This project predicts the popularity of songs using Spotify API data and machine learning.

## 🔥 Features
- Spotify API data collection
- XGBoost ML model
- SHAP explainability
- FastAPI deployment

## 🧠 AI Enhancement
Uses advanced ensemble learning (XGBoost) for better prediction accuracy.

## 📊 Model Performance
- MAE: ~10-15
- R2 Score: ~0.6+

## ⚙️ Setup
```bash
pip install -r requirements.txt
```

## ▶️ Run Project
```bash
python src/fetch_data.py
python src/train.py
uvicorn app.main:app --reload
```

## 📡 API Usage
POST /predict

Example JSON:
```
{
  "danceability": 0.8,
  "energy": 0.7,
  "tempo": 120
}
```

## 📌 Tech Stack
- Python
- Scikit-learn
- XGBoost
- SHAP
- FastAPI

## 💡 Future Improvements
- Real-time Spotify search
- Web dashboard
- Deep learning model

## 👨‍💻 Author
Pawan Nikam

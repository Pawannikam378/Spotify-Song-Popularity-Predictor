import shap
import joblib
import pandas as pd

model  = joblib.load("E:\D Drive Data\Project\Spotify Song Prediction System\Spotify-Song-Popularity-Predictor\models\model.pkl")
df = pd.read_csv("data").dropna()
X = df.drop(columns="popularity", axis=1)

explainer = shap.Explainer(model, X)
shap_values = explainer(X)

shap.summary_plot(shap_values, X)


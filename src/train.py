from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score
from xgboost import XGBRegressor
import joblib
from preprocess import preprocess


X, y = preprocess()

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
model.fit(X_train, y_train)

preds  = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, preds))
print("R2 Score:", r2_score(y_test, preds))

joblib.dump(model, "E:\D Drive Data\Project\Spotify Song Prediction System\Spotify-Song-Popularity-Predictor\models\model.pkl")

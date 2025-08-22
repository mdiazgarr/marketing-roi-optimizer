import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv('data/processed/engineered.csv')

# Features and target
X = df[['Clicks', 'Impressions', 'Cost', 'Conversions', 'CPC', 'CTR', 'CPA']]
y = df['ROI']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("R2 Score:", r2_score(y_test, y_pred))
print("RMSE:", rmse)

# Save model (optional)
import joblib
joblib.dump(model, 'models/roi_predictor.pkl')


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib


np.random.seed(42)

data = pd.DataFrame({
    'day_of_week': np.random.randint(1, 8, 100),
    'is_weekend': np.random.randint(0, 2, 100),
    'is_exam': np.random.randint(0, 2, 100),
    'weather': np.random.randint(0, 2, 100),
    'previous_attendance': np.random.randint(180, 350, 100)
})

data['attendance'] = (
    data['previous_attendance']
    - data['is_weekend'] * 80
    + data['is_exam'] * 40
    - data['weather'] * 30
    + np.random.randint(-10, 10, 100)
)


X = data.drop('attendance', axis=1)
y = data['attendance']


model = RandomForestRegressor()


model.fit(X, y)


pred = model.predict(X)


accuracy = r2_score(y, pred)

print("\n MODEL TRAINING COMPLETE")
print("=========================")
print(f" R² Score: {round(accuracy, 2)}")

import os
os.makedirs("outputs", exist_ok=True)


joblib.dump(model, "outputs/model.pkl")

print(" Model saved to outputs/model.pkl")

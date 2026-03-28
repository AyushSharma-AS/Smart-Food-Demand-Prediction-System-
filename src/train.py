import os
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error



print("\n" + "=" * 60)
print("   SMART FOOD DEMAND PREDICTION SYSTEM - TRAINING")
print("=" * 60)



print("\n[1/6] Generating dataset...")

np.random.seed(42)
n = 200

data = pd.DataFrame({
    'day_of_week': np.random.randint(1, 8, n),
    'day_of_month': np.random.randint(1, 31, n),
    'is_weekend': np.random.randint(0, 2, n),
    'is_exam': np.random.randint(0, 2, n),
    'holiday': np.random.randint(0, 2, n),
    'special_event': np.random.randint(0, 2, n),
    'weather': np.random.randint(0, 2, n),          # 0 = Clear, 1 = Rainy
    'meal_type': np.random.randint(0, 3, n),        # 0 = Breakfast, 1 = Lunch, 2 = Dinner
    'previous_attendance': np.random.randint(180, 350, n)
})

data['attendance'] = (
    data['previous_attendance']
    - data['is_weekend'] * 70
    + data['is_exam'] * 50
    - data['weather'] * 25
    - data['holiday'] * 60
    + data['special_event'] * 80
    + data['meal_type'] * 10
    + np.random.randint(-15, 15, n)
)

print("Dataset created successfully.")
print(f"Total records: {len(data)}")
print(f"Total features: {len(data.columns) - 1}")


print("\n[2/6] Preparing features and target...")

X = data.drop('attendance', axis=1)
y = data['attendance']

print("Features selected:")
for col in X.columns:
    print(f"  - {col}")



print("\n[3/6] Splitting dataset into training and testing sets...")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples : {len(X_test)}")



print("\n[4/6] Training Random Forest Regressor...")

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Model training completed successfully.")



print("\n[5/6] Evaluating model performance...")

predictions = model.predict(X_test)

r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

print("\n" + "-" * 60)
print("MODEL PERFORMANCE")
print("-" * 60)
print(f"R² Score             : {r2:.2f}")
print(f"Mean Absolute Error  : {mae:.2f}")



print("\n[6/6] Saving model and displaying feature importance...")

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
}).sort_values(by='Importance', ascending=False)

print("\nTop Feature Importance:")
print("-" * 60)
for _, row in feature_importance.iterrows():
    print(f"{row['Feature']:<22} : {row['Importance']:.3f}")

os.makedirs("outputs", exist_ok=True)
joblib.dump(model, "outputs/model.pkl")

print("\nModel saved successfully at: outputs/model.pkl")



print("\n" + "=" * 60)
print("   TRAINING COMPLETE")
print("=" * 60)
print("Project : Smart Food Demand Prediction System")
print("Model   : Random Forest Regressor")
print(f"Accuracy: R² = {r2:.2f}")
print(f"Error   : MAE = {mae:.2f}")
print("=" * 60)
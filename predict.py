import pandas as pd
import joblib

model = joblib.load("outputs/model.pkl")


day = int(input("Enter day (1=Mon, 7=Sun): "))
is_weekend = 1 if day in [6,7] else 0
is_exam = int(input("Exam Day? (1=Yes, 0=No): "))
weather = int(input("Weather (0=Clear, 1=Rainy): "))
prev = int(input("Previous Day Attendance: "))


input_data = pd.DataFrame({
    'day_of_week': [day],
    'is_weekend': [is_weekend],
    'is_exam': [is_exam],
    'weather': [weather],
    'previous_attendance': [prev]
})

prediction = int(model.predict(input_data)[0])


days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


print("\n" + "="*45)
print("   SMART FOOD DEMAND PREDICTION")
print("="*45)

print(f"Day: {days[day-1]}")
print(f"Weather: {'Rainy' if weather else 'Clear'}")
print(f"Exam: {'Yes' if is_exam else 'No'}")
print(f"Previous Attendance: {prev}")

print("\nPrediction Result")
print("-"*45)
print(f" Expected Students: {prediction}")

# Decision system
print("\nRecommendation")
print("-"*45)

if prediction > 300:
    print("Prepare HIGH quantity of food")
elif prediction > 230:
    print("Prepare MODERATE quantity")
else:
    print("Prepare LOW quantity (reduce waste)")

print("="*45)
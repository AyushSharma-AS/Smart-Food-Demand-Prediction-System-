import joblib
import pandas as pd


print("\n" + "=" * 60)
print("   SMART FOOD DEMAND PREDICTION SYSTEM - PREDICTION")
print("=" * 60)


model = joblib.load("outputs/model.pkl")


day_map = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

meal_map = {
    0: "Breakfast",
    1: "Lunch",
    2: "Dinner"
}

weather_map = {
    0: "Clear",
    1: "Rainy"
}




print("\n[1/3] Enter meal demand details")
print("-" * 60)

print("\nSelect Day:")
for key, value in day_map.items():
    print(f"  {key}. {value}")
day = int(input("Enter day number (1-7): "))

day_of_month = int(input("Enter day of month (1-31): "))
is_weekend = int(day in [6, 7])

is_exam = int(input("Exam Day? (1=Yes, 0=No): "))
holiday = int(input("Holiday? (1=Yes, 0=No): "))
special_event = int(input("Special Event? (1=Yes, 0=No): "))

print("\nWeather:")
for key, value in weather_map.items():
    print(f"  {key}. {value}")
weather = int(input("Enter weather option (0-1): "))

print("\nMeal Type:")
for key, value in meal_map.items():
    print(f"  {key}. {value}")
meal_type = int(input("Enter meal type number (0-2): "))

previous_attendance = int(input("Enter previous day attendance: "))



print("\n[2/3] Preparing input data...")
print("-" * 60)

input_data = pd.DataFrame({
    'day_of_week': [day],
    'day_of_month': [day_of_month],
    'is_weekend': [is_weekend],
    'is_exam': [is_exam],
    'holiday': [holiday],
    'special_event': [special_event],
    'weather': [weather],
    'meal_type': [meal_type],
    'previous_attendance': [previous_attendance]
})

print("Input data prepared successfully.")



print("\n[3/3] Predicting attendance...")
print("-" * 60)

prediction = int(model.predict(input_data)[0])



print("\n" + "=" * 60)
print("                     PREDICTION RESULT")
print("=" * 60)

print(f"Day                 : {day_map[day]}")
print(f"Day of Month        : {day_of_month}")
print(f"Weekend             : {'Yes' if is_weekend else 'No'}")
print(f"Exam Day            : {'Yes' if is_exam else 'No'}")
print(f"Holiday             : {'Yes' if holiday else 'No'}")
print(f"Special Event       : {'Yes' if special_event else 'No'}")
print(f"Weather             : {weather_map[weather]}")
print(f"Meal Type           : {meal_map[meal_type]}")
print(f"Previous Attendance : {previous_attendance}")
print("-" * 60)
print(f"Expected Students   : {prediction}")

print("\nRecommendation")
print("-" * 60)
if prediction > 320:
    print("Prepare HIGH quantity of food")
elif prediction > 240:
    print("Prepare MODERATE quantity of food")
else:
    print("Prepare LOW quantity of food to reduce waste")

print("=" * 60)
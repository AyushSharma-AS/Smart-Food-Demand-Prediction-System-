# Smart Food Demand Prediction System

## Overview

The **Smart Food Demand Prediction System** is a Machine Learning-based project designed to reduce food wastage in college mess or hostel environments.

It predicts the number of students likely to attend meals based on real-world factors and provides actionable recommendations for food preparation.

---

## Problem Statement

In many institutions, food is prepared based on rough estimates, leading to:

* Excess food wastage
* Financial loss
* Environmental impact

This project solves the problem by using **data-driven predictions** instead of guesswork.

---

## Solution

This system uses **Machine Learning (Random Forest Regressor)** to:

* Predict daily attendance
* Analyze influencing factors
* Provide food preparation recommendations

---

## Key Features

* Predicts student attendance using ML
* Considers real-world factors:

  * Day of the week
  * Weekend indicator
  * Exam schedule
  * Weather conditions
  * Previous attendance
* Uses Random Forest (ensemble learning)
* Provides actionable recommendations
* Clean and user-friendly output

---

## Key Highlight

 This project is designed as a **Decision Support System**, not just a prediction model.

---

## Tech Stack

* **Language:** Python
* **Libraries:**

  * pandas
  * numpy
  * scikit-learn
  * joblib

---

## Project Structure

```
smart-food-demand-prediction/
│
├── data/
│   └── dataset.csv
│
├── src/
│   ├── train.py
│   └── predict.py
│
├── outputs/
│   └── model.pkl
│
├── docs/
│   └── Project_Report.pdf
│
├── requirements.txt
└── README.md
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/smart-food-demand-prediction.git
cd smart-food-demand-prediction
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

### Step 1: Train the Model

```bash
python src/train.py
```

### Step 2: Run Prediction

```bash
python src/predict.py
```

---

## Sample Output

```
=============================================
   SMART FOOD DEMAND PREDICTION
=============================================
Day: Monday
Weather: Clear
Exam: No
Previous Attendance: 280

Prediction Result
---------------------------------------------
Expected Students: 310

Recommendation
---------------------------------------------
Prepare HIGH quantity of food
=============================================
```

---

## Model Details

* **Algorithm Used:** Random Forest Regressor

* **Why Random Forest?**

  * Handles non-linear relationships
  * More accurate than simple regression
  * Reduces overfitting

* **Evaluation Metric:**

  * R² Score (for accuracy measurement)

---

## Challenges Faced

* Lack of real-world dataset
* Feature selection and engineering
* Avoiding overfitting
* Making output user-friendly

---

## Key Learnings

* Practical application of Machine Learning
* Importance of feature engineering
* Model evaluation techniques
* Building real-world AI solutions

---

## Future Improvements

* Web or mobile application (Streamlit)
* Real-time data integration
* Advanced models (Deep Learning)
* Dashboard with analytics

---

## Author

**Ayush Sharma**

---

## Acknowledgement

This project was developed as part of an **AI & Machine Learning course**, applying theoretical concepts to solve a real-world problem.

---

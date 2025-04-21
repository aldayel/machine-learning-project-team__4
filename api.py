# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# # Define input data schema using PascalCase fields
# class InputData(BaseModel):
#     Age: int
#     Gender: str
#     Height_cm: float
#     Weight_kg: float
#     Heart_Rate: float
#     Workout_Duration_mins: int
#     Workout_Days: int
#     Workout_Type: str

# @app.post("/calculate-calories")
# def calculate_calories(data: InputData):
#     # Define workout factors
#     workout_factors = {
#         "None": 0,
#         "Yoga": 1,
#         "Dancing": 2,
#         "Cardio": 3,
#         "HIIT": 4
#     }
    
#     workout_factor = workout_factors.get(data.Workout_Type, 0)

#     # Calculate calories
#     calories_per_min = (data.Heart_Rate * data.Weight_kg * 0.0007) + (data.Age * 0.01) + workout_factor
#     calories_total = calories_per_min * data.Workout_Duration_mins

#     # Calculate BMI
#     bmi = data.Weight_kg / ((data.Height_cm / 100) ** 2)

#     return {
#         "Total_Calories": round(calories_total, 2),
#         "Calories_Per_Minute": round(calories_per_min, 2),
#         "BMI": round(bmi, 2)
#     }


from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load assets for recommendation model
recommender_model = joblib.load("recommender_rf_model.pkl")
label_encoders = joblib.load("recommender_label_encoders.pkl")
feature_names = joblib.load("recommender_features.pkl")  # Optional if needed

# -----------------------------
# 🔸 Calories Calculator Endpoint
# -----------------------------
class CaloriesInput(BaseModel):
    Age: int
    Gender: str
    Height_cm: float
    Weight_kg: float
    Heart_Rate: float
    Workout_Duration_mins: int
    Workout_Days: int
    Workout_Type: str

@app.post("/calculate-calories")
def calculate_calories(data: CaloriesInput):
    workout_factors = {
        "None": 0, "Yoga": 1, "Dancing": 2, "Cardio": 3, "HIIT": 4
    }
    factor = workout_factors.get(data.Workout_Type, 0)
    cal_per_min = (data.Heart_Rate * data.Weight_kg * 0.0007) + (data.Age * 0.01) + factor
    total_cal = cal_per_min * data.Workout_Duration_mins
    bmi = data.Weight_kg / ((data.Height_cm / 100) ** 2)

    return {
        "total_calories": round(total_cal, 2),
        "calories_per_min": round(cal_per_min, 2),
        "bmi": round(bmi, 2)
    }

# -----------------------------
# 🔸 Workout Recommendation Endpoint
# -----------------------------
class RecommenderInput(BaseModel):
    Age: int
    Gender: str
    Height_cm: float
    Weight_kg: float
    Workout_Intensity: str
    Workout_Duration_mins: int
    Workout_Days: int

@app.post("/recommend-workout")
def recommend_workout(data: RecommenderInput):
    # Feature engineering
    height_m = data.Height_cm / 100
    bmi = data.Weight_kg / (height_m ** 2)
    duration_per_day = data.Workout_Duration_mins / data.Workout_Days

    # Encoding
    gender_encoded = label_encoders['Gender'].transform([data.Gender])[0]
    intensity_encoded = label_encoders['Workout Intensity'].transform([data.Workout_Intensity])[0]

    features = [
        data.Age,
        gender_encoded,
        intensity_encoded,
        data.Workout_Days,
        bmi,
        duration_per_day
    ]

    pred = recommender_model.predict([features])[0]
    category = label_encoders['Workout Category'].inverse_transform([pred])[0]

    return {
        "recommended_category": category
    }



# test_api.py

# ----------
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def hello():
#     return {"message": "Hello"}




# @app.get("/Calo_Calculater")

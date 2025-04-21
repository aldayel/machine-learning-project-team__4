import streamlit as st
import requests

st.set_page_config(page_title="🔥 Calorie Calculator", page_icon="🏋️", layout="centered")
st.title("🔥 Calorie Calculator (via FastAPI)")

# User inputs
weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=79.0)
height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=173.0)
age = st.number_input("Age", min_value=10, max_value=100, value=23)
gender = st.selectbox("Gender", ["Male", "Female"])
heart_rate = st.slider("Average Heart Rate", min_value=60, max_value=200, value=120)
duration = st.slider("Workout Duration (minutes)", min_value=10, max_value=120, value=30)
workout_days = st.slider("Workout Days per Week", min_value=1, max_value=7, value=3)
workout_type = st.selectbox("Workout Type", ["None", "Yoga", "Dancing", "Cardio", "HIIT"])

if st.button("💥 Calculate Calories"):
    # Send to FastAPI
    payload = {
        "Age": age,
        "Gender": gender,
        "Height_cm": height,
        "Weight_kg": weight,
        "Heart_Rate": heart_rate,
        "Workout_Duration_mins": duration,
        "Workout_Days": workout_days,
        "Workout_Type": workout_type
    }

    try:
        response = requests.post("http://127.0.0.1:8000/calculate-calories", json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"🔥 Total Calories Burned: {result['Total_Calories']} kcal")
            st.info(f"⚖️ BMI: {result['BMI']}")
        else:
            st.error(f"❌ Error from API: {response.text}")
    except Exception as e:
        st.error(f"🚨 Could not reach FastAPI: {e}")

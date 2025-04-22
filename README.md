# 🏋️‍♀️ Fitness Vision - Workout Recommendation System

Fitness Vision is a machine learning-powered system designed to recommend workout categories and generate personalized exercise plans based on user profiles (age, gender, BMI, workout intensity, etc.). It includes both a predictive model for workout category classification and an exercise plan generator using the ExerciseDB API, along with a calories calculator.

---

## 👥 Team Members

-Najla Almarshde
-Wasan Alotaibi
-Abdullah Aldayel
-Faisal Almufarrih
-Abdulmohsen Aldughayem



---

## 📊 Data Source
- **Dataset**: [Workout & Fitness Tracker Dataset](https://www.kaggle.com/datasets/arashnic/workout-and-fitness-tracker-data) from Kaggle.
- **Description**: Contains user demographics, workout durations, intensities, and workout types.
- **External API**: [ExerciseDB API](https://rapidapi.com/justin-WFnsXH_t6/api/exercisedb/) for fetching exercise details (body part, target muscle, equipment, GIFs).

---

## 🗂️ Project Structure

```bash
├── data/
│   ├── cleaned_workout_fitness_tracker_data.csv  # Processed data
│   ├── workout_fitness_tracker_data.csv          # Original dataset
├── deployment/
│   ├── Backend/
│   │   ├── api.py                                # API endpoint for backend
│   │   ├── label_encoders.joblib                 # Encoded labels for model inference
│   │   ├── recommendation_model.joblib           # Trained classification model
│   │   ├── requirements.txt                      # Backend dependencies
│   ├── frontend/
│   │   ├── app.py                                # Frontend application
│   │   ├── requirements.txt                      # Frontend dependencies            # Model training script
├── notebooks/
│   ├── Recommend_workout_model.ipynb     
│   ├── Recommendatio_RF.ipynb         # EDA, model training, evaluation
├── slides/  
│   ├── Fit-Vision-Presentation.pdf                                     # Presentation slides
├── README.md                                     # Project documentation
```

---

## 🛠️ Tools & Libraries
- **Python**: `pandas`, `numpy`, `scikit-learn`, `joblib`, `requests`
- **Deployment**: `FastAPI`, `Uvicorn`

---


## 🎯 Key Features

- **Workout type Recommendation**:  
  - Predicts the optimal workout **category** (`Endurance`, `High Effort`, `Flexibility`) based on user inputs like age, weight, height, and more.
  - Provides specific exercise types within each category. Example:  
    - *Endurance Training* is a Good Fit for You!  
    - Recommended exercises:  
      - Cardio  
      - Running  
      - Cycling  

 
- **Calorie Needs Estimation and Burn Tracking**:  
- Calculates **calories burned** based on user profile and activity level during workouts by factoring in exercise type, duration, intensity level, and more.

- **Personalized Exercise Plans**:  
  - Suggests exercises targeting **specific muscles**, **body parts**, or **full-body routines**.  
  - Integrates with **ExerciseDB API** to provide:
    - Exercise images  
    - Equipment details  
    - Targeted body parts information



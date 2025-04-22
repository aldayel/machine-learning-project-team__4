# 🏋️‍♀️ Fit Vision - Workout Recommendation System

Fit Vision is a machine learning-powered system designed to recommend workout categories and generate personalized exercise plans based on user profiles (age, gender, BMI, workout intensity, etc.). It includes both a predictive model for workout category classification and an exercise plan generator using the ExerciseDB API also a calories calculator. 

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
│   ├── api.py                                    # API endpoint for deployment
│   ├── app.py                                    # Main deployment application
│   ├── generate_workout_plan.py                  # Logic for exercise plan generation
│   ├── label_encoders.joblib                     # Encoded labels for model inference
│   ├── recommendation_model.joblib               # Trained classification model
│   ├── recommender_model_training.py             # Model training script
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
- **Visualization**: `matplotlib`, `seaborn`

---

## 🚀 Usage

1. **Clone the repository**:
   ```bash
   git clone [repo_url]
   cd [repo_name]
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Jupyter notebooks for data processing and model training**:
   ```bash
   jupyter notebook notebooks/Recommend_workout_model.ipynb
   ```

4. **Launch the API (optional)**:
   ```bash
   cd deployment
   uvicorn api:app --reload
   ```

---

## 🎯 Key Features
- Predict workout category (`Endurance`, `High Effort`, `Flexibility`) based on user input.
- Generate personalized exercise plans:
  - Based on **muscle target**, **body part**, or **full-body**.
  - Fetches exercise images, equipment, and body part details from the ExerciseDB API.

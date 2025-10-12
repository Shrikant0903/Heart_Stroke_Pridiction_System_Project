import streamlit as st
import pandas as pd
import joblib

# --- Page Config ---
st.set_page_config(
    page_title="🫀 Heart Stroke Prediction System",
    layout="centered"
)

# --- Title and Description ---
st.title("🫀 Heart Stroke Prediction System")
st.markdown("Enter patient details below to predict the risk of stroke using KNN.")
st.markdown("---")  # horizontal line

# --- Load model and scaler ---
knn_model = joblib.load("models/knn_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# --- Manual mappings for categorical columns ---
gender_mapping = {"Male": 0, "Female": 1}
married_mapping = {"No": 0, "Yes": 1}
work_mapping = {"Private": 0, "Self-employed": 1, "Govt_job": 2, "Children": 3, "Never_worked": 4}
residence_mapping = {"Rural": 0, "Urban": 1}
smoking_mapping = {"formerly smoked": 0, "never smoked": 1, "smokes": 2, "Unknown": 3}

# --- Helper functions ---
def options_from_mapping(mapping):
    return [f"{k} = {v}" for k, v in mapping.items()]

def extract_code(option):
    return int(option.split('=')[-1].strip())

def validate_inputs(age, bmi, glucose):
    errors = []
    if not (0 <= age <= 120):
        errors.append("Age must be between 0 and 120.")
    if not (10 <= bmi <= 70):
        errors.append("BMI must be between 10 and 70.")
    if not (50 <= glucose <= 300):
        errors.append("Average Glucose Level must be between 50 and 300.")
    return errors

# --- Input Form (all in one column layout) ---
with st.container():
    st.subheader("Patient Details")
    
    # Numeric inputs
    age = st.number_input("Age", min_value=0, max_value=120, value=30, step=1)
    bmi = st.number_input("BMI", min_value=10.0, max_value=70.0, value=25.0, step=0.1)
    avg_glucose_level = st.number_input("Average Glucose Level", min_value=50.0, max_value=300.0, value=100.0, step=0.1)

    # Categorical inputs
    gender_sel = st.selectbox("Gender", options_from_mapping(gender_mapping))
    ever_married_sel = st.selectbox("Ever Married", options_from_mapping(married_mapping))
    work_type_sel = st.selectbox("Work Type", options_from_mapping(work_mapping))
    residence_sel = st.selectbox("Residence Type", options_from_mapping(residence_mapping))
    smoking_sel = st.selectbox("Smoking Status", options_from_mapping(smoking_mapping))

    # Binary inputs
    hypertension = st.selectbox("Hypertension", [0, 1])
    heart_disease = st.selectbox("Heart Disease", [0, 1])

# --- Predict Button ---
if st.button("Predict Stroke Risk"):
    # Validate inputs
    errors = validate_inputs(age, bmi, avg_glucose_level)
    if errors:
        for err in errors:
            st.error(err)
    else:
        # Prepare input DataFrame
        input_dict = {
            "gender": extract_code(gender_sel),
            "age": age,
            "hypertension": hypertension,
            "heart_disease": heart_disease,
            "ever_married": extract_code(ever_married_sel),
            "work_type": extract_code(work_type_sel),
            "Residence_type": extract_code(residence_sel),
            "avg_glucose_level": avg_glucose_level,
            "bmi": bmi,
            "smoking_status": extract_code(smoking_sel)
        }

        df_input = pd.DataFrame([input_dict])

        # Scale numeric columns
        numeric_cols = ['age', 'bmi', 'avg_glucose_level']
        df_input[numeric_cols] = scaler.transform(df_input[numeric_cols])

        # Predict
        pred = knn_model.predict(df_input)
        if pred[0] == 1:
            st.error("⚠️ Patient is at risk of stroke")
        else:
            st.success("✅ Patient is not at risk of stroke")

# --- Footer ---
st.markdown("---")
st.caption("Made by Shrikant")

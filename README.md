# Heart_Stroke_Pridiction_System_Project
Heart Stroke Prediction System – A Streamlit web app that predicts stroke risk using a trained KNN model. Users input age, BMI, glucose, gender, marital status, work type, residence, smoking, hypertension, and heart disease for instant risk prediction.
# 🫀 Heart Stroke Prediction System

A **Streamlit-based web application** that predicts the risk of **stroke** in patients using a **K-Nearest Neighbors (KNN)** model. Users can input patient details and get **instant predictions**, along with visualizations of the dataset.  

---

## ✨ Features

- 🧑‍⚕️ **Patient Data Inputs**:
  - Age, BMI, Average Glucose Level  
  - Gender, Marital Status, Work Type, Residence Type  
  - Smoking Status, Hypertension, Heart Disease  

- 🛠 **Data Preprocessing**:
  - Remove `id` column  
  - Fill missing **BMI** values with mean  
  - Encode categorical variables using `LabelEncoder`  
  - Scale numeric features with `StandardScaler`  
  - Handle imbalanced dataset using **SMOTE**  

- 📊 **Model & Evaluation**:
  - **Algorithm:** K-Nearest Neighbors (KNN)  
  - **Accuracy:** ~80%  
  - Confusion Matrix & Classification Report  
  - Visualizations: Stroke distribution, Age vs Glucose, BMI distribution  

- 🖥 **Streamlit Frontend**:
  - Dropdowns show readable labels with codes (e.g., `Male = 0`)  
  - Real-time input validation for Age, BMI, Glucose  
  - Compact one-page layout  
  - Background image with **50% transparency**  
  - Footer credit: **Made by Shrikant**

---

## 🚀 Installation

1. **Clone the repo**:

```bash
git clone https://github.com/your-username/heart_stroke_prediction_system.git
cd heart_stroke_prediction_system

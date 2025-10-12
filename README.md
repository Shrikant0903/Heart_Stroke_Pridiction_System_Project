# 🫀 Heart Stroke Prediction System

[![Live App](https://img.shields.io/badge/🌐_Live_App-Click_Here-brightgreen?style=for-the-badge)](https://heartstroke-prediction-system.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-View_Repository-black?style=for-the-badge&logo=github)](https://github.com/shrikant0903/Heart_Stroke_Pridiction_System_Project)

---

## 💡 Overview

The **Heart Stroke Prediction System** is an interactive **Streamlit web application** that predicts the likelihood of a person having a **stroke** based on health and lifestyle parameters.  
It utilizes a **Machine Learning (KNN)** model trained on medical data to provide **real-time risk assessment** with an easy-to-use interface.

This project bridges **data science** and **healthcare**, helping users and doctors analyze potential stroke risks before symptoms appear.

---

## ✨ Key Features

- 🧠 **Machine Learning-Based Prediction**
  - Uses **K-Nearest Neighbors (KNN)** algorithm for classification
  - Accuracy around **80%**

- 👨‍⚕️ **User Input Parameters**
  - Age, Gender, Marital Status, Work Type, Residence Type  
  - Hypertension, Heart Disease, Smoking Status  
  - Average Glucose Level, BMI  

- 🛠 **Data Preprocessing**
  - Missing **BMI** values replaced with mean  
  - Categorical features encoded using **LabelEncoder**  
  - Numeric values scaled using **StandardScaler**  
  - Data imbalance handled via **SMOTE (Synthetic Minority Oversampling Technique)**

- 📈 **Model Evaluation**
  - Confusion Matrix  
  - Classification Report  
  - Accuracy Score  
  - Visual plots showing feature relationships

- 💻 **Streamlit Frontend**
  - Clean, responsive, one-page design  
  - Dropdowns with meaningful labels  
  - Real-time prediction output  
  - Transparent background styling  
  - Footer credit: *“Made by Shrikant”*

---

## 🧩 Project Workflow

1. **Data Loading** → CSV dataset loaded using pandas  
2. **Data Cleaning** → Handle nulls, remove ID column  
3. **Encoding** → Convert categorical data to numeric  
4. **Scaling** → Normalize features  
5. **Balancing** → Apply SMOTE for class balancing  
6. **Model Training** → Train KNN classifier  
7. **Evaluation** → Assess model performance  
8. **Deployment** → Build UI using Streamlit  

---

## 🖼️ Screenshots

| 🩺 Input Form | 📊 Prediction Output |
|---------------|----------------------|
| ![App Screenshot 1](https://github.com/shrikant0903/Heart_Stroke_Pridiction_System_Project/blob/main/Screenshot1.png) | ![App Screenshot 2](https://github.com/shrikant0903/Heart_Stroke_Pridiction_System_Project/blob/main/Screenshot2.png) |

---

## 🚀 Live Demo

Try the live application here 👇  
🔗 **[Heart Stroke Prediction System (Streamlit App)](https://heartstroke-prediction-system.streamlit.app/)**  

No installation required — runs directly in your browser!

---

## ⚙️ Installation (Run Locally)

Clone this repository and install dependencies:

```bash
git clone https://github.com/shrikant0903/Heart_Stroke_Pridiction_System_Project.git
cd Heart_Stroke_Pridiction_System_Project
pip install -r requirements.txt
streamlit run app.py

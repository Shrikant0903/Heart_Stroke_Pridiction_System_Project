# 🫀 Heart Stroke Prediction System

[![Live App](https://img.shields.io/badge/🌐_Live_App-Click_Here-brightgreen?style=for-the-badge)](https://heartstroke-prediction-system.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-View_Repository-black?style=for-the-badge&logo=github)](https://github.com/shrikant0903/Heart_Stroke_Pridiction_System_Project)

---

## 🩺 Overview

**Heart Stroke Prediction System** – A **Streamlit-based web application** that predicts the risk of **stroke** in patients using a **K-Nearest Neighbors (KNN)** model.  
Users can input patient details and get **instant predictions**, along with **visualizations** of the dataset.

---

## ✨ Features

- 🧑‍⚕️ **Patient Data Inputs**:
  - Age, BMI, Average Glucose Level  
  - Gender, Marital Status, Work Type, Residence Type  
  - Smoking Status, Hypertension, Heart Disease  

- 🛠 **Data Preprocessing**:
  - Removed `id` column  
  - Filled missing **BMI** values with mean  
  - Encoded categorical variables using **LabelEncoder**  
  - Scaled numeric features using **StandardScaler**  
  - Handled imbalanced data using **SMOTE**  

- 📊 **Model & Evaluation**:
  - Algorithm: **K-Nearest Neighbors (KNN)**  
  - Accuracy: **~80%**  
  - Evaluation: Confusion Matrix, Classification Report  
  - Visualizations: Stroke distribution, Age vs Glucose, BMI distribution  

- 💻 **Streamlit Frontend**:
  - Dropdowns show readable labels with codes (e.g., `Male = 0`)  
  - Real-time input validation  
  - Compact one-page layout  
  - Background image with 50% transparency  
  - Footer credit: **Made by Shrikant**

---

## 🖼️ App Screenshots

| 🩸 Input Form | 📈 Prediction Output |
|---------------|----------------------|
| ![App Screenshot 1](https://github.com/shrikant0903/Heart_Stroke_Pridiction_System_Project/blob/main/Screenshot1.png) | ![App Screenshot 2](https://github.com/shrikant0903/Heart_Stroke_Pridiction_System_Project/blob/main/Screenshot2.png) |

---

## 🚀 Installation

To run locally:

```bash
git clone https://github.com/shrikant0903/Heart_Stroke_Pridiction_System_Project.git
cd Heart_Stroke_Pridiction_System_Project
pip install -r requirements.txt
streamlit run app.py

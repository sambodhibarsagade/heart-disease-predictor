# ❤️ Heart Disease Predictor
**Final Year Project by Sambodhi Barsagade — PG Diploma Student**

A Machine Learning web application that predicts the risk of heart disease based on user inputs such as age, cholesterol, and blood pressure.

---

## 📚 Table of Contents
- [Introduction](#introduction)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Connect with Me](#connect-with-me)

---

## 🩺 Introduction
Cardiovascular diseases are a leading global health concern. This web app predicts heart disease risk using trained ML models. It demonstrates real-world use of ML in healthcare through a user-friendly interface.

---

## 🚀 Key Features
- **Dual ML Models:**
  - **Decision Tree**: Fast, interpretable predictions.
  - **K-Nearest Neighbors (KNN)**: Predictions based on similarity.
- **User-Friendly Form**: Clean, responsive design for input.
- **Real-Time Results**: Displays prediction and confidence level.
- **Mobile Friendly**: Works on any device.

---

## 🔧 Technologies Used

### ML Models
- **Decision Tree** (Scikit-learn)
- **KNN Classifier** (Scikit-learn)

### Backend
- **Python**
- **Flask**
- **joblib** for saving/loading models

### Frontend
- **HTML / CSS**
- **Jinja2** for rendering
- **Bootstrap-like layout** (custom responsive styles)

---

## 📊 Dataset: `heart.csv`
Trained on UCI Heart Disease dataset with these features:

| Feature    | Description                                |
|------------|--------------------------------------------|
| age        | Age in years                               |
| sex        | Gender (0 = Female, 1 = Male)              |
| cp         | Chest pain type (0–3)                      |
| trestbps   | Resting blood pressure (mmHg)              |
| chol       | Serum cholesterol (mg/dL)                  |
| fbs        | Fasting blood sugar > 120 mg/dL (0/1)      |
| restecg    | Resting ECG results (0–2)                  |
| thalach    | Maximum heart rate achieved                |
| exang      | Exercise-induced angina (0 = No, 1 = Yes)  |
| oldpeak    | ST depression from exercise                |
| slope      | Slope of ST segment (0–2)                  |
| ca         | Number of major vessels (0–3)              |
| thal       | Thalassemia (1 = Normal, 2/3 = Defect)     |
| target     | 0 = No disease, 1 = Risk present           |

---

## ⚙️ How It Works

1. **User Input**: Fill out the health form.
2. **Preprocessing**: Input is scaled with `StandardScaler`.
   ```python
   scaled_input = scaler.transform([user_input])

# ❤️ Heart Disease Predictor
**Final Year Project by Sambodhi Barsagade — PG Diploma Student**

A Machine Learning web application that predicts the risk of heart disease based on user inputs such as age, cholesterol, and blood pressure.



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



##  Introduction
Cardiovascular diseases are a leading global health concern. This web app predicts the risk of heart disease using Machine Learning models trained on clinical data. Designed as a final-year MCA project, it demonstrates the practical application of ML in healthcare by providing actionable insights based on user inputs like age, cholesterol, and blood pressure.



##  Key Features
- **Dual ML Models:**
  - **Decision Tree**: Fast, interpretable predictions.
  - **K-Nearest Neighbors (KNN)**: Predictions based on similarity.
- **User-Friendly Form**: Clean, responsive design for input.
- **Real-Time Results**: Displays prediction and confidence level.
- **Mobile Friendly**: Works on any device.



##  Technologies Used

### ML Models
- **Decision Tree** (Scikit-learn)
     A supervised learning algorithm that splits data into branches using feature thresholds (e.g., "Is cholesterol > 200?") to make predictions.
     Advantages: Easy to visualize, no need for feature scaling.
- **KNN Classifier** (Scikit-learn)
     A lazy learning algorithm that classifies data points based on the majority class of their *k* nearest neighbors (default *k=5*).
     Advantages: Simple implementation, no training phase.

### Backend
- **Python** : Core language for logic and ML model training.
- **Flask** : Lightweight web framework to handle routing and HTTP requests.
- **Scikit-learn** : Library for model training (DecisionTreeClassifier, KNeighborsClassifier).
- **joblib** : for saving/loading models

### Frontend
- **HTML / CSS** :  Structures and styles the input form and results page.
- **Jinja2** : Templating engine to dynamically render HTML with Python variables.
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



## ⚙️ How It Works

1. **User Input**: Fill out the health form.
2. **Preprocessing**: Input is scaled with `StandardScaler`.
   scaled_input = scaler.transform([user_input])

Prediction:

Decision Tree and KNN models both make predictions.

Higher confidence model is selected for final display.

Output: Prediction and advice are shown on a results page.

Installation
Prerequisites:
Python 3.8+


Steps:
# 1. Clone the repository
git clone https://github.com/yourusername/heart-disease-predictor.git
cd heart-disease-predictor

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py

# 5. Open in browser
http://127.0.0.1:5000
📄 License
This project is licensed under the MIT License.

🙏 Acknowledgments
UCI Machine Learning Repository for the dataset

Inspired by healthcare ML tutorials from Kaggle and freeCodeCamp

📬 Connect with Me
Email: sambodhibarsagade@gmail.com

LinkedIn: [Your LinkedIn URL]

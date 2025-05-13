# heart-disease-predictor
❤️ Heart Disease Prediction Web Application
Final Year Project by Sambodhi Barsagade , PG Diploma Student
 
 

 Table of Contents
•	Introduction
•	Key Features
•	Technologies Used
•	Dataset
•	How It Works
•	Installation
•	License
•	Acknowledgments


 Introduction
Cardiovascular diseases are a leading global health concern. This web app predicts the risk of heart disease using Machine Learning models trained on clinical data. Designed as a final-year MCA project, it demonstrates the practical application of ML in healthcare by providing actionable insights based on user inputs like age, cholesterol, and blood pressure.
________________________________________
 Key Features
•	Dual ML Models:
o	Decision Tree: Fast, interpretable predictions using rule-based splits.
o	K-Nearest Neighbors (KNN): Robust predictions based on similarity to historical data.
•	User-Friendly Interface: Input health metrics via a simple web form.
•	Real-Time Results: Displays risk level (Low/High) and model confidence.
•	Responsive Design: Works seamlessly on all devices.
________________________________________
Technologies Used
1. Machine Learning Models
•	Decision Tree:
o	A supervised learning algorithm that splits data into branches using feature thresholds (e.g., "Is cholesterol > 200?") to make predictions.
o	Advantages: Easy to visualize, no need for feature scaling.
•	K-Nearest Neighbors (KNN):
o	A lazy learning algorithm that classifies data points based on the majority class of their *k* nearest neighbors (default *k=5*).
o	Advantages: Simple implementation, no training phase.
2. Backend
•	Python: Core language for logic and ML model training.
•	Flask: Lightweight web framework to handle routing and HTTP requests.
•	Scikit-learn: Library for model training (DecisionTreeClassifier, KNeighborsClassifier).
3. Frontend
•	HTML/CSS: Structures and styles the input form and results page.
•	Jinja2: Templating engine to dynamically render HTML with Python variables.
________________________________________

📊 Dataset: heart.csv
The model is trained on the Heart Disease Dataset with the following features:
Feature	Description	Type/Values
age	Age in years	Integer (29-77)
sex	Gender	0 = Female, 1 = Male
cp	Chest pain type	0-3 (e.g., 0 = typical angina)
trestbps	Resting blood pressure (mmHg)	Integer
chol	Serum cholesterol (mg/dL)	Integer
fbs	Fasting blood sugar > 120 mg/dL	0 = No, 1 = Yes
restecg	Resting electrocardiographic results	0-2
thalach	Maximum heart rate achieved	Integer
exang	Exercise-induced angina	0 = No, 1 = Yes
oldpeak	ST depression induced by exercise	Float
slope	Slope of peak exercise ST segment	0-2
ca	Number of major vessels	0-3
thal	Thalassemia type	1-3
target	Presence of heart disease	0 = No, 1 = Yes

Preprocessing Steps:
1.	Handled missing values (e.g., thal filled with mode).
2.	Scaled features using StandardScaler for KNN.
3.	Split data into 80% training and 20% testing sets.
________________________________________
 How It Works
Workflow:
1.	User Input: Submit health metrics via the web form.
2.	Data Preprocessing:
o	Inputs are scaled to match training data format.
scaler = StandardScaler()  
scaled_inputs = scaler.transform([user_inputs])  

3.	Model Prediction:
o	Both models generate risk predictions.
dt_prediction = dt_model.predict(scaled_inputs)  # Decision Tree  
knn_prediction = knn_model.predict(scaled_inputs) # KNN  

4.	Result Display: Rendered dynamically using Jinja2.
<h3>Decision Tree Prediction: {{ dt_pred }}</h3>  
<h3>KNN Prediction: {{ knn_pred }}</h3>  
________________________________________
 Installation
Prerequisites:
•	Python 3.8+
•	pip
Steps:
1.	Clone the repository:
git clone https://github.com/yourusername/heart-disease-prediction.git  
cd heart-disease-prediction  

2.	Set up a virtual environment:
python -m venv venv  
source venv/bin/activate  # Windows: venv\Scripts\activate  

3.	Install dependencies:
pip install -r requirements.txt  

4.	Run the app:
python app.py  

5.	Access the app: Open http://127.0.0.1:5000 in your browser.
________________________________________
License
This project is licensed under the MIT License.
________________________________________
 Acknowledgments
•	Dataset adapted from the UCI Machine Learning Repository.
•	Inspired by healthcare ML tutorials on Kaggle and freeCodeCamp.
________________________________________
Connect with me!
🔗 LinkedIn | 🌐 Portfolio | 📧 your.email@example.com
(Replace placeholder links before uploading!)


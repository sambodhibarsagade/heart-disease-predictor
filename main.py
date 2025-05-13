import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import joblib
import os

# Ensure 'static' folder exists
if not os.path.exists('static'):
    os.makedirs('static')

# Load dataset
heart = pd.read_csv('heart.csv')

# Split features and target
X = heart.drop('target', axis=1)
y = heart['target']

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save the scaler
joblib.dump(scaler, 'static/scaler.pkl')

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=10)

# Train Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
joblib.dump(dt, 'static/decision_tree_model.pkl')

# Train KNN
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
joblib.dump(knn, 'static/knn_model.pkl')

# Gender comparison plot
plt.figure(figsize=(8,6))
sns.countplot(data=heart, x='sex', hue='target', palette="Set2")
plt.title("Heart Disease by Gender")
plt.savefig('static/gender_comparison.png')
plt.close()

# Age comparison plot
plt.figure(figsize=(8,6))
sns.boxplot(data=heart, x='target', y='age', hue='target', palette="Set2")
plt.legend().remove()
plt.title("Age Distribution by Heart Disease")
plt.savefig('static/age_comparison.png')
plt.close()

print("✅ Models, scaler, and plots saved in 'static/' folder.")

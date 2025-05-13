from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained models and scaler from the 'static' folder
try:
    dt_model = joblib.load('static/decision_tree_model.pkl')
    knn_model = joblib.load('static/knn_model.pkl')
    scaler = joblib.load('static/scaler.pkl')
except FileNotFoundError:
    print("Error: One or more model files not found.")
    exit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        input_data = [float(request.form.get(feature)) for feature in [
            'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
            'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
        ]]

        # Scale the input
        input_data_scaled = scaler.transform([input_data])

        # Predict with both models
        dt_prediction = dt_model.predict(input_data_scaled)
        knn_prediction = knn_model.predict(input_data_scaled)

        # Compare average confidence/probability
        dt_prob = np.mean(dt_model.predict_proba(input_data_scaled)[:, 1])
        knn_prob = np.mean(knn_model.predict_proba(input_data_scaled)[:, 1])

        # Choose best model
        if dt_prob > knn_prob:
            prediction = dt_prediction[0]
            best_model = "Decision Tree"
        else:
            prediction = knn_prediction[0]
            best_model = "KNN"

        # Generate message
        if prediction == 1:
            prediction_text = (
                "<div class='result danger'>"
                "⚠️ <strong>Potential Risk of Heart Disease</strong><br>"
                "👉 Please consult a cardiologist and undergo further medical evaluation.<br>"
                "🩺 Early detection can save lives.<br>"
                f"<small><em>Prediction by {best_model} model</em></small>"
                "</div>"
            )
        else:
            prediction_text = (
                "<div class='result success'>"
                "✅ <strong>No Heart Disease Risk Detected</strong><br>"
                "🎉 Keep up with your healthy lifestyle: regular check-ups, exercise, and a balanced diet.<br>"
                f"<small><em>Prediction by {best_model} model</em></small>"
                "</div>"
            )

        return render_template('index.html', prediction_text=prediction_text)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved model and scaler
model = joblib.load('gradient_boosting_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('bmi_calculator.html')  # Serve the BMI calculator on the home page

@app.route('/bmi', methods=['POST'])
def bmi_calculator():
    weight = float(request.form['weight'])
    height = float(request.form['height']) / 100  # Convert height from cm to meters
    bmi = weight / (height ** 2)  # Calculate BMI
    return redirect(url_for('predict', bmi=bmi))  # Redirect to predict with BMI as a query parameter

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['age'])
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])  # Get the number of children
        smoker = request.form['smoker']  # 'yes' or 'no'

        # Convert smoker to appropriate numeric value
        smoker_code = 1 if smoker == 'yes' else 0

        # Calculate the age-bmi interaction
        age_bmi_interaction = age * bmi

        # Create features array for prediction
        features = np.array([[age, bmi, children, smoker_code, age_bmi_interaction]])  # 5 features
        features_scaled = scaler.transform(features)  # Apply scaling

        # Make prediction using the model
        predicted_charges = model.predict(features_scaled)[0]

        return render_template('predict.html', predicted_charges=predicted_charges, bmi=bmi)  # Show predicted charges

    # If GET, show the form without any prediction
    bmi = request.args.get('bmi', type=float)  # Get BMI from query parameters
    return render_template('predict.html', bmi=bmi)  # Pass BMI to the form

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Run the app on port 5001
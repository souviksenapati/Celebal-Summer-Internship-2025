import pandas as pd
import numpy as np
import joblib
import shap

from flask import Flask, render_template, request

app = Flask(__name__)

# Load model
model = joblib.load('model/student_score_lgbm_model.pkl')

# For SHAP explanations
explainer = shap.TreeExplainer(model)

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    # Get form values
    Gender = int(data['Gender'])
    Hours_Studied = float(data['Hours_Studied'])
    Previous_Score = float(data['Previous_Score'])
    Attendance = float(data['Attendance'])
    Internet = int(data['Internet'])
    Extra = float(data['Extra'])
    Sleep = float(data['Sleep'])
    Health = int(data['Health'])

    # Prepare data for model
    features = np.array([[Gender, Hours_Studied, Previous_Score, Attendance, Internet, Extra, Sleep, Health]])
    score_pred = model.predict(features)[0]

    # SHAP explanation
    shap_values = explainer.shap_values(pd.DataFrame(features, columns=[
        'Gender','Hours_Studied','Previous_Exam_Score','Attendance','Internet_Access','Extra_Curricular_Hours','Sleep_Hours','Health_Issues'
    ]))

    # Risk Flagging
    risk = "Needs Support" if score_pred < 60 else "Good Performance"

    return render_template("result.html", score=round(score_pred,2), risk=risk, shap_values=shap_values[0])

# Educator Dashboard — Show top features
@app.route('/risk')
def risk_students():
    # Future: show risk list — right now just template placeholder
    return render_template("risk.html")

if __name__ == "__main__":
    app.run(debug=True)

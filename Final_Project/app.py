# ============================
# Imports
# ============================
import pickle
import numpy as np
from flask import Flask, render_template, request
import shap

# ============================
# Flask App Initialization
# ============================
app = Flask(__name__)

# ============================
# Load Trained Model
# ============================
model = pickle.load(open("model/student_score_lgbm_model.pkl", "rb"))

# Initialize SHAP explainer
explainer = shap.TreeExplainer(model)

# ============================
# Routes
# ============================

# Landing Page Route
@app.route("/")
def landing():
    return render_template("index.html")

# Prediction Form Route
@app.route("/predictor")
def index():
    return render_template("predictor.html")

# Prediction Processing Route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect & validate data from form
        data = [
            float(request.form["Gender"]),
            float(request.form["Hours_Studied"]),
            float(request.form["Previous_Score"]),
            float(request.form["Attendance"]),
            float(request.form["Extra"]),
            float(request.form["Sleep"]),
            float(request.form["Health"]),
        ]

        # Convert to 2D array for model input
        data_array = np.array([data])

        # Make prediction
        prediction = model.predict(data_array)[0]

        # SHAP explanation
        shap_values = explainer.shap_values(data_array)
        feature_names = [
            'Gender', 'Hours Studied', 'Previous Exam Score', 'Attendance',
            'Extra Curricular Hours', 'Sleep Hours', 'Health Issues'
        ]

        explanation = list(zip(feature_names, shap_values[0]))
        explanation_sorted = sorted(explanation, key=lambda x: abs(x[1]), reverse=True)

        # Suggested actionable feedback for educator
        negative_impacts = [f for f in explanation if f[1] < 0]
        negative_impacts_sorted = sorted(negative_impacts, key=lambda x: x[1])
        top_issues = [f[0] for f in negative_impacts_sorted[:2]]
        suggested_action = ", ".join(top_issues) if top_issues else "No major concerns"

        # Risk categorization
        if prediction >= 85:
            status = "Excellent"
        elif prediction >= 60:
            status = "Good Performance"
        else:
            status = "Needs Attention"

        return render_template(
            "result.html", 
            prediction=round(prediction, 2), 
            status=status, 
            explanation=explanation_sorted,
            suggestion=suggested_action
        )

    except Exception as e:
        return str(e)

# ============================
# Main launcher
# ============================
if __name__ == "__main__":
    app.run(debug=True)

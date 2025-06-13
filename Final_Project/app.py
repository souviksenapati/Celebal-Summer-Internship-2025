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

# Home route (form)
@app.route("/")
def index():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect data from form
        data = [
            float(request.form["gender"]),
            float(request.form["hours_studied"]),
            float(request.form["previous_exam_score"]),
            float(request.form["attendance"]),
            float(request.form["internet_access"]),
            float(request.form["extra_curricular_hours"]),
            float(request.form["sleep_hours"]),
            float(request.form["health_issues"]),
        ]

        # Predict score
        prediction = model.predict([data])[0]

        # Convert to proper shape for SHAP
        input_array = np.array([data])

        # SHAP explanation
        shap_values = explainer.shap_values(input_array)
        feature_names = ['Gender', 'Hours Studied', 'Previous Exam Score', 'Attendance', 
                        'Internet Access', 'Extra Curricular Hours', 'Sleep Hours', 'Health Issues']

        explanation = list(zip(feature_names, shap_values[0]))
        explanation_sorted = sorted(explanation, key=lambda x: abs(x[1]), reverse=True)


        # Simple risk categorization
        if prediction >= 85:
            status = "Excellent"
        elif prediction >= 60:
            status = "Good Performance"
        else:
            status = "Needs Attention"

        return render_template("result.html", 
                                prediction=round(prediction, 2), 
                                status=status, 
                                explanation=explanation_sorted)
    
    except Exception as e:
        return str(e)

# ============================
# Main launcher
# ============================
if __name__ == "__main__":
    app.run(debug=True)

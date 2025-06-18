# ============================
# Imports
# ============================
import pickle
import numpy as np
import pandas as pd
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
explainer = shap.TreeExplainer(model)

# ============================
# Routes
# ============================

# Landing Page
@app.route("/")
def landing():
    return render_template("index.html")

# Form Page
@app.route("/predictor")
def index():
    return render_template("predictor.html")

# Prediction Logic
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

        feature_names = [
            'Gender', 'Hours Studied', 'Previous Exam Score', 'Attendance',
            'Extra Curricular Hours', 'Sleep Hours', 'Health Issues'
        ]

        data_array = np.array([data])
        df = pd.DataFrame(data_array, columns=feature_names)

        # Make prediction
        prediction = model.predict(df)[0]

        # Get SHAP values
        shap_values = explainer.shap_values(df)
        shap_val_row = shap_values[0] if len(shap_values.shape) == 2 else shap_values
        explanation = list(zip(feature_names, shap_val_row))
        explanation_sorted = sorted(explanation, key=lambda x: abs(x[1]), reverse=True)

        # Top 2 negative contributors
        negative_impacts = [f for f in explanation_sorted if f[1] < 0]
        top_issues = [f[0] for f in negative_impacts[:2]]

        # Status tag
        if prediction >= 90:
            status = "Outstanding"
        elif prediction >= 80:
            status = "Excellent"
        elif prediction >= 70:
            status = "Very Good"
        elif prediction >= 60:
            status = "Good"
        elif prediction >= 50:
            status = "Average"
        elif prediction >= 40:
            status = "Below Average"
        else:
            status = "Needs Serious Attention"

        # Suggestions (based on top_issues only)
        raw_suggestions = []

        if "Sleep Hours" in top_issues:
            sleep = data[5]
            if sleep > 8:
                raw_suggestions.append(f"reduce sleep by {round(sleep - 8, 1)} hr")
            elif sleep < 5:
                raw_suggestions.append(f"increase sleep by {round(6 - sleep, 1)} hr")

        if "Hours Studied" in top_issues:
            studied = data[1]
            if studied < 4:
                raw_suggestions.append(f"increase study time by {round(3 - studied, 1)} hr")
            elif studied > 10:
                raw_suggestions.append(f"reduce study time by {round(studied - 8, 1)} hr to avoid burnout")

        if "Extra Curricular Hours" in top_issues:
            extra = data[4]
            if extra > 4:
                raw_suggestions.append(f"reduce extra-curricular activities by {round(extra - 5, 1)} hr")

        if "Attendance" in top_issues:
            attendance = data[3]
            if attendance < 75:
                raw_suggestions.append(f"improve attendance by at least {round(75 - attendance, 1)}%")

        if "Previous Exam Score" in top_issues:
            prev = data[2]
            if prev < 50:
                raw_suggestions.append("focus on basic concepts to improve your score")

        if "Health Issues" in top_issues:
            health = data[6]
            if health == 1:
                raw_suggestions.append("focus on your health and manage study load accordingly")

        # Final suggestion formatting
        if raw_suggestions:
            if len(raw_suggestions) == 1:
                sentence = raw_suggestions[0]
            else:
                sentence = ", ".join(raw_suggestions[:-1]) + " and " + raw_suggestions[-1]
            suggestions = [sentence[0].upper() + sentence[1:] + "."]
        else:
            suggestions = ["You're doing great! Keep maintaining your current routine."]

        return render_template(
            "result.html",
            prediction=round(prediction, 2),
            status=status,
            explanation=explanation_sorted,
            feedback=", ".join(top_issues) if top_issues else "No major concerns",
            suggestions=suggestions
        )

    except Exception as e:
        return str(e)

# ============================
# Launch App
# ============================
if __name__ == "__main__":
    app.run(debug=True)

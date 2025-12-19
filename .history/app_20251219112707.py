from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("final_model.pkl", "rb"))

@app.route("/")
def home():
    return "Titanic Survival Prediction API is running successfully."

@app.route("/desktop")
def desktop():
    return "Welcome to the Titanic ML Flask App (Desktop Route)."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        features = np.array([[
            data["Age"],
            data["Sex"],
            data["Pclass"],
            data["Parch"],
            data["Fare"],
            data["SibSp"],
            data["Embarked"]
        ]])

        prediction = model.predict(features)[0]

        result = "Survived" if prediction == 1 else "Not Survived"

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

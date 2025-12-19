# Titanic Passenger Survival Prediction Project 🚢

This project is a **machine learning–based REST API** built using **Flask** that predicts whether a passenger survived the Titanic disaster based on passenger-related features. The prediction model is trained on the famous **Titanic dataset** and deployed as a Flask web service.

---

## 🔍 Project Overview

The Titanic dataset contains demographic and travel-related information of passengers aboard the Titanic. This project uses that dataset to build a **supervised classification model** that predicts passenger survival (`Survived` or `Not Survived`).

The trained model is integrated into a **Flask API**, allowing predictions through HTTP requests. This makes the project suitable for real-world ML deployment scenarios and API-based consumption.

---

## 📊 Dataset Description

The dataset includes the following important features:

* **Age** – Age of the passenger
* **Sex** – Gender of the passenger (encoded numerically)
* **Pclass** – Passenger class (1st, 2nd, or 3rd)
* **SibSp** – Number of siblings/spouses aboard
* **Parch** – Number of parents/children aboard
* **Fare** – Ticket fare paid by the passenger
* **Embarked** – Port of embarkation (encoded numerically)

**Target Variable:**

* `Survived` → 1 = Survived, 0 = Not Survived

---

## 🛠️ Technologies Used

* Python
* Flask
* NumPy
* Scikit-learn
* Pickle (for model serialization)

---

## 📁 Project Structure

```
Titanic-Passenger-Survival-Prediction-Project/
│── app.py
│── final_model.pkl
│── requirements.txt
│── README.md
```

---

## ⚙️ API Endpoints

### 1️⃣ Home Route

**GET /**

```
Titanic Survival Prediction API is running successfully.
```

---

### 2️⃣ Desktop Route

**GET /desktop**

```
Welcome to the Titanic ML Flask App (Desktop Route).
```

---

### 3️⃣ Prediction Route

**POST /predict**

This endpoint accepts passenger details in JSON format and returns the survival prediction.

#### 📥 Request Format (JSON)

```json
{
  "Age": 22,
  "Sex": 1,
  "Pclass": 3,
  "Parch": 0,
  "Fare": 7.25,
  "SibSp": 1,
  "Embarked": 0
}
```

> ⚠️ Note: Categorical values such as `Sex` and `Embarked` must be **numerically encoded** before sending the request.

#### 📤 Response Format

```json
{
  "prediction": "Survived"
}
```

or

```json
{
  "prediction": "Not Survived"
}
```

---

## 🚀 How to Run the Project Locally

### Step 1: Clone the Repository

```bash
git clone https://github.com/Anukul-Chandra/Titanic-Passenger-Survival-Prediction-Project.git
cd Titanic-Passenger-Survival-Prediction-Project
```

### Step 2: Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Flask App

```bash
python app.py
```

### Step 5: Test the API

Open browser or Postman and go to:

```
http://127.0.0.1:5000/
```

---

## 🧠 Model Description

A supervised machine learning classification model was trained using the Titanic dataset. The trained model is saved as `final_model.pkl` and loaded into the Flask application to perform real-time predictions.

---

## 📌 Use Cases

* Learning Flask-based ML deployment
* Understanding REST API creation for ML models
* Academic and university projects
* Beginner-friendly ML + backend integration

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Anukul Chandra**
GitHub: [https://github.com/Anukul-Chandra](https://github.com/Anukul-Chandra)

from flask import request,Flask,jsonify

app = Flask(__name__)


# Get request
@app.route("/")
def input():
    return "Hello Anukul , i am from Flask home function !You have successfully setup Flask."
@app.route("/desktop")
def input2():
    return "Hello Anukul , i am from Flask desktop function !You have successfully setup Flask."


# Post request
@app.route("/post", methods=["POST"])
def post():
    name  = request.form.get("name")
    age = request.form.get("age")

    return jsonify({'message' : f'Hello {name}, you are {str(age)} years old!'})


if __name__ == "__main__":
    app.run(debug=True)

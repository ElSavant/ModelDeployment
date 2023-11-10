from flask import (Flask, render_template,
                   request, jsonify)
from utils import make_prediction

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    email_text = request.form.get("email-content")
    prediction = make_prediction(email_text)
    return render_template("home.html", prediction=prediction,
                           text=email_text)


@app.route("/api/predict", methods=["POST"])
def predict_api():
    data = request.get_json(force=True)
    email_text = data["email-content"]
    prediction = make_prediction(email_text)
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

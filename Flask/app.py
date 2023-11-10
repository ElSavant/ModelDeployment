from flask import Flask, render_template, request
import pickle

tokenizer = pickle.load(open("models/cv.pkl", "rb"))
model = pickle.load(open("models/clf.pkl", "rb"))

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    email_text = request.form.get("email-content")
    tokenize_email = tokenizer.transform([email_text])
    prediction = model.predict(tokenize_email)
    prediction = "spam" if prediction == 1 else "not spam"
    return render_template("home.html", prediction=prediction,
                           text=email_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

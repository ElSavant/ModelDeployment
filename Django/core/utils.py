import pickle

tokenizer = pickle.load(open("models/cv.pkl", "rb"))
model = pickle.load(open("models/clf.pkl", "rb"))


def make_prediction(text):
    tokenize_text = tokenizer.transform([text])
    prediction = model.predict(tokenize_text)
    prediction = "spam" if prediction == 1 else "not spam"
    return prediction

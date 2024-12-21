from flask import Flask, render_template, request, jsonify
import json
from difflib import get_close_matches

# Load data
data = json.load(open("data.json"))

app = Flask(__name__)

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return {"suggestion": get_close_matches(w, data.keys())[0]}
    else:
        return "The word doesn't exist. Please double-check it."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-meaning", methods=["POST"])
def get_meaning():
    word = request.form["word"]
    output = translate(word)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)

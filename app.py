from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)
data = pd.read_csv("data/biotech_terms.csv")

def preprocess(text):
    return text.lower().strip()

@app.route("/", methods=["GET", "POST"])
def search():
    results = None
    if request.method == "POST":
        keyword = preprocess(request.form["keyword"])
        results = data[data["term_name"].str.lower().str.contains(keyword)]
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run()
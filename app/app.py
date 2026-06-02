from flask import Flask, render_template, request

app = Flask(__name__)

votes = {
    "Terraform": 0,
    "Docker": 0
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        choice = request.form.get("vote")
        votes[choice] += 1

    return render_template("index.html", votes=votes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
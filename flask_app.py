from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def accueil():
    return render_template("accueil.html")


@app.get("/presentation")
def presentation():
    return render_template("presentation.html")


@app.get("/loisir")
def loisir():
    return "Je vais au Bar"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

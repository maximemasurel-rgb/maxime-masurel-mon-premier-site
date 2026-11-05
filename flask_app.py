from flask import Flask

app = Flask(__name__)
@app.get("/")
def accueil():
    return "C'est moi Maxime"
@app.get("/presentation")
def presentation():
    return """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Présentation</title>
</head>
<body>
    <h1>Maxime Masurel</h1>
    <p>Je suis étudiant en <strong>deuxième année à l'ICAM</strong>.</p>

    <h2>Ce que j'aime</h2>
    <ul>
        <li>Les voitures</li>
        <li>La voile</li>
        <li>Le code (bientôt !)</li>
    </ul>

    <img src="https://snbsm.com/wp-content/uploads/2017/12/Rhum-Logo-Rond400.png" width="100">
</body>
</html>
"""


@app.get("/loisir")
def loisir():
    return "Je vais au Bar"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

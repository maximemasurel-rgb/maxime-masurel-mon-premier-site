# ---------------------------------------------------------------
#  Mon premier site Web avec Flask
# ---------------------------------------------------------------
#  Ce fichier est le "cerveau" de votre site : c'est lui qui
#  reçoit les demandes des navigateurs et qui fabrique les réponses.
#
#  Vous allez le compléter petit à petit, exercice après exercice.
#  Les consignes sont dans le dossier "exercices/".
# ---------------------------------------------------------------

from flask import Flask

app = Flask(__name__)


# Une "route" associe une adresse (URL) à une fonction Python.
# Ici : quand quelqu'un visite la page d'accueil "/",
# Flask exécute la fonction accueil() et renvoie son résultat au navigateur.
@app.get("/")
def accueil():
    return "C'est moi Maxime"


# ---------------------------------------------------------------
#  Ajoutez vos nouvelles routes ci-dessous 👇
# ---------------------------------------------------------------
@app.get("/presentation")
def presentation():
    return """
    <h1>MAXIME MASUREL</h1>
    <head>
    <meta charset="utf-8">
    <title>Présentation</title>
</head>
<body>
    <h1>{{ Maxime }} {{ Masurel }}</h1>
    <p>Je suis étudiant en <strong>deuxieme année a l'ICAM</strong</strong>.</p>
</body>
    
    <h2>Ce que j'aime</h2>
    <ul>
        <li>Les voiture</li>
        <li>La voile ]</li>
        <li>Le code (bientôt !)</li>
    <img src="https://snbsm.com/wp-content/uploads/2017/12/Rhum-Logo-Rond400.png" width="100">
    """ 
    </ul>
    """

@app.get("/loisir")
def loisir():
    return "Je vais au Bar"


# ---------------------------------------------------------------
#  Ne pas modifier : utile seulement pour lancer le site
#  sur votre propre ordinateur (python flask_app.py)
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

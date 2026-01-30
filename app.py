from flask import Flask, render_template, request

app = Flask(__name__)

# Algorithme de décision (Logique "Smart-Decision")
def evaluer_statut(moyenne, presence, heures):
    # Score basé sur une pondération académique
    # On considère que la moyenne compte pour 50%, la présence 30% et l'étude 20%
    score = (moyenne * 5) + (presence * 0.3) + (heures * 2)
    
    if moyenne < 10 or presence < 50:
        return {"code": 2, "label": "Risque Élevé", "color": "#e74c3c"}
    elif score < 65:
        return {"code": 1, "label": "Risque Modéré", "color": "#f39c12"}
    else:
        return {"code": 0, "label": "Situation Normale", "color": "#27ae60"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Récupération des données
    nom = request.form.get("nom")
    filiere = request.form.get("filiere")
    niveau = request.form.get("niveau")
    moyenne = float(request.form.get("note_moyenne"))
    presence = float(request.form.get("taux_presence"))
    heures = float(request.form.get("heures_etude"))

    # Calcul du risque
    resultat = evaluer_statut(moyenne, presence, heures)

    return render_template('dashboard.html', 
                           nom=nom, filiere=filiere, niveau=niveau,
                           moyenne=moyenne, presence=presence, 
                           heures=heures, resultat=resultat)

if __name__ == '__main__':
    app.run(debug=True)
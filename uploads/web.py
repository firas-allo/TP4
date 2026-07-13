from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/reconnaissance', methods=['GET', 'POST'])
def reconnaissance():
    prediction = None

    if request.method == 'POST':
        file = request.files['file']
        if file:
            # ⚠️ ici tu mets ton modèle IA
            prediction = "Dauphin"  # exemple

    return render_template('reconnaissance.html', prediction=prediction)

@app.route('/informations')
def informations():
    return render_template('informations.html')

if __name__ == "__main__":
    app.run(debug=True)
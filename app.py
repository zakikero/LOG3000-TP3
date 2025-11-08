"""
Module principal de l'application Flask Calculator

Cette application web fournit une calculatrice simple qui permet d'évaluer
des expressions arithmétiques avec un seul opérateur (+, -, *, /).

Routes:
    / (GET, POST) - Affiche le formulaire de la calculatrice et traite les calculs

Fonctionnalités:
    - Interface web avec boutons cliquables pour saisir les expressions
    - Traitement côté serveur des calculs via Flask
    - Validation des expressions et gestion des erreurs
    - Support des quatre opérations de base (voir operators.py)
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Dictionnaire mappant les symboles d'opérateurs aux fonctions correspondantes
# Permet de résoudre dynamiquement l'opération à effectuer
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Évalue une expression arithmétique simple avec un seul opérateur.
    
    Parse et calcule une expression de la forme "nombre opérateur nombre"
    où l'opérateur peut être +, -, *, ou /.
    
    Entrées:
        expr (str): L'expression arithmétique à évaluer (ex: "10+5", "20*3")
    
    Sorties:
        float: Le résultat du calcul
    
    Lève:
        ValueError: Si l'expression est vide, contient plus d'un opérateur,
                   a un format invalide, ou contient des opérandes non numériques
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de la calculatrice Flask.
    
    Gère les requêtes GET (affichage initial) et POST (calcul d'expressions).
    En GET, affiche un formulaire vide. En POST, récupère l'expression
    depuis le champ 'display', la calcule et affiche le résultat.
    
    Sorties:
        str: Le HTML rendu du template index.html avec le résultat du calcul
             (chaîne vide en GET, résultat ou message d'erreur en POST)
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
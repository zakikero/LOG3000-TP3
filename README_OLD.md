# LOG3000-TP3

## Nom du projet

Calculatrice Web Flask

## Numéro d'équipe

Équipe 07

## Objectif

Ce projet est une calculatrice web simple construite avec la bibliothèque Flask de Python. L'objectif est de fournir une interface utilisateur intuitive permettant d'effectuer des calculs mathématiques de base via un navigateur web.

## Composantes du projet

### Frontend

- **index.html** : Fichier HTML qui fournit l'interface utilisateur de la calculatrice
- **style.css** : Fichier CSS qui gère le style et l'apparence de l'interface

### Backend

- **app.py** : Fichier Python principal qui exécute le serveur Flask
- **operators.py** : Fichier Python qui gère la logique des opérations mathématiques

## Structure du projet

```
LOG3000-TP3/
├── app.py                    # Application Flask principale (routes et logique serveur)
├── operators.py              # Fonctions d'opérations arithmétiques
├── README.md                 # Ce fichier - Documentation générale du projet
├── static/                   # Fichiers statiques (CSS, JS, images)
│   ├── style.css            # Feuille de style de la calculatrice
│   └── README.md            # Documentation du module static
└── templates/                # Templates HTML Jinja2
    ├── index.html           # Interface principale de la calculatrice
    └── README.md            # Documentation du module templates
```

### Documentation des modules

Chaque répertoire contient sa propre documentation détaillée :

- **[static/README.md](static/README.md)** : Documentation des fichiers statiques (CSS, assets)
  - Raison d'être du module
  - Description de `style.css` et son architecture
  - Dépendances et hypothèses
  - Notes pour les développeurs

- **[templates/README.md](templates/README.md)** : Documentation des templates HTML
  - Raison d'être du module
  - Structure de `index.html` et variables Jinja2
  - Architecture du flux de données
  - Syntaxe Jinja2 et bonnes pratiques

Ces documentations permettent à un nouveau développeur de :
- Comprendre rapidement la structure du projet
- Naviguer efficacement dans le code
- Connaître les dépendances et hypothèses de chaque module
- Suivre les bonnes pratiques établies

## Architecture de l'application

### Flux de données

1. **Requête GET initiale** : L'utilisateur accède à `/`
   - Flask rend `templates/index.html` avec `result=""`
   - Le navigateur charge `static/style.css`

2. **Interaction utilisateur** : Clics sur les boutons (JavaScript côté client)
   - `appendToDisplay()` ajoute des caractères au champ
   - `clearDisplay()` efface le champ

3. **Soumission du formulaire** : L'utilisateur clique sur "="
   - POST vers `/` avec `display="expression"`
   - Flask reçoit les données via `request.form.get('display')`

4. **Traitement serveur** :
   - `calculate(expression)` parse et valide l'expression
   - Appelle la fonction appropriée depuis `operators.py`
   - Gère les erreurs (expression invalide, division par zéro, etc.)

5. **Réponse** :
   - Flask rend `index.html` avec `result=résultat_calculé`
   - Le navigateur affiche le résultat dans le champ

### Fichiers Python

#### `app.py`
**Responsabilités :**
- Initialisation de l'application Flask
- Définition de la route `/` (GET et POST)
- Parsing des expressions arithmétiques (fonction `calculate()`)
- Validation et gestion des erreurs
- Rendu des templates avec résultats

**Fonctions principales :**
- `calculate(expr: str) -> float` : Parse et évalue une expression simple
- `index()` : Route principale de l'application

#### `operators.py`
**Responsabilités :**
- Implémentation des opérations arithmétiques de base

**Fonctions :**
- `add(a, b)` : Addition (a + b)
- `subtract(a, b)` : Soustraction (b - a)
- `multiply(a, b)` : Puissance (a ** b)
- `divide(a, b)` : Division entière (a // b)

**Note importante :** Les noms des fonctions ne correspondent pas exactement aux opérations mathématiques standards (ceci est intentionnel pour le projet).

## Prérequis d'installation

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

## Instructions d'installation

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/zakikero/LOG3000-TP3.git
   cd LOG3000-TP3
   ```

2. Installer Flask :

   ```bash
   pip install flask
   ```

3. Lancer l'application :

   ```bash
   python app.py
   ```

4. Ouvrir votre navigateur et accéder à :
   ```
   http://localhost:5000
   ```

## Fonctionnalités

- ✅ Interface graphique intuitive avec grille de boutons
- ✅ Calculs arithmétiques de base (+, -, *, /)
- ✅ Validation des expressions côté serveur
- ✅ Gestion des erreurs avec messages conviviaux
- ✅ Design responsive et moderne
- ✅ Support d'un seul opérateur par expression

## Limitations actuelles

- Supporte uniquement les expressions avec **un seul opérateur**
- Pas de support pour les parenthèses ou expressions complexes
- Pas de gestion de l'historique des calculs
- Mode debug activé (à désactiver en production)

## Pour les développeurs

### Code documenté

Tous les fichiers Python contiennent :
- **Docstrings de module** : Explication du rôle et des fonctionnalités
- **Docstrings de fonctions** : Arguments, valeurs de retour, exceptions
- **Commentaires en ligne** : Explications de la logique complexe

### Tests

Pour tester l'application manuellement :
1. Expressions valides : `5+3`, `10-2`, `2*3`, `8/2`
2. Expressions invalides : `5++3`, `abc`, `5/0`, ` `
3. Vérifier les messages d'erreur appropriés

### Contribution

Pour contribuire au projet :
1. Consulter les README.md des modules concernés
2. Suivre les conventions de documentation (docstrings en français)
3. Ajouter des commentaires expliquant le "pourquoi", pas le "quoi"
4. Tester localement avant de committer

### Déploiement en production

⚠️ **Attention :** Ne pas utiliser le serveur de développement Flask en production

Recommandations :
1. Désactiver `debug=True` dans `app.py`
2. Utiliser un serveur WSGI (Gunicorn, uWSGI, Waitress)
3. Servir les fichiers statiques via nginx/Apache
4. Implémenter CSRF protection (Flask-WTF)
5. Configurer HTTPS

Exemple avec Gunicorn :
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Licence

Ce projet est développé dans le cadre du cours LOG3000.

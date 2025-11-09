# Flask Calculator - Calculatrice Web

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![License](https://img.shields.io/badge/License-LOG3000-orange)

> **Équipe 07** | Projet LOG3000-TP3 | Documentation complète

---

## Table des matières

- [À propos du projet](#à-propos-du-projet)
- [Fonctionnalités](#fonctionnalités)
- [Architecture](#architecture)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Tests](#tests)
- [Contribution](#contribution)
- [Documentation des modules](#documentation-des-modules)

---

## À propos du projet

### Description

Flask Calculator est une application web de calculatrice arithmétique développée avec le framework Python Flask. Le projet démontre les concepts fondamentaux du développement web moderne en séparant clairement les responsabilités entre le frontend (HTML/CSS/JavaScript) et le backend (Python/Flask).

### But et portée

**Objectifs pédagogiques :**

- Maîtriser les bases du framework Flask (routes, templates Jinja2, gestion des formulaires)
- Comprendre l'architecture client-serveur et le cycle requête/réponse HTTP
- Implémenter une validation robuste des entrées utilisateur côté serveur
- Appliquer les bonnes pratiques de documentation et de structure de code

**Portée fonctionnelle :**

- Calculatrice web accessible via navigateur
- Support des quatre opérations arithmétiques de base (+, -, \*, /)
- Interface utilisateur intuitive avec grille de boutons cliquables
- Validation et traitement des expressions côté serveur
- Gestion d'erreurs avec messages conviviaux

**Limitations intentionnelles :**

- Support d'un seul opérateur par expression (pas d'expressions composées)
- Pas de gestion de priorité d'opérateurs ou de parenthèses
- Pas d'historique des calculs
- Mode développement uniquement (nécessite adaptation pour production)

### Contexte académique

Projet réalisé dans le cadre du cours **LOG3000** par l'**Équipe 07**.

---

## Fonctionnalités

### Opérations supportées

| Opération                  | Symbole | Exemple | Résultat   |
| -------------------------- | ------- | ------- | ---------- |
| Addition                   | `+`     | `5+3`   | `8`        |
| Soustraction               | `-`     | `10-4`  | `6`        |
| Multiplication (Puissance) | `*`     | `2*3`   | `8` (2³)   |
| Division (Entière)         | `/`     | `10/3`  | `3` (10÷3) |

⚠️ **Note importante :** Les opérations `*` et `/` implémentent respectivement la puissance (`**`) et la division entière (`//`) en Python. Ceci est intentionnel pour le projet.

### Fonctionnalités techniques

- **Interface responsive** : Design moderne adaptatif
- **Validation robuste** : Vérification côté serveur de toutes les entrées
- **Gestion d'erreurs** : Messages d'erreur explicites pour les expressions invalides
- **Code documenté** : Docstrings complètes et commentaires en français
- **Architecture modulaire** : Séparation claire entre logique métier et présentation
- **Templates Jinja2** : Rendu dynamique des résultats

---

## Architecture

### Structure du projet

```
LOG3000-TP3/
├── app.py                    # Application Flask principale
├── operators.py              # Fonctions d'opérations arithmétiques
├── README.md                 # Ce fichier - Documentation générale
├── static/                   # Fichiers statiques (CSS, JS, images)
│   ├── style.css            # Feuille de style principale
│   └── README.md            # Documentation du module static
└── templates/                # Templates HTML Jinja2
    ├── index.html           # Interface utilisateur principale
    └── README.md            # Documentation du module templates
```

### Composants principaux

#### Backend (Python/Flask)

**`app.py`** - Application Flask principale

- Initialisation de l'application Flask
- Route `/` (GET et POST) pour l'interface calculatrice
- Fonction `calculate(expr)` : parsing et validation des expressions
- Gestion des erreurs et rendu des templates

**`operators.py`** - Logique arithmétique

- `add(a, b)` : Addition (a + b)
- `subtract(a, b)` : Soustraction (b - a)
- `multiply(a, b)` : Puissance (a \*\* b)
- `divide(a, b)` : Division entière (a // b)

#### Frontend (HTML/CSS/JavaScript)

**`templates/index.html`** - Interface utilisateur

- Formulaire HTML avec champ d'affichage
- Grille de boutons 4x4 (chiffres 0-9 et opérateurs)
- JavaScript pour interaction côté client
- Variables Jinja2 pour injection de données serveur

**`static/style.css`** - Présentation visuelle

- Design moderne avec thème sombre
- CSS Grid pour disposition des boutons
- Effets de survol et transitions
- Responsive design

### Flux de données

```
┌─────────────────────────────────────────────────────────────┐
│  1. GET /                                                   │
│     → Flask rend index.html avec result=""                  │
│     → Navigateur affiche le formulaire vide                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  2. Interaction utilisateur (JavaScript côté client)        │
│     → Clics sur boutons ajoutent des caractères             │
│     → appendToDisplay('5'), appendToDisplay('+'), etc.      │
│     → Champ display : "5+3"                                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  3. Soumission formulaire (clic sur "=")                    │
│     → POST / avec form data: display="5+3"                  │
│     → Flask reçoit request.form.get('display')              │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  4. Traitement serveur                                      │
│     → calculate("5+3")                                      │
│     → Parse : left="5", operator="+", right="3"             │
│     → Validation : conversions en float                     │
│     → Appel : OPS['+'](5, 3) = add(5, 3) = 8                │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  5. Réponse                                                 │
│     → render_template('index.html', result=8)               │
│     → HTML généré avec <input value="8" ...>                │
│     → Navigateur affiche le résultat                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Installation

### Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Python 3.7 ou supérieur** ([Télécharger Python](https://www.python.org/downloads/))
- **pip** (gestionnaire de paquets Python, inclus avec Python)
- **Git** (pour cloner le dépôt)

Vérifiez vos installations :

```bash
python --version    # Doit afficher Python 3.7+
pip --version       # Doit afficher pip 20.0+
git --version       # Doit afficher git 2.0+
```

### Guide d'installation étape par étape

#### 1. Cloner le dépôt

Ouvrez votre terminal et exécutez :

```bash
git clone https://github.com/zakikero/LOG3000-TP3.git
cd LOG3000-TP3
```

#### 2. Installer les dépendances

```bash
pip install flask
```

Pour une installation avec versions spécifiques (recommandé) :

```bash
pip install flask>=2.0.0
```

#### 3. Vérifier l'installation

Vérifiez que Flask est correctement installé :

```bash
python -c "import flask; print(flask.__version__)"
```

Devrait afficher la version de Flask (ex: `2.3.0` ou supérieur).

#### 4. Lancer l'application

```bash
python app.py
```

Vous devriez voir :

```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

#### 6. Accéder à l'application

Ouvrez votre navigateur et accédez à :

```
http://localhost:5000
```

ou

```
http://127.0.0.1:5000
```

Vous devriez voir l'interface de la calculatrice !

### Résolution de problèmes d'installation

#### Erreur : "Flask n'est pas installé"

```bash
pip install --upgrade pip
pip install flask
```

#### Erreur : "Port 5000 déjà utilisé"

Modifiez `app.py` ligne 115 :

```python
app.run(debug=True, port=8000)  # Utilise le port 8000 à la place
```

#### Erreur : "Permission denied" (macOS/Linux)

Utilisez `python3` au lieu de `python` :

```bash
python3 app.py
```

---

## Utilisation

### Lancer l'application

1. **Démarrer le serveur Flask** :

   ```bash
   python app.py
   ```

2. **Ouvrir dans le navigateur** :
   - Automatique : Cliquez sur le lien dans le terminal
   - Manuel : Naviguez vers `http://localhost:5000`

### Utiliser la calculatrice

#### Effectuer un calcul simple

1. **Saisir l'expression** en cliquant sur les boutons :

   - Exemple : Cliquez sur `5`, `+`, `3`
   - Le champ d'affichage montre : `5+3`

2. **Calculer le résultat** :

   - Cliquez sur le bouton `=`
   - Le serveur traite l'expression
   - Le résultat s'affiche : `8`

3. **Effacer** :
   - Cliquez sur le bouton `C` pour vider le champ

#### Exemples d'utilisation

**Addition :**

```
Input:  12+5
Output: 17
```

**Soustraction :**

```
Input:  20-8
Output: 12
```

**Multiplication (Puissance) :**

```
Input:  2*3
Output: 8        (car 2³ = 8)
```

**Division (Entière) :**

```
Input:  15/4
Output: 3        (car 15÷4 = 3 en division entière)
```

#### Gestion des erreurs

L'application affiche des messages d'erreur pour les cas invalides :

**Expression vide :**

```
Input:  [vide]
Output: Error: empty expression
```

**Plusieurs opérateurs :**

```
Input:  5+3-2
Output: Error: only one operator is allowed
```

**Opérandes non numériques :**

```
Input:  abc+5
Output: Error: operands must be numbers
```

**Opérateur manquant ou mal placé :**

```
Input:  +5
Output: Error: invalid expression format
```

**Division par zéro :**

```
Input:  5/0
Output: Error: integer division or modulo by zero
```

### Arrêter l'application

Dans le terminal où l'application tourne :

- Appuyez sur `Ctrl+C` (Windows/macOS/Linux)
- Le serveur s'arrête proprement

### Désactiver l'environnement virtuel

Après avoir arrêté l'application :

```bash
deactivate
```

---

## Tests

Le projet dispose d'une suite complète de tests automatisés utilisant pytest.

### Tests automatisés

#### Installation

Pour exécuter les tests, installez d'abord pytest :

```bash
pip install pytest pytest-cov
```

#### Exécution des tests

> **Note :** Utilisez `python -m pytest` pour exécuter les tests sans environnement virtuel.

**Exécuter tous les tests :**

```bash
python -m pytest tests/ -v
```

**Exécuter un fichier de test spécifique :**

```bash
python -m pytest tests/test_operators.py -v
python -m pytest tests/test_calculate.py -v
python -m pytest tests/test_routes.py -v
```

**Avec rapport de couverture :**

```bash
python -m pytest tests/ --cov=. --cov-report=html
```

#### Statistiques des tests

- **Total de tests :** 23 tests
- **Test operators :** 6 tests (opérations arithmétiques + bug division)
- **Test calculate :** 9 tests (parsing d'expressions)
- **Test routes :** 8 tests (intégration Flask + bug UI)

#### Documentation des tests

Pour plus de détails sur les tests, consultez :

- **[tests/README.md](tests/README.md)** - Guide complet des tests

#### Résultats des tests

- **Tests réussis :** 23/23 (100%)

**Bugs identifiés :**

1. ~~**Bug #1** : Soustraction - ordre des opérandes inversé (`b-a` au lieu de `a-b`)~~ **[RÉSOLU]** - Corrigé dans la branche `fix/ordre-substract`
2. ~~**Bug #2** : Nombres négatifs non supportés (le parser interprétait `-` comme un second opérateur)~~ **[RÉSOLU]** – Corrigé dans la branche `bugfix/4-negative-numbers`
3. **Bug #3** : Division entière au lieu de décimale (`//` au lieu de `/`)~~ **[RÉSOLU]** - Corrigé dans la branche ` fix/division-decimal`
4. ~~**Bug #4** : Bugs d'affichage UI (boutons "02", "88", "\*" et "/" vides)~~ **[RÉSOLU]** - Corrigé dans la branche `fix/affichage-calculatrice`

### Tests manuels

Vous pouvez également tester manuellement l'application. Voici le protocole de test :

#### Scénarios de test

**Test 1 : Addition basique**

- Input : `5+3`
- Résultat attendu : `8`
- Statut : Pass / Fail

**Test 2 : Soustraction**

- Input : `10-4`
- Résultat attendu : `6`
- Statut : Pass / Fail

**Test 3 : Puissance (via \*)**

- Input : `2*3`
- Résultat attendu : `8` (2³)
- Statut : Pass / Fail

**Test 4 : Division entière (via /)**

- Input : `10/3`
- Résultat attendu : `3`
- Statut : Pass / Fail

**Test 5 : Gestion d'erreur - Expression vide**

- Input : `[soumettre sans rien saisir]`
- Résultat attendu : `Error: empty expression`
- Statut : Pass / Fail

**Test 6 : Gestion d'erreur - Plusieurs opérateurs**

- Input : `5+3-2`
- Résultat attendu : `Error: only one operator is allowed`
- Statut : Pass / Fail

**Test 7 : Gestion d'erreur - Caractères non numériques**

- Input : `abc+5`
- Résultat attendu : `Error: operands must be numbers`
- Statut : Pass / Fail

**Test 8 : Gestion d'erreur - Division par zéro**

- Input : `5/0`
- Résultat attendu : `Error: ...`
- Statut : Pass / Fail

---

## Contribution

### Flux de travail Git

Le projet utilise un workflow basé sur les branches et les pull requests (PR) pour faciliter la collaboration.

#### Structure des branches

```
main (ou master)           # Branche principale - code stable et testé
  ├── Documentation        # Branche actuelle - ajout de documentation
  ├── feature/nom          # Nouvelles fonctionnalités
  ├── bugfix/nom           # Corrections de bugs
  └── hotfix/nom           # Correctifs urgents
```

#### Convention de nommage des branches

Utilisez des noms descriptifs pour vos branches :

- **Features** : `feature/nom-descriptif`
  - Exemple : `feature/historique-calculs`, `feature/support-parentheses`
- **Bugfix** : `bugfix/description-bug`
  - Exemple : `bugfix/division-par-zero`, `bugfix/validation-expression`
- **Hotfix** : `hotfix/probleme-urgent`
  - Exemple : `hotfix/securite-injection`, `hotfix/crash-serveur`

#### Processus de contribution

1. **Créer une branche** depuis `main` :

   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/ma-fonctionnalite
   ```

2. **Développer et committer** :

   ```bash
   # Faire vos modifications
   git add .
   git commit -m "feat: description de la fonctionnalité"
   ```

   **Convention de messages de commit :**

   - `feat:` Nouvelle fonctionnalité
   - `fix:` Correction de bug
   - `docs:` Documentation uniquement
   - `refactor:` Refactoring de code
   - `test:` Ajout ou modification de tests

3. **Pousser la branche** :

   ```bash
   git push origin feature/ma-fonctionnalite
   ```

4. **Créer une Pull Request (PR)** :

   - Allez sur GitHub : https://github.com/zakikero/LOG3000-TP3
   - Cliquez sur "Pull requests" → "New pull request"
   - Sélectionnez votre branche comme source et `main` comme cible
   - Remplissez la description de la PR :

     ```markdown
     ## Description

     [Décrivez les changements apportés]

     ## Tests effectués

     - [ ] Tests manuels passés
     - [ ] Tests automatisés passés (si applicable)

     ## Type de changement

     - [ ] Nouvelle fonctionnalité
     - [ ] Correction de bug
     - [ ] Documentation
     - [ ] Refactoring
     ```

5. **Code Review** :
   - Un membre de l'équipe reverra votre code
   - Apportez les modifications demandées si nécessaire
   - Une fois approuvée, la PR sera mergée dans `main`

#### Gestion des Issues

Pour signaler un bug ou proposer une fonctionnalité :

1. **Créer une issue** sur GitHub
2. **Utiliser les labels appropriés** :

   - `bug` : Quelque chose ne fonctionne pas
   - `enhancement` : Nouvelle fonctionnalité ou amélioration
   - `documentation` : Documentation manquante ou incorrecte
   - `question` : Question ou besoin de clarification

3. **Décrire clairement** :
   - Pour un bug : étapes de reproduction, comportement attendu vs actuel
   - Pour une fonctionnalité : cas d'usage, bénéfices attendus

#### Bonnes pratiques

- Tester localement avant de pousser
- Écrire des messages de commit clairs et descriptifs
- Ajouter des docstrings et commentaires en français
- Suivre les conventions de code du projet (PEP 8)
- Mettre à jour la documentation si nécessaire
- Garder les PR focalisées (une fonctionnalité/fix par PR)

---

## Documentation des modules

Chaque module du projet possède sa propre documentation détaillée :

### [static/README.md](static/README.md)

**Fichiers statiques (CSS, JavaScript, assets)**

- Raison d'être du module
- Description de `style.css` et son architecture
- Dépendances et hypothèses
- Notes pour les développeurs
- Guide de style CSS

### [templates/README.md](templates/README.md)

**Templates HTML Jinja2**

- Raison d'être du module
- Structure détaillée de `index.html`
- Variables Jinja2 utilisées
- Architecture du flux de données
- Syntaxe Jinja2 et bonnes pratiques
- Considérations de sécurité

Ces documentations vous permettent de :

- Comprendre rapidement la structure du projet
- Naviguer efficacement dans le code
- Connaître les dépendances de chaque module
- Suivre les bonnes pratiques établies
- Contribuer sans friction

---

<div align="center">

**Fait par l'Équipe 07**

</div>

# Module templates/

## Raison d'être

Ce module contient tous les templates HTML de l'application Flask Calculator. Les templates utilisent le moteur de rendu Jinja2 intégré à Flask pour générer dynamiquement le HTML envoyé au navigateur.

Les templates permettent de :

- Séparer la présentation (HTML) de la logique métier (Python)
- Injecter des données dynamiques depuis le serveur Flask
- Réutiliser des composants HTML via l'héritage de templates
- Générer du HTML sécurisé avec auto-escaping

## Fichiers contenus

### `index.html`

**Responsabilité :** Template principal de l'interface calculatrice

**Structure :**

- **En-tête HTML :**

  - Meta charset UTF-8
  - Viewport pour le responsive design
  - Lien vers `style.css` via `{{ url_for('static', filename='style.css') }}`

- **Formulaire POST :**

  - Champ `display` (name="display") pour afficher l'expression et le résultat
  - Attribut `value="{{ result }}"` injecte la valeur retournée par Flask
  - Pas d'attribut `action` → soumission vers la même route `/`

- **Grille de boutons (4x4) :**

  - Boutons numériques : 0-9
  - Boutons opérateurs : +, -, \*, /
  - Bouton Clear (C) : efface l'affichage
  - Bouton Submit (=) : envoie le formulaire au serveur

- **JavaScript intégré :**
  - `appendToDisplay(value)` : ajoute un caractère au champ
  - `clearDisplay()` : vide le champ d'affichage

**Variables Jinja2 utilisées :**

- `{{ result }}` : Résultat du calcul ou message d'erreur (passé depuis `app.py`)
- `{{ url_for('static', filename='style.css') }}` : URL générée automatiquement pour les fichiers statiques

## Dépendances

### Techniques

- **Jinja2 :** Moteur de template fourni par Flask
- **Flask :** Fonction `render_template()` dans `app.py`
- **CSS :** Dépend de `static/style.css` pour le style visuel

### Données serveur

- **Variable `result` :** Doit être fournie par la route Flask (chaîne vide par défaut)
  ```python
  return render_template('index.html', result=result)
  ```

## Hypothèses

1. **Configuration Flask :**

   - Le répertoire `templates/` est configuré par défaut comme dossier de templates
   - Flask est instancié avec `app = Flask(__name__)`

2. **Route associée :**

   - La route `/` existe dans `app.py`
   - Elle accepte les méthodes GET et POST
   - En GET : `result=""` (affichage initial vide)
   - En POST : `result` contient le résultat du calcul ou un message d'erreur

3. **Navigation :**
   - Le formulaire se soumet à lui-même (même URL)
   - Le cycle complet : saisie → POST → calcul serveur → re-rendu avec résultat

## Architecture de flux

```
┌─────────────────────────────────────────────────────────────┐
│  1. GET /          → render_template('index.html', result='')│
│                      Affichage initial (champ vide)          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  2. User clicks buttons  → JavaScript modifie display.value  │
│     (ex: "12+5")                                             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  3. User clicks "="  → POST / avec display="12+5"            │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  4. Flask calcule    → calculate("12+5") = 17                │
│     render_template('index.html', result=17)                 │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  5. Template rendu   → <input value="17" ...>                │
│     Navigateur affiche le résultat                           │
└─────────────────────────────────────────────────────────────┘
```

## Utilisation

### Ajouter un nouveau template

1. Créer un fichier `.html` dans ce répertoire
2. Utiliser la syntaxe Jinja2 pour les parties dynamiques
3. Rendre le template depuis `app.py` :

   ```python
   from flask import render_template

   @app.route('/nouvelle-page')
   def nouvelle_page():
       return render_template('nouveau_template.html', data=data)
   ```

### Syntaxe Jinja2 courante

- **Variables :** `{{ variable }}`
- **Conditions :** `{% if condition %}...{% endif %}`
- **Boucles :** `{% for item in items %}...{% endfor %}`
- **Héritage :** `{% extends "base.html" %}` et `{% block content %}...{% endblock %}`
- **Filtres :** `{{ variable|upper }}`, `{{ variable|default('valeur') }}`

## Notes pour les développeurs

### Sécurité

- **Auto-escaping activé par défaut :** Les variables Jinja2 sont automatiquement échappées pour prévenir les injections XSS
- **N'utilisez JAMAIS `|safe` sur des données utilisateur non validées**

### Bonnes pratiques

1. **Validation côté serveur :** Ne jamais faire confiance aux données du formulaire
2. **CSRF Protection :** Pour une application en production, utiliser Flask-WTF pour protéger les formulaires
3. **Séparation des responsabilités :**
   - Templates = présentation uniquement
   - Logique métier = dans les routes Python
   - JavaScript = interactions légères côté client

### Limitations actuelles

- **Un seul template :** Structure simple adaptée à une petite application
- **Pas d'héritage :** Pour étendre, créer un `base.html` et utiliser `{% extends %}`
- **JavaScript inline :** Pour un projet plus grand, externaliser dans `static/js/`

### Évolutions possibles

- Créer un `base.html` pour factoriser l'en-tête et le pied de page
- Ajouter des templates pour l'historique des calculs
- Implémenter des messages flash pour les erreurs utilisateur
- Créer un template d'erreur personnalisé (404, 500)

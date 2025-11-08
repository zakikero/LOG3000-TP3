# Module static/

## Raison d'être

Ce module contient tous les fichiers statiques de l'application Flask Calculator. Les fichiers statiques sont des ressources qui ne changent pas dynamiquement et sont servis directement par Flask au navigateur sans traitement côté serveur.

## Fichiers contenus

### `style.css`

**Responsabilité :** Feuille de style principale de l'application

- Définit l'apparence visuelle complète de la calculatrice
- Utilise CSS Grid pour la disposition des boutons en grille 4x4
- Implémente un design moderne avec effets de survol et transitions
- Thème sombre avec boutons d'opérateurs en orange (#ff9500)
- Responsive avec largeur maximale de 600px

**Sections principales :**

- Centrage et mise en page globale (body)
- Conteneur de la calculatrice (.calculator)
- Champ d'affichage (#display)
- Grille de boutons (.buttons)
- Styles des boutons (.btn, .operator)
- États interactifs (:hover, :active)

## Dépendances

- **Flask :** Utilise le système de fichiers statiques de Flask via `url_for('static', filename='...')`
- **Navigateurs modernes :** Requiert le support de CSS Grid (IE11+ non supporté)

## Hypothèses

- Le répertoire `static/` est configuré comme dossier statique par défaut dans Flask
- Les fichiers sont accessibles via l'URL `/static/` en production
- Le template HTML référence correctement les fichiers via `{{ url_for('static', filename='style.css') }}`

## Utilisation

Les fichiers de ce répertoire sont automatiquement servis par Flask. Pour ajouter un nouveau fichier statique (image, JavaScript, etc.) :

1. Placer le fichier dans ce répertoire
2. Référencer dans le template HTML via : `{{ url_for('static', filename='nom_fichier.ext') }}`

## Notes pour les développeurs

- **Ne pas modifier en production :** Les fichiers statiques sont généralement mis en cache par les navigateurs. Utiliser le versioning ou cache-busting si nécessaire.
- **Performance :** En production, considérer l'utilisation d'un CDN ou d'un serveur web (nginx, Apache) pour servir les fichiers statiques plutôt que Flask.
- **Organisation :** Pour des projets plus grands, organiser en sous-répertoires (`css/`, `js/`, `images/`, etc.)

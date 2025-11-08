# Module de tests - Flask Calculator

## Description

Ce répertoire contient tous les tests unitaires et d'intégration pour l'application Flask Calculator. Les tests sont organisés par module testé et utilisent le framework pytest pour l'exécution et les assertions.

## Structure des fichiers

```
tests/
├── __init__.py              # Initialisation du package de tests
├── README.md                # Ce fichier - Documentation des tests
├── test_operators.py        # Tests unitaires pour operators.py
├── test_calculate.py        # Tests unitaires pour la fonction calculate()
└── test_routes.py           # Tests d'intégration pour les routes Flask
```

## Installation des dépendances de test

Avant d'exécuter les tests, vous devez installer pytest :

```bash
pip install pytest
```

Pour les tests avec rapport de couverture (optionnel) :

```bash
pip install pytest-cov
```

## Comment exécuter les tests

> **Note :** Utilisez `python -m pytest` pour exécuter les tests sans environnement virtuel.

### Exécuter tous les tests

Depuis le répertoire racine du projet (LOG3000-TP3/) :

```bash
python -m pytest tests/
```

Ou avec plus de détails (mode verbose) :

```bash
python -m pytest tests/ -v
```

### Exécuter un fichier de test spécifique

Pour tester uniquement les opérateurs :

```bash
python -m pytest tests/test_operators.py -v
```

Pour tester uniquement la fonction calculate :

```bash
python -m pytest tests/test_calculate.py -v
```

Pour tester uniquement les routes Flask :

```bash
python -m pytest tests/test_routes.py -v
```

### Exécuter une classe de tests spécifique

```bash
python -m pytest tests/test_operators.py::TestAdd -v
```

### Exécuter un test spécifique

```bash
python -m pytest tests/test_operators.py::TestAdd::test_add_positive_numbers -v
```

### Options utiles de pytest

- `-v` ou `--verbose` : Affiche plus de détails sur chaque test
- `-s` : Affiche les sorties print() pendant les tests
- `-x` : Arrête à la première erreur
- `--tb=short` : Affiche un traceback court en cas d'erreur
- `-k "test_add"` : Exécute seulement les tests dont le nom contient "test_add"

## Couverture des tests

### test_operators.py

**Module testé :** `operators.py`

**Fonctions testées :**

- `add(a, b)` - Addition de deux nombres
- `subtract(a, b)` - Soustraction (b - a)
- `multiply(a, b)` - Puissance (a \*\* b)
- `divide(a, b)` - Division entière (a // b)

**Types de tests :**

- Cas normaux (nombres positifs)
- Gestion d'erreurs (division par zéro)

**Nombre de tests :** 5 tests

### test_calculate.py

**Module testé :** `app.py` (fonction `calculate`)

**Fonction testée :**

- `calculate(expr)` - Parse et évalue une expression arithmétique

**Types de tests :**

- Expressions valides (toutes les opérations)
- Expressions avec espaces
- Nombres négatifs
- Erreurs de format (expression vide, plusieurs opérateurs)
- Division par zéro

**Nombre de tests :** 9 tests

### test_routes.py

**Module testé :** `app.py` (routes Flask)

**Routes testées :**

- `GET /` - Affichage du formulaire
- `POST /` - Soumission et calcul d'expressions

**Types de tests :**

- Codes de statut HTTP
- Présence d'éléments dans le template
- Calculs corrects pour chaque opération
- Gestion d'erreurs (expressions invalides)
- Nombres négatifs

**Nombre de tests :** 7 tests

**Total : 21 tests**

## Interprétation des résultats

### Tests réussis

Lorsque tous les tests passent, vous verrez :

```
===================== 21 passed in 0.50s =====================
```

### Tests échoués

En cas d'échec, pytest affiche :

- Le nom du test qui a échoué
- La ligne où l'assertion a échoué
- La valeur attendue vs la valeur obtenue
- Le traceback complet

Exemple :

```
FAILED tests/test_operators.py::TestSubtract::test_subtract_positive_numbers
AssertionError: Expected 7, but got -7
```

Cela indique un bogue dans l'implémentation qu'il faut corriger.

## Bogues connus et Issues GitHub

Après l'exécution des tests, certains tests peuvent échouer, révélant des bogues dans le code. Pour chaque test échoué :

1. **Analysez l'erreur** : Comprenez pourquoi le test échoue
2. **Reproduisez le bogue** : Vérifiez manuellement dans l'application
3. **Ouvrez une Issue GitHub** avec :
   - Titre clair décrivant le problème
   - Description détaillée
   - Étapes de reproduction
   - Résultat attendu vs obtenu
   - Test(s) échoué(s)
   - Label approprié (bug, high-priority, etc.)

### Exemple d'Issue pour un test échoué

**Titre :** Bug dans subtract() - Ordre des opérandes inversé

**Description :**

```
La fonction subtract(a, b) retourne a - b au lieu de b - a comme documenté.

Test échoué : test_operators.py::TestSubtract::test_subtract_positive_numbers

Résultat attendu : subtract(3, 10) devrait retourner 7 (10-3)
Résultat obtenu : subtract(3, 10) retourne -7 (3-10)

Fichier : operators.py, ligne 28
```

## Bonnes pratiques

- Exécuter les tests avant chaque commit
- Ajouter des tests pour chaque nouveau bug découvert
- Maintenir une couverture de code élevée (>80%)
- Écrire des tests clairs et bien documentés
- Tester les cas normaux, limites et d'erreur
- Utiliser des assertions avec des messages explicites

## Ressources

- [Documentation pytest](https://docs.pytest.org/)
- [pytest-cov documentation](https://pytest-cov.readthedocs.io/)
- [Flask testing documentation](https://flask.palletsprojects.com/en/latest/testing/)

---

**Maintenu par l'Équipe 07**

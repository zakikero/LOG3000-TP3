"""
Tests d'intégration pour les routes Flask de l'application

Ce fichier contient les tests pour les routes de l'application Flask.
Les tests vérifient le comportement de l'interface web, les requêtes GET/POST,
et le rendu des templates.

Routes testées:
    - GET / : Affichage du formulaire vide
    - POST / : Soumission d'expressions et affichage des résultats
"""

import pytest
import sys
import os

# Ajouter le répertoire parent au path pour pouvoir importer app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


@pytest.fixture
def client():
    """
    Fixture pytest pour créer un client de test Flask.
    
    Crée un client de test qui permet de simuler des requêtes HTTP
    vers l'application Flask sans avoir à démarrer un serveur.
    
    Sorties:
        FlaskClient: Client de test Flask configuré
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestIndexRouteGET:
    """
    Tests pour la route GET /
    
    Vérifie que la page d'accueil s'affiche correctement
    sans erreur et avec le contenu attendu.
    """
    
    def test_index_get_status_code(self, client):
        """
        Test du code de statut HTTP pour GET /.
        
        Vérifie que la requête GET retourne 200 (OK)
        """
        response = client.get('/')
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    def test_index_get_contains_form(self, client):
        """
        Test de la présence d'un formulaire dans la page.
        
        Vérifie qu'il y a un élément <form> dans le HTML
        """
        response = client.get('/')
        assert b'<form' in response.data, "Expected form element in response"
    
    def test_calculator_buttons_display_correctly(self, client):
        """
        Test des bugs d'affichage des boutons de la calculatrice.
        
        BUG #4: Plusieurs boutons ont un affichage incorrect dans le HTML :
        - Bouton "2" affiche "02" au lieu de "2"
        - Bouton "8" affiche "88" au lieu de "8"
        - Bouton "*" (multiplication) est vide (pas de texte)
        - Bouton "/" (division) est vide (pas de texte)
        
        Ce test vérifie que TOUS les boutons (0-9, +, -, *, /, C, =) 
        ont le texte correct affiché.
        """
        response = client.get('/')
        html = response.data.decode('utf-8')
        
        # Vérifier tous les boutons numériques (0-9)
        expected_buttons = {
            '0': "onclick=\"appendToDisplay('0')\">0</button>",
            '1': "onclick=\"appendToDisplay('1')\">1</button>",
            '2': "onclick=\"appendToDisplay('2')\">2</button>",  
            '3': "onclick=\"appendToDisplay('3')\">3</button>",
            '4': "onclick=\"appendToDisplay('4')\">4</button>",
            '5': "onclick=\"appendToDisplay('5')\">5</button>",
            '6': "onclick=\"appendToDisplay('6')\">6</button>",
            '7': "onclick=\"appendToDisplay('7')\">7</button>",
            '8': "onclick=\"appendToDisplay('8')\">8</button>",  
            '9': "onclick=\"appendToDisplay('9')\">9</button>",
        }
        
        # Vérifier tous les boutons opérateurs
        expected_operators = {
            '+': "onclick=\"appendToDisplay('+')\">+</button>",
            '-': "onclick=\"appendToDisplay('-')\">-</button>",
            '*': "onclick=\"appendToDisplay('*')\">*</button>",
            '/': "onclick=\"appendToDisplay('/')\">/</button>",
        }
        
        # Vérifier les boutons de contrôle
        expected_controls = {
            'C': "onclick=\"clearDisplay()\">C</button>",
            '=': "type=\"submit\" class=\"btn operator\">=</button>",
        }
        
        # Tester tous les boutons numériques
        for digit, expected_html in expected_buttons.items():
            assert expected_html in html, \
                f"Bug: Button '{digit}' not displaying correctly. Expected pattern: {expected_html}"
        
        # Tester tous les boutons opérateurs
        for operator, expected_html in expected_operators.items():
            assert expected_html in html, \
                f"Bug: Operator button '{operator}' not displaying correctly. Expected pattern: {expected_html}"
        
        # Tester les boutons de contrôle
        for control, expected_html in expected_controls.items():
            assert expected_html in html, \
                f"Bug: Control button '{control}' not displaying correctly. Expected pattern: {expected_html}"
        
        # Vérifier qu'il n'y a PAS les bugs connus
        assert '>02</button>' not in html, "Bug: Found '02' instead of '2' in button display"
        assert '>88</button>' not in html, "Bug: Found '88' instead of '8' in button display"
        
        # Vérifier qu'il n'y a pas de boutons vides pour * et /
        # Un bouton vide aurait la forme: onclick="appendToDisplay('*')"></button>
        assert "onclick=\"appendToDisplay('*')\"></button>" not in html, \
            "Bug: Multiplication button (*) is empty - missing display text"
        assert "onclick=\"appendToDisplay('/')\"></button>" not in html, \
            "Bug: Division button (/) is empty - missing display text"


class TestIndexRoutePOST:
    """
    Tests pour la route POST /
    
    Vérifie que les calculs sont effectués correctement
    et que les résultats sont affichés dans le template.
    """
    
    def test_index_post_addition(self, client):
        """
        Test de l'addition via POST.
        
        Vérifie que POST avec "5+3" affiche 8 dans la réponse
        """
        response = client.post('/', data={'display': '5+3'})
        assert response.status_code == 200
        assert b'8' in response.data, "Expected result '8' in response"
    
    def test_index_post_subtraction(self, client):
        """
        Test de la soustraction via POST.
        
        Vérifie que POST avec "10-4" affiche 6 dans la réponse
        """
        response = client.post('/', data={'display': '10-4'})
        assert response.status_code == 200
        assert b'6' in response.data, "Expected result '6' in response"
    
    def test_index_post_empty_expression(self, client):
        """
        Test avec une expression vide via POST.
        
        Vérifie que POST avec "" affiche un message d'erreur
        """
        response = client.post('/', data={'display': ''})
        assert response.status_code == 200
        assert b'Error' in response.data, "Expected error message in response"
    
    def test_index_post_division_by_zero(self, client):
        """
        Test de division par zéro via POST.
        
        Vérifie que POST avec "5/0" affiche un message d'erreur
        """
        response = client.post('/', data={'display': '5/0'})
        assert response.status_code == 200
        assert b'Error' in response.data, "Expected error message in response"
    
    def test_index_post_negative_numbers(self, client):
        """
        Test avec des nombres négatifs via POST.
        
        Vérifie que POST avec "-5+10" affiche 5
        """
        response = client.post('/', data={'display': '-5+10'})
        assert response.status_code == 200
        assert b'5' in response.data, "Expected result '5' in response"



if __name__ == "__main__":
    # Permet d'exécuter les tests directement avec: python test_routes.py
    pytest.main([__file__, "-v"])

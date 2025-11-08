"""
Tests unitaires pour la fonction calculate() du module app.py

Ce fichier contient les tests pour la fonction calculate() qui parse et évalue
les expressions arithmétiques. Les tests couvrent les cas valides, les erreurs
de format et les cas limites.

Fonction testée:
    - calculate(expr): Parse et évalue une expression arithmétique simple
"""

import pytest
import sys
import os

# Ajouter le répertoire parent au path pour pouvoir importer app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import calculate


class TestCalculateValid:
    """
    Tests pour les expressions valides avec calculate()
    
    Vérifie que la fonction parse et calcule correctement les expressions
    arithmétiques bien formées.
    """
    
    def test_calculate_addition(self):
        """
        Test de l'addition via calculate.
        
        Vérifie que "5+3" retourne 8
        """
        result = calculate("5+3")
        assert result == 8, f"Expected 8, but got {result}"
    
    def test_calculate_subtraction(self):
        """
        Test de la soustraction via calculate.
        
        Vérifie que "10-4" retourne 6 (4 soustrait de 10)
        """
        result = calculate("10-4")
        assert result == 6, f"Expected 6, but got {result}"
    
    def test_calculate_multiplication(self):
        """
        Test de la multiplication (puissance) via calculate.
        
        Vérifie que "2*3" retourne 8 (2^3)
        """
        result = calculate("2*3")
        assert result == 8, f"Expected 8, but got {result}"
    
    def test_calculate_division(self):
        """
        Test de la division (entière) via calculate.
        
        Vérifie que "10/3" retourne 3 (division entière)
        """
        result = calculate("10/3")
        assert result == 3, f"Expected 3, but got {result}"
    
    def test_calculate_negative_numbers(self):
        """
        Test du calcul avec des nombres négatifs.
        
        Vérifie que "-5+10" retourne 5
        """
        result = calculate("-5+10")
        assert result == 5, f"Expected 5, but got {result}"


class TestCalculateErrors:
    """
    Tests pour les cas d'erreur avec calculate()
    
    Vérifie que la fonction lève les bonnes exceptions pour les
    expressions invalides ou mal formées.
    """
    
    def test_calculate_empty_expression(self):
        """
        Test avec une expression vide.
        
        Vérifie que calculate("") lève ValueError
        """
        with pytest.raises(ValueError, match="empty expression"):
            calculate("")
    
    def test_calculate_multiple_operators(self):
        """
        Test avec plusieurs opérateurs.
        
        Vérifie que "5+3-2" lève ValueError (un seul opérateur autorisé)
        """
        with pytest.raises(ValueError, match="only one operator is allowed"):
            calculate("5+3-2")
    
    def test_calculate_division_by_zero(self):
        """
        Test de division par zéro.
        
        Vérifie que "5/0" lève ZeroDivisionError
        """
        with pytest.raises(ZeroDivisionError):
            calculate("5/0")


class TestCalculateEdgeCases:
    """
    Tests pour les cas limites avec calculate()
    
    Vérifie le comportement de la fonction dans des situations
    particulières ou à la limite de la spécification.
    """
    
    def test_calculate_with_spaces(self):
        """
        Test avec des espaces dans l'expression.
        
        Vérifie que "5 + 3" retourne 8
        """
        result = calculate("5 + 3")
        assert result == 8, f"Expected 8, but got {result}"


if __name__ == "__main__":
    # Permet d'exécuter les tests directement avec: python test_calculate.py
    pytest.main([__file__, "-v"])

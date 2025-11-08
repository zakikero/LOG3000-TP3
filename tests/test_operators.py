"""
Tests unitaires pour le module operators.py

Ce fichier contient les tests pour toutes les fonctions arithmétiques
définies dans operators.py. Chaque fonction est testée avec plusieurs
cas incluant les valeurs normales, les cas limites et les erreurs attendues.

Fonctions testées:
    - add(a, b): Addition
    - subtract(a, b): Soustraction
    - multiply(a, b): Puissance
    - divide(a, b): Division entière
"""

import pytest
import sys
import os

# Ajouter le répertoire parent au path pour pouvoir importer operators
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from operators import add, subtract, multiply, divide


class TestAdd:
    """
    Tests pour la fonction add(a, b)
    
    La fonction add devrait retourner la somme de a et b.
    """
    
    def test_add_positive_numbers(self):
        """
        Test de l'addition de deux nombres positifs.
        
        Vérifie que 5 + 3 = 8
        """
        result = add(5, 3)
        assert result == 8, f"Expected 8, but got {result}"


class TestSubtract:
    """
    Tests pour la fonction subtract(a, b)
    
    La fonction subtract devrait retourner b - a (attention à l'ordre!)
    """
    
    def test_subtract_positive_numbers(self):
        """
        Test de la soustraction de deux nombres positifs.
        
        Vérifie que subtract(3, 10) = 10 - 3 = 7
        """
        result = subtract(3, 10)
        assert result == 7, f"Expected 7, but got {result}"


class TestMultiply:
    """
    Tests pour la fonction multiply(a, b)
    
    La fonction multiply devrait retourner a ** b (puissance, pas multiplication!)
    """
    
    def test_multiply_basic_power(self):
        """
        Test de la puissance basique.
        
        Vérifie que multiply(2, 3) = 2^3 = 8
        """
        result = multiply(2, 3)
        assert result == 8, f"Expected 8, but got {result}"


class TestDivide:
    """
    Tests pour la fonction divide(a, b)
    
    La fonction divide devrait retourner a // b (division entière)
    """
    
    def test_divide_with_remainder(self):
        """
        Test de la division avec reste.
        
        Vérifie que divide(10, 3) = 10 // 3 = 3
        """
        result = divide(10, 3)
        assert result == 3, f"Expected 3, but got {result}"
    
    def test_divide_by_zero(self):
        """
        Test de la division par zéro.
        
        Vérifie que divide(5, 0) lève une ZeroDivisionError
        """
        with pytest.raises(ZeroDivisionError):
            divide(5, 0)


if __name__ == "__main__":
    # Permet d'exécuter les tests directement avec: python test_operators.py
    pytest.main([__file__, "-v"])

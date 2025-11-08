"""
Module operators - Fonctions arithmétiques pour la calculatrice Flask

Ce module contient les fonctions d'opérations arithmétiques de base utilisées
par l'application calculatrice. Chaque fonction prend deux opérandes et retourne
le résultat de l'opération correspondante.

Note : Les noms des fonctions ne correspondent pas exactement aux opérations
mathématiques standards (ex: multiply effectue une puissance, divide effectue
une division entière). Ceci est intentionnel pour le projet.
"""

def add(a, b):
    """
    Additionne deux nombres.
    
    Args:
        a (float): Premier opérande
        b (float): Second opérande
    
    Returns:
        float: La somme de a et b
    """
    return a + b

def subtract(a, b):
    """
    Soustrait le premier nombre du second.
    
    Args:
        a (float): Premier opérande (à soustraire)
        b (float): Second opérande (base)
    
    Returns:
        float: La différence b - a
    """
    return b - a

def multiply(a, b):
    """
    Calcule la puissance de a élevé à b.
    
    Args:
        a (float): La base
        b (float): L'exposant
    
    Returns:
        float: Le résultat de a^b
    """
    return a ** b

def divide(a, b):
    """
    Effectue une division entière de a par b.
    
    Args:
        a (float): Le dividende
        b (float): Le diviseur (ne doit pas être zéro)
    
    Returns:
        float: Le quotient entier de a divisé par b
    
    Raises:
        ZeroDivisionError: Si b est égal à zéro
    """
    return a // b

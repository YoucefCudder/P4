#!/usr/bin/python3
# coding: utf8
from tinydb import TinyDB


# recherche des objets contenant toute la logique de mon logiciel de gestion de tournois d'échecs
# les classes de mon modèle doivent permettre de rendre le logiciel au minimum fonctionnel sans vue(interface)
# et sans controller.
# Recherche d'une logique POO  où les attributs et les méthodes permettent de faire interagir mes objets entre eux


class Player:
    """class to define what compose the information's player and what a player does"""

    MALE = "M"
    FEMALE = "F"

    def __init__(self, name, f_name, age, birthdate, gender, ranking, score):
        """
        method to initialize
        """

        self.name = name
        self.f_name = f_name
        self.age = age
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = score

    def __str__(self):
        """Doctring."""


    def playing(self):
        """Doctring."""
        pass

    def winning(self):
        """Docstring"""
        self.score += 1
        pass

    def drawing(self):
        """Docstring"""
        self.score += 0.5
        pass


class Players:
    """class to manage a list of players for a tournament"""

    def __init__(self):
        """Docstring"""
        pass

#!/usr/bin/python3
# coding: utf8

# recherche des objets contenant toute la logique de mon logiciel de gestion de tournois d'échecs
# les classes de mon modèle doivent permettre de rendre le logiciel au minimum fonctionnel sans vue(interface)
# et sans controller.
# Recherche d'une logique POO  où les attributs et les méthodes permettent de faire interagir mes objets entre eux


class Tournament:
    """ class to define what compose and what does a tournament"""

    pass
    # a tournament is a group of rounds of matches with a final ranking of players.
    # a tournament has a name, a location, a date(it can be on more than 1 day), a number of rounds (4),
    # a list of players,a time controler (bullet, biltz or "coup rapide") and a description

    def __init__(self):
        """Docstring"""
        pass


class Round:
    """class to define what a round is and what it does"""

    pass
    # a round consists to split a list of players according to their ranking in half,
    # the matchmaking goes to 1-5, 2-6, 3-7, 4-8, the matchmaking picks the next player
    #  if 2 players already played against each others
    def __init__(self):
        """Docstring"""
        pass

    def matchmaking(self):
        """Docstring"""
        pass

    def looping_rounds(self):
        """Docstring"""
        pass


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
        self.score = 0

    def __str__(self):
        """Doctring."""
        pass

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

    def losing(self):
        """Docstring"""
        pass


class Players:
    """class to manage a list of players for a tournament"""

    def __init__(self):
        """Docstring"""
        pass


class Ranking:
    """ a class that manages the ranking of players in a tournament"""

    pass
    # the ranking is essential to make the matchmaking during the rounds
    # the update of the ranking can be made at any time, manually.

    def updating(self):
        pass


class Report:
    """a class that manage the report, which a collection of the general data of a tournament """

    pass


# the report of a tournament contains the list of all the players sorted by alphabetical or ranking,
# the list of all players of  a tournament sorted by alphabetical or ranking, the list of all tournaments,
# the list of all rounds of a tournament and the list of all the matchs of a tournament

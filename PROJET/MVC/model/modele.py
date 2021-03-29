#!/usr/bin/python3
# coding: utf8
from tinydb import TinyDB
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

player_1 = Player(name='Ngannou', f_name='Francis', age=34, birthdate=None, gender='M', ranking=None, score=0)
player_2 = Player(name='Nurmagomedov', f_name='Khabib', age=32, birthdate=None, gender='M', ranking=None, score=0)
player_3 = Player(name='Nunes', f_name='Amanda', age=31, birthdate=None, gender='F', ranking=None, score=0)
player_4 = Player(name='Jones', f_name='Jon', age=35,  birthdate=None, gender='M', ranking=None, score=0)
player_5 = Player(name='Adesanya', f_name='Israel', age=30, birthdate=None, gender='M', ranking=None, score=0)
player_6 = Player(name='Zhang', f_name='Weili', age=29, birthdate=None, gender='F', ranking=None, score=0)
player_7 = Player(name='Yan', f_name='Petr', age=28, birthdate=None, gender='M', ranking=None, score=0)
player_8 = Player(name='St-Pierre', f_name='Georges', age=39, birthdate=None, gender='M', ranking=None, score=0)


serialized_player_1 = {
    'name': player_1.name,
    'f_name' : player_1.f_name, 
    'age': player_1.age,
    'birthdate' : player_1.birthdate,
    'gender' : player_1.gender, 
    'ranking' : player_1.ranking,
    'score' : player_1.score
    
}
serialized_player_2 = {
    'name': player_2.name,
    'f_name' : player_2.f_name, 
    'age': player_2.age,
    'birthdate' : player_2.birthdate,
    'gender' : player_2.gender, 
    'ranking' : player_2.ranking,
    'score' : player_2.score
    
}
serialized_player_3 = {
    'name': player_3.name,
    'f_name' : player_3.f_name, 
    'age': player_3.age,
    'birthdate' : player_3.birthdate,
    'gender' : player_3.gender, 
    'ranking' : player_3.ranking,
    'score' : player_3.score
    
}
serialized_player_4 = {
    'name': player_4.name,
    'f_name' : player_4.f_name, 
    'age': player_4.age,
    'birthdate' : player_4.birthdate,
    'gender' : player_4.gender, 
    'ranking' : player_4.ranking,
    'score' : player_4.score
    
}
serialized_players = (serialized_player_1, serialized_player_2, serialized_player_3, serialized_player_4)

def __index__(self): 
    name = serialized_players['name']
    f_name = serialized_players['f_name']
    age = serialized_players['age']
    birthdate = serialized_players['birthdate']
    gender = serialized_players['gender']
    ranking = serialized_players['ranking']
    score = serialized_players['score']

db = TinyDB('db.json')
players_table = db.table('players')
players_table.truncate()	# clear the table first
players_table.insert_multiple(serialized_players)

serialized_players = players_table.all()

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

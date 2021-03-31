#!/usr/bin/python3
# coding: utf8


class Tournament:
    """ class to define what compose and what does a tournament"""

    def __init__(self, tournament_name=None, date=None, rounds=None, number_of_rounds=None, players=None,
                 time_control=None, description=None, location=None):
        """Docstring"""
        self.tournament_name = tournament_name
        self.location = location
        self.date = date
        self.rounds = rounds
        self.number_of_rounds = number_of_rounds
        self.players = players
        self.time_control = time_control
        self.description = description

# a tournament is a group of rounds of matches with a final ranking of players.
# a tournament has a name, a location, a date(it can be on more than 1 day), a number of rounds (4),
# a list of players,a time controler (bullet, biltz or "coup rapide") and a description


class Report:
    """a class that manage the report, which a collection of the general data of a tournament """

    pass
# the report of a tournament contains the list of all the players sorted by alphabetical or ranking,
# the list of all players of  a tournament sorted by alphabetical or ranking, the list of all tournaments,
# the list of all rounds of a tournament and the list of all the matchs of a tournament

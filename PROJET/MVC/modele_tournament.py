#!/usr/bin/python3
# coding: utf8
from tinydb import TinyDB
import datetime


class Tournaments:
    """class that defines what contains a tournament 
    """

    def __init__(self, name, place, start, end, rounds, timing, description, players):
        self.name = name
        self.place = place
        self.start = start
        self.end = end
        self.rounds = rounds
        self.timing = timing
        self.description = description
        self.date = str(datetime.datetime.now())
        self.players = players

    def create_tournament(self):
        db = TinyDB('db_tournaments.json')
        tournaments_table = db.table('tournaments')

        tournaments_table.insert({
            'name': self.name,
            'place': self.place,
            'start': self.start,
            'end': self.end,
            'rounds': self.rounds,
            'timing': self.timing,
            'description': self.description,
            'date': self.date,
            'players': self.players
        })

        return f'date du tournoi : {self.date}'


tournoi = Tournaments('ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok')
print(Tournaments.create_tournament(tournoi))
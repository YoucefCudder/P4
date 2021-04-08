#!/usr/bin/python3
# coding: utf8
from tinydb import TinyDB


class Player:
    """class to define what compose the information's player and what a player does"""

    def __init__(self):

        self.f_name = self.f_name
        self.name = self.name
        self.gender = self.gender
        self.birthdate = self.birthdate
        self.age = self.age
        self.score = self.score
        self.ranking = self.ranking

    def create_player(self):
        db = TinyDB('db_player.json')
        players_table = db.table('players')

        players_table.insert({
            'name': self.name,
            'f_name': self.f_name,
            'birthdate': self.birthdate,
            'gender': self.gender,
            'ranking': self.ranking
        })

        print(f"Le joueur {self.f_name} {self.name} a été créé")




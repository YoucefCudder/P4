#!/usr/bin/python3
# coding: utf8
import sys
import os

sys.path.insert(0, './PROJET/MVC')
from modele_tournament import Tournaments


class TournamentControl():
    def create_tournament(self):
        self.name = input('Name: ')
        self.place = input('Place: ')
        self.start = input('Start: ')
        self.end = input('End: ')
        self.rounds = input('Rounds:  ')
        self.timing = input('Timing:  ')
        self.description = input('Description: ')
        self.date = input('Date: ')
        self.players = input('Players: ')

        return {'name': self.name, 'place': self.place, 'start': self.start, 'end': self.end,
                'rounds': self.rounds,'timing': self.timing, 'description': self.description,
                'date': self.date, 'players': self.players}


nouveau_tournoi = TournamentControl().create_tournament()

Tournaments(name=nouveau_tournoi['name'], place=nouveau_tournoi['place'], start=nouveau_tournoi['start'],
                  end=nouveau_tournoi['end'], rounds=nouveau_tournoi['rounds'], timing=nouveau_tournoi['timing'],
                  description=nouveau_tournoi['description'], date=nouveau_tournoi['date'], players=nouveau_tournoi['players']).create_tournament()

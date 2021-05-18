#!/usr/bin/python3
# coding: utf8
import sys
import os
from PROJET.MVC.modele_tournament import Tournaments
from datetime import datetime

sys.path.insert(0, './PROJET/MVC')


class TournamentControl:
    def create_tournament(self):
        self.name = input('Name: ')
        self.place = input('Place: ')
        self.start = input('Start: ')
        self.end = input('End: ')
        self.rounds = input('Rounds:  ')
        self.timing = input('Timing:  ')
        self.description = input('Description: ')
        self.date = datetime.now().strftime('%d-%m-%y %H:%M:%S')

        return {'name': self.name, 'place': self.place, 'start': self.start, 'end': self.end,
                'rounds': self.rounds, 'timing': self.timing, 'description': self.description,
                'date': self.date}




nouveau_tournoi = TournamentControl().create_tournament()

Tournaments(name=nouveau_tournoi['name'], place=nouveau_tournoi['place'], start=nouveau_tournoi['start'],
            end=nouveau_tournoi['end'], rounds=nouveau_tournoi['rounds'], timing=nouveau_tournoi['timing'],
            description=nouveau_tournoi['description'], date=nouveau_tournoi['date']).create_tournament()

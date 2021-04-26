#!/usr/bin/python3
# coding: utf8
import sys
import os
from tinydb import TinyDB


sys.path.insert(0, './PROJET/MVC')
from modele_player import Player


class PlayersControl():

    def create_players(self):
        """ Input for create player & return inputs """
        
        self.f_name = input('Prénom : ')
        self.name = input('Nom : ')
        self.birthdate = input('Date de naissance (DD-MM-YYYY): ')
        self.genre = input('genre (M ou F) : ')
        self.age = input("Âge ? ")
        self.score = input('Score : ')
        self.ranking = input('Classement: ')
        
        return {'f_name': self.f_name, 'name': self.name, 'gender': self.genre, 'birthdate': self.birthdate,
            'age': self.age, 'score': self.score, 'ranking': self.ranking}
        
        
        
    
   
nouveau_joueur = PlayersControl().create_players()


Player(f_name=nouveau_joueur['f_name'], name=nouveau_joueur['name'], gender=nouveau_joueur['gender'],
       birthdate=nouveau_joueur['birthdate'], age=nouveau_joueur['age'], score=nouveau_joueur['score'],
       ranking=nouveau_joueur['ranking']).create_players()

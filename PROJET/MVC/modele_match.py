#!/usr/bin/python3
# coding: utf8

class Score:
    """ a class that manages the ranking of players in a tournament"""

    def updating_score(self):
        self.win = 1
        self.loss = 0
        self.draw = 0.5
        
        return f'le score a été mis à jour'
    
    

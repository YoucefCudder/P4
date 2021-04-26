#!/usr/bin/python3
# coding: utf8
import sys
import os
from tinydb import TinyDB


sys.path.insert(0, './PROJET/MVC')
from modele_match import Score
from modele_player import Player

class ScoreControl:
    
    
    def input_score(self):
        Player.score = input('')




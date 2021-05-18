#!/usr/bin/python3
# coding: utf8
import sys
import os
from tinydb import TinyDB
from PROJET.MVC.modele_player import Player

sys.path.insert(0, './PROJET/MVC')


class Score:
    """ a class that manages the scores of a match in a round"""

    def __init__(self, win, loose, draw):
        self.win = 1
        self.loose = 0
        self.draw = 0.5

    def updating_score(self):

#!/usr/bin/python3
# coding: utf8
import sys
import os
from tinydb import TinyDB

sys.path.insert(0, './model')
from modele_player import Player


class AddPlayer:
    def __init__(self, name, f_name, ranking):
        self.name = input('name:      ')
        self.f_name = input('first name:      ')
        self.ranking = input('ranking:        ')
        self.player_id = name + f_name + ranking

#!/usr/bin/python3
# coding: utf8


class Round:
    """class to define what a round is and what it does"""

    # a round consists to split a list of players according to their ranking in half,
    # the matchmaking goes to 1-5, 2-6, 3-7, 4-8, the matchmaking picks the next player
    #  if 2 players already played against each others

    def __init__(self, rounds):
        self.rounds = rounds

    def matchmaking(self):
        """Docstring"""
        pass

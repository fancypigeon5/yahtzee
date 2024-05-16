import random

class Player:
    """Creates an instance of a player"""
    scoresheet = {
        "1's" : "",
        "2's" : "",
        "3's" : "",
        "4's" : "",
        "5's" : "",
        "6's" : "",
        "Sum top" : "",
        "Bonus (if sum > 63)" : "",
        "Total top" : "",
        "Three of a kind" : "",
        "Four of a kind" : "",
        "Full House" : "",
        "Small straight" : "",
        "Large straight" : "",
        "YAHTZEE" : "",
        "YAHTZEE Bonus" : "",
        "Chance" : "",
        "Sum bottom" : "",
        "Total" : ""
    }

    def __init__(self, name, order):
        self.name = name
        self.order = order

    def throw(self, set_aside):
        throw = {}
        for i in ["a", "b", "c", "d", "e", "f"]:
            if i not in set_aside:
                throw[i] = random.randrange(1, 6)
            else:
                throw[i] = set_aside[i]
        return throw
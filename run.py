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
        """ 
        generates an object with keys a to e
        and random values between 1 and 6
        """
        throw = {}
        for i in ["a", "b", "c", "d", "e"]:
            if i not in set_aside:
                throw[i] = random.randrange(1, 7)
            else:
                throw[i] = set_aside[i]
        return throw

    def turn(self):
        """
        Starts a players turn
        """
        set_aside = {}
        roll = {}
        i = 0
        while i < 3:
            roll = self.throw(set_aside)
            print("your throw was: \n"),
            for x in roll:
                print(f"{x} : [{roll[x]}] \n")
            if i < 2:
                stop_throwing = False
                while True:
                    again = input("Would you like to throw again? y/n: \n")
                    if again == "n":
                        stop_throwing = True
                        break
                    elif again == "y":
                        print("What dice do you want to keep?")
                        print("Enter the letters of the dice you want to keep")
                        print("for example: ace\n")
                        keep = input("Enter the dice to keep: \n")
                        set_aside = {}
                        for y in [*keep]:
                            set_aside[y] = roll[y]
                        break
                    else:
                        print("please enter y or n")
                if stop_throwing:
                    break
            i += 1

jules = Player("jules", 1)

jules.turn()
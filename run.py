import random
import copy

class Player:
    """Creates an instance of a player"""
    def __init__(self, name, scoresheet):
        self.name = name
        self.scoresheet = scoresheet
        self.yahtzee = False

    def calculated_places(self, throw):
        possible_places = {}
        x = 1
        while x < 7:
            if throw.count(x) == 5:
                self.yahtzee = True
                break
            x += 1
        for i in self.scoresheet.keys():
            if self.scoresheet[i] == '':
                x = 1
                while x < 7:
                    if i == f"{x}'s":
                        possible_places[i] = 0
                        for y in throw:
                            if y == x:
                                possible_places[i] += x
                    x += 1
                if i == "Three of a kind":
                    three_of_a_kind = False
                    x = 1
                    while x < 7:
                        if throw.count(x) >= 3:
                            three_of_a_kind = True
                            break
                        x += 1
                    if three_of_a_kind:
                        possible_places[i] = sum(throw)
                    else:
                        possible_places[i] = 0
                elif i == "Four of a kind":
                    four_of_a_kind = False
                    x = 1
                    while x < 7:
                        if throw.count(x) >= 4:
                            four_of_a_kind = True
                            break
                        x += 1
                    if four_of_a_kind:
                        possible_places[i] = sum(throw)
                    else:
                        possible_places[i] = 0        
                elif i == "Full House":
                    full_house = False
                    x = 1
                    while x < 7:
                        if throw.count(x) == 5:
                            full_house = True
                            break
                        elif throw.count(x) == 3:
                            y = 1
                            while y < 7:
                                if y != x and throw.count(y) >= 2:
                                    full_house = True
                                    break
                                y += 1
                        x += 1
                    if full_house:
                        possible_places[i] = 25
                    else:
                        possible_places[i] = 0
                elif i == "Small straight":
                    small_straight = False
                    x = 1
                    while x < 4:
                        y = 0
                        while y < 4:
                            if x + y in throw:
                                small_straight = True
                            else:
                                small_straight = False
                                break
                            y += 1
                        if small_straight == True:
                            break
                        x += 1
                    if small_straight:
                        possible_places[i] = 30
                    else:
                        possible_places[i] = 0
                elif i == "Large straight":
                    large_straight = False
                    x = 1
                    while x < 3:   
                        y = 0
                        while y < 5:
                            if x + y in throw:
                                large_straight = True
                            else:
                                large_straight = False
                                break
                            y += 1
                        if large_straight == True:
                            break
                        x += 1
                    if large_straight:
                        possible_places[i] = 40
                    else:
                        possible_places[i] = 0
                elif i == "YAHTZEE":
                    yahtzee = False
                    x = 1
                    while x < 7:
                        if throw.count(x) == 5:
                            yahtzee = True
                            break
                        x += 1
                    if yahtzee:
                        possible_places[i] = 50 
                    else:
                        possible_places[i] = 0
                elif i == "Chance":
                    possible_places[i] = sum(throw)
                    
        return possible_places

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

    def print_scoresheet(self):
        """
        prints the scoresheet
        """
        sum_top = 0
        sum_bottom = 0
        for i in ["1's", "2's", "3's", "4's", "5's", "6's"]:
            if self.scoresheet[i] != "":
                sum_top += self.scoresheet[i]
        for i in [
                "Three of a kind",
                 "Four of a kind", 
                 "Full House", 
                 "Small straight", 
                 "Large straight", 
                 "YAHTZEE", 
                 "YAHTZEE Bonus",
                 "Chance"
                 ]:
            if self.scoresheet[i] != "":
                sum_bottom += self.scoresheet[i]
        if sum_top >= 63:
            self.scoresheet["Bonus (if sum > 63)"] = 35
        else:
            self.scoresheet["Bonus (if sum > 63)"] = 0
        self.scoresheet["Sum top"] = sum_top
        self.scoresheet["Total top"] = self.scoresheet["Sum top"] + self.scoresheet["Bonus (if sum > 63)"]
        self.scoresheet["Sum bottom"] = sum_bottom
        self.scoresheet["Total"] = self.scoresheet["Sum bottom"] + self.scoresheet["Total top"]
        for i in self.scoresheet:
            if self.scoresheet[i] != "":
                print("%-20s| %-5i" % (i, self.scoresheet[i]))
            else:
                print("%-20s| %-5s" % (i, self.scoresheet[i]))

    def turn(self):
        """
        Starts a players turn
        """
        set_aside = {}
        roll = {}
        i = 0
        print(f"{self.name}'s turn, your scoresheet is")
        self.print_scoresheet()
        input("press any key to start rolling")
        self.yahtzee = False
        while i < 3:
            roll = self.throw(set_aside)
            print("your throw was: \n"),
            for x in roll:
                print(f"{x} : [{roll[x]}]")
            if i < 2:
                stop_throwing = False
                print("What dice do you want to keep?")
                print("Enter the letters of the dice you want to keep")
                print("for example: ace")
                print("If you do not want to throw again, enter x \n")
                while True:
                    keep = input("Enter the dice to keep: \n")
                    if keep == "x":
                        stop_throwing = True
                        break
                    elif len(keep) < 6:
                        set_aside_temp = {}
                        valid = True
                        for y in [*keep]:
                            if y in roll.keys():
                                set_aside_temp[y] = roll[y]
                            else:
                                valid = False
                        if valid:
                            set_aside = set_aside_temp
                            break
                    else:
                        print("please enter something valid")
                if stop_throwing:
                    break
            i += 1
        input("Press any key to choose where to fill in your score")
        possible_places = self.calculated_places(list(roll.values()))
        choices = {}
        x = 0
        for i in possible_places:
            key = "abcdefghijklmnopqrstuvwxyz"[x]
            choices[key] = [i, possible_places[i]]
            x += 1
        print("where do you want to fill it in?")
        for i in choices:
            print("%-2s| %-20s : %-5i" % (i, choices[i][0], choices[i][1]))
        while True:
            fill = input("Enter where to fill it in: \n")
            if fill in choices.keys():
                key = choices[fill][0]
                if self.yahtzee and key != "YAHTZEE":
                    if self.scoresheet["YAHTZEE Bonus"] == "":
                        self.scoresheet["YAHTZEE Bonus"] = 100
                    elif self.scoresheet["YAHTZEE Bonus"] < 300:
                        self.scoresheet["YAHTZEE Bonus"] += 100
                self.scoresheet[key] = choices[fill][1]
                break
        
        self.print_scoresheet()
        input("press any key to continue")

def start_game():
    num_of_players = 0
    players = []
    scoresheet_template = {
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
    while True:
        num_of_players = input("how many players are there? \n")
        try:
            num_of_players = int(num_of_players)
            break
        except ValueError:
            print("That's not an int!")
    i = 0
    while i < num_of_players:
        name = input(f"Enter player{i + 1} name? \n")
        scoresheet = copy.deepcopy(scoresheet_template)
        players.append(Player(name, scoresheet))
        i += 1
    total_rounds = 13
    round = 0
    while round < total_rounds:
        for i in players:
            i.turn()
        round += 1
    scores = {}
    for i in players:
        scores[i.name] = i.scoresheet["Total"]
    print(f"The winner is {max(scores, key=scores.get)} with {max(scores.values())} points")

start_game()
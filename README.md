# YAHTZEE

Yahtzee is a Python terminal game that runs on Code Institute's mock terminal on Heroku

The aim of the program is to let people enjoy a game of Yahtzee together.

[Here is the live version of the site](https://yahtzee-1-32ffa45a6b88.herokuapp.com)

## How to play

Yahtzee is a classic dice game where you get three throws each turn to roll five dice to get a desired outcome.
Each turn the player decides where on the scoresheet he wants to put the throw.
the game ends after 13 rounds when all of the possible places on the scoresheet have been filled.
for more info on the exact rules read [this wikipedia article](https://en.wikipedia.org/wiki/Yahtzee) 

choosing dice to keep and/or where to fill in the throw is done by writing the corresponding letters when asked.

## Features

- __Choose players__

    - Choose how many players are participating.
    - Every player can enter their name or nickname.

- __Dice rolls__

    - By rolling the dice 5 random numbers between 1 and 6 are generated and displayed as dice.
    - After rolling the player can decide what dice to keep (they are not rolled again in the next roll).
    - If a player is satisfied with the roll all next rolls of the turn can be skipped by entering x in the input field

- __Choosing a category for the roll__

    - After all 3 throws (or less if skipped) players will be presented with all available categories for this throw.
    - The total score for each category is calculated automaticly and displayed.

- __Scoresheet__

    - The scoresheets are kept and displayed on a players turn.
    - All totals (and top bonus, yahtzee bonus) are calculated automaticly and updated with each turn.

- __Input__

    - All the inputs are validated after entering


## Data Model



## Testing

## Deployment
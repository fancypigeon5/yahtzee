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

For this project I used an object oriented approach.
There is a class Player.
For each player a new instance is created containing a scoresheet, name and all the necessary methods for running a turn.

## Testing

The following tests have been done manually to make sure everything works.

- Run a game and make sure it stops after 13 rounds.
- Make sure the scoresheet is updated after each turn.
- Try invalid inputs: the game should ask you to input correct values.
- test both the terminal and the heroku deployed version.

The code was also put through this [PEP8 validator](https://pep8ci.herokuapp.com/#)
and passed all test without problem

## Deployment

For this project the Code Institute mock terminal for heroku was used.

### How to deploy

- Fork or Clone this repository
- Create a heroku app
- Add the buildpacks for Python and NodeJS in that order
- Link the app to the repository
- Deploy

# Credits

- Code Institute for the template.
- Wikipedia for the rules of Yahtzee
- Stackoverflow for when experiencing a problem, this site was very useful to find others experiencing simular issues.
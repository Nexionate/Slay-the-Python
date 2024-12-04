Ethan O'Connor - Nexionate - A01435041

# **My 1510 Project**

This is the first terminally based game I have created! Some first-time features I have programmed include

- deck of playable cards, with a draw, discard and current hand
- challenging turn-based combat, that includes damaging, blocking and energy consumption upon playing cards
- an enemy intent system that allows players to plan their turn ahead
- randomly generated map each run for heightened playability
- a pool of diverse cards players can add to their deck
- shops with randomly generated relics available for sale
- coloured and scrolling text, to increase readability and atmosphere
- Campfires where players can upgrade or rest, cultivating risk-reward gameplay
- an upgrade system, that lets player permanently strengthen a card of their choice
- a pool of various relics players can find to empower themselves
Your goal is to reach the bottom right tile.

## *Trust me, this took some time to make*

If you get stuck, type help at the map or combat input areas.



### For colorama to work
- py -m pip install colorama~=0.4.6
- or install colorama from pycharm packages

Funny quirk about colorama, the function I wrote to display text compactly has an unintended side-effect.
Since it is necessary to wrap a word with COLOUR and STYLE.RESET, this changes the underlying string. The reason for
creating the col() function has to do with colorama. If you want to colour one word in a sentence, you would need to
add STYLE.RESET after every word. If you don't, the rest of the sentence also becomes that colour. The function
automatically resets the colour after. However, this produced another side-effect. STYLE.RESET also changes
the original string.
This causes me to have to import colorama in unit tests and use the old method to make unit tests pass correctly.
If you want to see an example, go to test_initialize_game_print_board

F-strings were used once I realized they were required

See term project requirements below

| Required element                                                    |                                 File                                 | Line number |
|:--------------------------------------------------------------------|:--------------------------------------------------------------------:|------------:|
| a) use of immutable data structures like tuples                     |                         [enemy](./enemy.py)                          |          #1 |
| b) use of mutable data structures like lists and dictionaries       |                         [cards](./cards.py)                          |          #6 |
| c) thoughtful use of exceptions and exception handling              |                     [main_game](./main_game.py)                      |        #481 |
| d) minimized scope and lifetime of all variables and objects        |                     [main_game](./main_game.py)                      |        #381 |
| e) decomposition of your idea into small functions                  |                     [main_game](./main_game.py)                      |        #173 |
| f) simple flat code that is easy to understand                      |                     [main_game](./main_game.py)                      |  #184, #588 |
| g) comprehensions work though correct use of one or more list/dicts |                         [cards](./cards.py)                          |         #44 |
| h) selection using if-statements                                    |          [relics](./relics.py), [main_game](./main_game.py)          |  #147, #619 |
| i) repetition using the for-loop                                    |           [main_game](./main_game.py), [cards](./cards.py)           |  #106, #135 |
| j) use of the membership operator where it makes sense              | [initialize_game](./initialize_game.py), [main_game](./main_game.py) |  #110, #551 |
| k) appropriate use of the the range function                        |                     [main_game](./main_game.py)                      |  #106, #216 |
| l) use of one or more functions from itertools                      |                     [main_game](./main_game.py)                      |        #111 |
| m) the random module                                                |                     [main_game](./main_game.py)                      |        #178 |
| n) function annotations                                             |                     [main_game](./main_game.py)                      |        #816 |
| o) doctests and/or unit tests for every single function             |          See unit test folder, [main_game](./main_game.py)           |             |
| p) output must be formatted using f-strings                         |                     [main_game](./main_game.py)                      |        #149 |
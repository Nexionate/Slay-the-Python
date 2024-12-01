Ethan O'Connor - Nexionate - A01435041

# **My  1510 Project**

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
- unique events that offer players rewards

### *Trust me, this took some time to make*
If you get stuck, type help at most available input areas. 

See term project requirements below


CHANGES TO MAKE BEFORE LAUNCH
- check all input in fires, card rewards and shops
- LN145 in initialize game, doctest spacing
- cycle for boss attacks
- remove events
- update flowchart
- doctests 714 main (include?)

Funny quirk about colorama, the function I wrote to display text compactly has an unintended side-effect. 
Since it is necessary to wrap a word with COLOUR and STYLE.RESET, this changes the underlying string. The reason for
creating the col() function has to do with colorama. If you want to colour one word in a sentence, you would need to
add STYLE.RESET after every word. If you don't, the rest of the sentence also becomes that colour. The function 
automatically resets the colour after. However, this produced another side-effect. STYLE.RESET also changes
the original string.
This causes me to have to import colorama in unit tests and use the old method to make unit tests pass correctly.
If you want to see an example, go to test_initialize_game_print_board


| Required element                                                    |               File               |              Line number |
|:--------------------------------------------------------------------|:--------------------------------:|-------------------------:|
| a) use of immutable data structures like tuples                     |             enemy.py             | [L1](./main_game.py), #5 |
| b) use of mutable data structures like lists and dictionaries       |             cards.py             |                       #6 |
| c) thoughtful use of exceptions and exception handling              |           main_game.py           |                     #213 |
| d) minimized scope and lifetime of all variables and objects        |           main_game.py           |                     #380 |
| e) decomposition of your idea into small functions                  |           main_game.py           |                     #178 |
| f) simple flat code that is easy to understand                      |           main_game.py           |                     #588 |
| g) comprehensions work though correct use of one or more list/dicts |            relics.py             |                      #50 |
| h) selection using if-statements                                    |        initialize_game.py        |                 #70, #74 |
| i) repetition using the for-loop                                    |           main_game.py           |                #81, #187 |
| j) use of the membership operator where it makes sense              | initialize_game.py, main_game.py |                #70, #460 |
| k) appropriate use of the the range function                        |           main_game.py           |                #98, #187 |
| l) use of one or more functions from itertools                      |           main_game.py           |                     #111 |
| m) the random module                                                |            relics.py             |                 #47, #72 |
| n) function annotations                                             |             text.py              |                      #51 |
| o) doctests and/or unit tests for every single function             |        See all unit tests        |                          |
| p) output must be formatted using f-strings                         |    welp i ain't wanna do that    |                          |
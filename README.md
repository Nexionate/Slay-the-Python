Ethan O'Connor - Nexionate - A01435041

# **Slay the Python**

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

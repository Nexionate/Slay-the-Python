import sys
import time
from colorama import Fore, Back, Style, init
init(autoreset=True)
"""
Ethan O'Connor
A01435041
Set E
"""


def col(colour, word):
    """
    Generate coloured text

    :param colour: a non-empty string
    :param word: a non-empty string
    :precondition: colour is a string of a colour
    :precondition: word is a string
    :postcondition: the selected colour is applied to the word
    :postcondition: !colour applies the lighter selected colour to the word

    >>> col("!red", "a light red message")      # doctest: +SKIP
    >>> col("blue", "a blue message")      # doctest: +SKIP
    """
    colour_dict = {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,

        "@black": Back.BLACK,
        "@red": Back.RED,
        "@green": Back.GREEN,
        "@yellow": Back.YELLOW,
        "@blue": Back.BLUE,
        "@magenta": Back.MAGENTA,
        "@cyan": Back.CYAN,
        "@white": Back.WHITE,

        "!black": Fore.LIGHTBLACK_EX,
        "!red": Fore.LIGHTRED_EX,
        "!green": Fore.LIGHTGREEN_EX,
        "!yellow": Fore.LIGHTYELLOW_EX,
        "!blue": Fore.LIGHTBLUE_EX,
        "!white": Fore.LIGHTWHITE_EX,
        "!magenta": Fore.LIGHTMAGENTA_EX,
        "!cyan": Fore.LIGHTCYAN_EX,
        "reset": Style.RESET_ALL
    }
    try:
        colour_code = colour_dict.get(colour.lower(), Style.RESET_ALL)
    except KeyError:
        colour_code = Style.RESET_ALL

    return colour_code + word + Style.RESET_ALL


def lbl(sentence, delay=.1, colour=""):
    """
    Print a sentence letter by letter with a delay between each character.

    :param colour: a string of a colour
    :param sentence: The sentence to be printed.
    :param sentence: A non-empty string
    :param delay: a non-zero positive integer
    :postcondition: Print each letter with a delay between each character.
    """
    for char in sentence:
        sys.stdout.write(col(colour, char))  # Print the character without a newline
        sys.stdout.flush()  # Ensure it's immediately written to the terminal
        time.sleep(delay)  # Wait for the specified delay


CONST_HELP_TEXT = \
    "\n\n" + col("magenta", "Combat information:") + "" \
    "\n- To play a card, input its number order or full name. The yellow squares " + col("!yellow", "\u25A1") +" indicate your current energy." \
    "\n- You cannot play a card if you don't have sufficient energy. " \
    "\n- You will gain your Max Energy upon the end of the enemies turn." \
    "" \
    "\n- If you do not have enough energy to play your remaining cards, type" + col("magenta", " \"end\" ") + "to finish your turn" \
    "\n- The " + col("!cyan", chr(10683)) + " icon indicates how much damage will be blocked. " \
    "\n- " + col("!cyan", chr(10683) + " Block") + " wears off at the start of your next turn. " \
    "\n- Cards that " + col("!black", "exhaust") + " can only be used once per battle, and will return to your deck when complete. " \
    "\n- Example: a player with " + col("!cyan", "15 BLCK") + "\n" \
    f"{(col("green", "■") * 10)}  50/50{col("!green", " HP ")} {col("!cyan", chr(10683) + str(15))} {(col("!yellow", "□") * 3)} 3/3{col("!yellow", " energy")}\n"

CONST_MAP_HELP = \
    ("\n\nWelcome to this land. Your goal is to reach the boss at the " + col("red", "bottom-right tile of the board.") + ""\
    "\n\n\n" + col("magenta", "Map information:") + "" \
    "\nEvery board tile will contain an event. "\
    "\n" + col("!white", "- fights:") + " normal enemy battle with" + col("!yellow", " gold ") + "and card rewards"\
    "\n" + col("red", "- elites:") + " extra tough enemies that will drop powerful " + col("!magenta", "relics") + \
     " and more gold"\
    "\n" + col("blue", "- empty:") + " an empty area"\
    "\n" + col("magenta", "- shop:") + " spend your gold on relics and upgrades! Can only be visited once, so " \
            "plan around it!"\
    "\n" + col("yellow", "- fires:") + " allow the player to heal" + col("!white", " *OR*") + " permanently " \
                    "upgrade a card from your deck, making it more powerful"\
    "\nElites are completely optional, but will be very helpful in defeating the boss!"\
    "\n\n\n" + col("magenta", "Input information:") + "" \
    "\nType " + col("!white", "help") + " for this text to appear again"\
    "\nType " + col("!white", "relics") + " to view your current relics"\
    "\nType " + col("!white", "gold") + " to view your current gold"\
    "\n\n\n" + col("magenta", "Deck information:") + "" \
    "\nEvery battle, you will gain cards from your " + col("!green", "Draw pile") + " into your " + col("!yellow", "Hand") + ""\
    "\nAfter playing a card, it will go to the " + col("!red", "Discard pile") + ""\
    "\nAt the end of your turn, any remaining cards in your " + col("!yellow", "Hand") + " will go to the " + col("!red", "Discard pile") + ""\
    "\nOnce the " + col("!green", "Draw pile") + " is empty, your " + col("!red", "Discard pile") + " will be shuffled back into the " + col("!green", "Draw pile") + ""\
    "\n" + col("!green", "Draw pile") + " --> " + col("!yellow", "Hand") + " --> " + col("!red", "Discard pile") + "" \
    "\n\n\n" + col("magenta", "General tips:") + "" \
    "\n- first prioritize normal fights to get card rewards" \
    "\n- make sure to have a few good card rewards before fighting an " + col("red", "elite") + "" \
    "\n- upgrade your best cards when you have health to spare (above 30HP)" \
    "\n- visit the shop after an elite or once you have over 275 gold" \
    "\n- you will have access to one final campfire before the boss, so choose carefully") \

CONST_TUTORIAL_COMBAT = \
    "\n "


def print_shop_intro():
    """
    Print the intro of the shop

    :postcondition: Prints the intro of the shop for the player
    """
    print(col("magenta", chr(10870) * 8 + "SHOP" + chr(10870) * 8))
    lbl("hellllooooooOOooOOooo", 0.08, "!cyan")
    time.sleep(0.25)
    sys.stdout.write(col("!black", " a shopkeeper greets your rather obvious entrance"))
    time.sleep(1.5)
    sys.stdout.write("\r")
    lbl("I HAVE LOTS OF WARES FOR SALEEEEE", 0.08, "!cyan")
    time.sleep(0.5)
    sys.stdout.write("\r")
    lbl("PLEASE TAKE A LOOK", 0.08, "!cyan")
    time.sleep(0.25)
    sys.stdout.write(col("!black", " he seems harmless"))


def print_campfire(player):
    """
    Print the intro of the campfire

    :postcondition: Prints the intro of the campfire for the player
    :postcondition: if player is about to fight boss, print special message
    """
    from main_game import check_if_goal_attained
    print(col("!black", "You approach a small campfire, you know you are safe "))
    time.sleep(1.25)
    print("The " + col("yellow", "warmth of the fire") + " welcomes you ")
    time.sleep(1.25)
    if check_if_goal_attained(player, 5, 5):
        print(col("!black", "You know there's no turning back after this"))
        time.sleep(0.5)
    time.sleep(1.25)
    print("\nYou have the option to " + col("!green", "rest (recover 20HP)") + " or " + col("!blue",
                                                                                            "smith (upgrade a card)"))
    print(col("!black", "You currently have " + str(player["Current HP"]) + "/" + str(player["Max HP"]) + "HP"))

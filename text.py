from time import sleep

from colorama import Fore, Back, Style, init
init(autoreset=True)
import sys
import time


def col(colour, word):
    """
   Use !colour for the lighter version
   This makes anythign in word that colour and resets it to normal after
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
        "@r8ed": Back.RED,
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


def lbl(sentence, delay=1, colour=""):
    """
    Prints a sentence letter by letter with a delay between each character.

    :param sentence: The sentence to be printed.
    :param sentence: A string
    :param delay: The delay (in seconds) between printing each letter.
    """
    for char in sentence:
        sys.stdout.write(col(colour, char))  # Print the character without a newline
        sys.stdout.flush()  # Ensure it's immediately written to the terminal
        time.sleep(delay)  # Wait for the specified delay


CONST_HELP_TEXT = \
    "\n- To play a card, input its number order or full name. The yellow squares " + col("!yellow", "\u25A1") +" indicate your current energy." \
    "\n- You cannot play a card if you don't have sufficient energy. " \
    "\n- You will gain your Max Energy upon the end of the enemies turn." \
    "" \
    "\n- If you do not have enough energy to play your remaining cards, type" + col("magenta", " \"end\" ") + "to finish your turn" \
    "\n- The " + col("!cyan", chr(10683)) + " icon indicates how much damage will be blocked. " \
    "\n- " + col("!cyan", chr(10683) + " Block") + " wears off at the start of your next turn. " \
    "\n- Cards that " + col("!black", "exhaust") + " can only be used once per battle, and will return to your deck when complete. "

CONST_MAP_HELP = \
    "Welcome to this land. I will explain the map. Your goal is to reach the bottom-right tile of the board."\
    "\nEvery board tile will contain an event. "\
    "\n" + col("!white", "- fights:") + " normal enemy battle with" + col("!yellow", " gold ") + "and card rewards"\
    "\n" + col("red", "- elites:") + " extra tough enemies that will drop powerful " + col("!magenta", "relics") + " and more gold"\
    "\n" + col("blue", "- events:") + " a special event will play, who knows what will happen?"\
    "\n" + col("magenta", "- shop:") + " spend your gold on relics and upgrades! Can only be visited once, so plan around it!"\
    "\n" + col("yellow", "- fires:") + " allow the player to heal" + col("!white", " *OR*") + " permanently upgrade a card from your deck, making it more powerful"\
    "\nElites are completely optional, but will be very helpful in defeating the boss! \n"\
    "\nEvery battle, you will gain cards from your " + col("!green", "Draw pile") + " into your " + col("!yellow", "Hand") + ". After playing a card, it will go to the " + col("!red", "Discard pile") + ""\
    "\nAt the end of your turn, any remaining cards in your " + col("!yellow", "Hand") + " will go to the " + col("!red", "Discard pile") + ""\
    "\nOnce the " + col("!green", "Draw pile") + " is empty, your " + col("!red", "Discard pile") + " will be shuffled back into the " + col("!green", "Draw pile") + ""\
    "\n" + col("!green", "Draw pile") + " --> " + col("!yellow", "Hand") + " --> " + col("!red", "Discard pile") + ""\
    #"\nType " + col("!white", "help") + " for this text to appear again"\


def print_shop():
    print(" " * 4 + col("magenta", chr(10870) * 6 + "SHOP" + chr(10870) * 6))
    lbl("hellllooooooOOooOOooo", 0.08, "!cyan")
    time.sleep(0.25)
    sys.stdout.write(col("!black", " a shopkeeper greets your rather obvious entrance"))
    time.sleep(1.5)
    sys.stdout.write("\r")
    lbl("I HAVE LOTS OF WARES FOR SURE", 0.08, "!cyan")
    time.sleep(0.5)
    sys.stdout.write("\r")
    lbl("PLEASE TAKE A LOOK", 0.08, "!cyan")
    time.sleep(0.75)
    sys.stdout.write(col("!black", " he seems harmless"))


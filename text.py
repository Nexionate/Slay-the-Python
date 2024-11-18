from colorama import Fore, Back, Style, init
init(autoreset=True)


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
    colour_code = colour_dict.get(colour.lower(), Style.RESET_ALL)
    return colour_code + word + Style.RESET_ALL


CONST_HELP_TEXT = \
    "- To play a card, input its number order or full name. The yellow squares " + col("!yellow", "\u25A1") +" indicate your current energy." \
    "\n- You cannot play a card if you don't have sufficient energy. " \
    "\n- You will gain your Max Energy upon the end of the enemies turn." \
    "" \
    "\n- If you do not have enough energy to play your remaining cards, type" + col("magenta", " \"end\" ") + "to finish your turn" \
    "\n- The " + col("!cyan", chr(10683)) + " icon indicates how much damage will be blocked. " \
    "\n- " + col("!cyan", chr(10683) + " Block") + " wears off at the start of your next turn. " \
    "\n- Cards that " + col("!black", "exhaust") + " can only be used once per battle, and will return to your deck when complete. "

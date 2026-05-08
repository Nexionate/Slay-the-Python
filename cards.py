import random
from text import col
"""
Ethan O'Connor
A01435041
Set E
"""
yellow_square = col("!yellow", "\u25A1")
purple_square = col("magenta", "\u25A1")


def card_list(wanted):
    """
    A dictionary of all cards

    :param wanted: a non-empty string
    :precondition: wanted is a string of the wanted card
    :return: a dictionary of the wanted card

    >>> card_list("strike")
    {'name': 'strike', 'type': 'attack', "amount": {"damage": 6}, 'energy': 1, 'description': '6 DMG', \
'exhaust': False, 'upgrade': False}
    >>> card_list("defend")
    {'name': 'defend', 'type': 'block', "amount": {"block": 5}, 'energy': 1, 'description': '5 BLCK', \
'exhaust': False, 'upgrade': False}
    """
    card_dict = {
        "strike": {"name": "strike", "type": "attack", "amount": {"damage": 6}, "energy": 1, "description": "6 DMG",
                   "exhaust": False, "upgrade": False},
        "defend": {"name": "defend", "type": "block", "amount": {"block": 5}, "energy": 1, "description": "5 BLCK",
                   "exhaust": False, "upgrade": False},
        "bash": {"name": "bash", "type": "attack", "amount": {"damage": 9}, "energy": 2, "description": "9 DMG", "exhaust": False,
                 "upgrade": False},
        "bludgeon": {"name": "bludgeon", "type": "attack", "amount": {"damage": 18}, "energy": 2, "description": "18 DMG",
                     "exhaust": True, "upgrade": False},
        "iron wave": {"name": "iron wave", "type": "hybrid", "amount": {"damage": 5, "block": 5}, "energy": 1, "description": "5 DMG, 5 BLCK",
                      "exhaust": False, "upgrade": False},
        "anger": {"name": "anger", "type": "attack", "amount": {"damage": 7}, "energy": 0, "description": "7 DMG",
                  "exhaust": True, "upgrade": False},
        "barricade": {"name": "barricade", "type": "block", "amount": {"block": 12}, "energy": 2, "description": "12 BLCK",
                      "exhaust": False, "upgrade": False},
        "prepared": {"name": "prepared", "type": "other", "amount": {"draw": 3}, "energy": 0,
                      "description": f"{3*purple_square} DRAW",
                      "exhaust": False, "upgrade": False},
        "blood letting": {"name": "blood letting", "type": "other", "amount": {"draw": 3, "energy": 2, "HP loss": 5}, "energy": 0, "description": f"{3*purple_square} DRAW {2*yellow_square} ENERGY {col("!red", "-5HP")}",
                      "exhaust": True, "upgrade": False}
    }
    try:
        card = card_dict.get(wanted)

    except KeyError:
        print("card not found")
    else:
        return card


def card_list_upgraded(wanted):
    """
    A dictionary of all upgraded cards

    :param wanted: a non-empty string
    :precondition: wanted is a string of the wanted card
    :return: a dictionary of the upgraded wanted card
    >>> card_list_upgraded("strike")
    {'name': 'strike+', 'type': 'attack', "amount": {"damage": 9}, 'energy': 1, 'description': '9 DMG', \
'exhaust': False, 'upgrade': True}
    >>> card_list_upgraded("defend")
    {'name': 'defend+', 'type': 'block', "amount": {"block": 8}, 'energy': 1, 'description': '8 BLCK', \
'exhaust': False, 'upgrade': True}
    """
    card_dict_upgraded = {
        "strike": {"name": "strike+", "type": "attack", "amount": {"damage": 9}, "energy": 1, "description": "9 DMG",
                   "exhaust": False, "upgrade": True},
        "defend": {"name": "defend+", "type": "block", "amount": {"block": 8}, "energy": 1, "description": "8 BLCK",
                   "exhaust": False, "upgrade": True},
        "bash": {"name": "bash+", "type": "attack", "amount": {"damage": 13}, "energy": 1, "description": "13 DMG",
                 "exhaust": False, "upgrade": True},
        "bludgeon": {"name": "bludgeon+", "type": "attack", "amount": {"damage": 25}, "energy": 2, "description": "25 DMG",
                     "exhaust": True, "upgrade": True},
        "iron wave": {"name": "iron wave+", "type": "hybrid", "amount": {"damage": 7, "block": 7}, "energy": 1, "description": "7 DMG, 7 BLCK",
                      "exhaust": False, "upgrade": True},
        "anger": {"name": "anger+", "type": "attack", "amount": {"damage": 9}, "energy": 0, "description": "9 DMG",
                  "exhaust": False, "upgrade": True},
        "barricade": {"name": "barricade+", "type": "block", "amount": {"block": 17}, "energy": 2, "description": "17 BLCK",
                      "exhaust": False, "upgrade": True},
        "prepared": {"name": "prepared+", "type": "other", "amount": {"draw": 4}, "energy": 0,
                     "description": f"{4 * purple_square} DRAW",
                     "exhaust": False, "upgrade": False},
        "blood letting": {"name": "blood letting+", "type": "other", "amount": {"draw": 3, "energy": 3, "HP loss": 3},
                          "energy": 0, "description": f"{3*purple_square} DRAW {3*yellow_square} ENERGY {col("!red", "-3HP")}",
                          "exhaust": True, "upgrade": True}
    }
    try:
        card = card_dict_upgraded.get(wanted)
    except KeyError:
        print("card not found")
    else:
        return card


# only used in the final boss fight
def debuff_card_list():
    """
    Return a dictionary of the debuff card

    :return: a dictionary of the debuff cards stats
    """
    return {"name": "burn", "type": "debuff", "amount": {"HP loss": 3}, "energy": 1,
            "description": col("red", "2 SELF DMG") + col("!black", "( if in hand by end of turn)"),
            "exhaust": True}


def random_card_reward():
    """
    Generate a random card reward

    :postcondition: a random card is selected
    :return: a dictionary of a card

    >>> random_card_reward()    # doctest: +SKIP
    {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False}
    >>> random_card_reward()    # doctest: +SKIP
    {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                      "exhaust": True, "upgrade": False}
    """
    card_reward_random = ["strike", "defend", "bash", "bludgeon", "iron wave", "anger", "barricade", "prepared"]

    option = card_list(random.choice(card_reward_random))
    return option


def add_new_card(deck, option):
    """
    Append a card to the deck

    :param deck: a list of cards
    :param option: a dictionary of a card
    :postcondition: the card option is appended to the deck
    """
    deck.append(option)


def show_deck_upgrade(hand):
    """
    Display all available card upgrades in the deck

    :param hand: a list of cards
    :precondition: hand is a list containing dictionaries of cards stats
    :postcondition: all cards and their upgraded stats are displayed to the player

    >>> show_deck_upgrade([{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False}]) # doctest: +SKIP
    1) strike □ - 6 DMG          --->        strike+ □ - 9 DMG
    """
    for counter in range(len(hand)):
        card = hand[counter]
        exhaust_print = ""
        exhaust_upgrade_print = ""
        if card["exhaust"]:
            exhaust_print = col("!black", "exhausts")
        yellow_square = col("!yellow", "\u25A1")

        upgraded_card = card_list_upgraded(card["name"])
        if upgraded_card["exhaust"]:
            exhaust_upgrade_print = col("!black", "exhausts")

        normal_card_print = str(counter + 1) + ") " + str(card["name"]) + " " + str(
            card["energy"] * yellow_square) + " - " + str(card["description"]) + " " + exhaust_print
        
        upgraded_card_print = str(upgraded_card["name"]) + " " + str(
            upgraded_card["energy"] * yellow_square) + " - " + str(
            upgraded_card["description"]) + " " + exhaust_upgrade_print

        print(normal_card_print + col("!black", "         --->        ") + upgraded_card_print)


def upgrade_card_list(deck):
    """
    Determine all cards in the deck that are not upgraded

    :param deck: a list of cards
    :postcondition: all non-upgraded cards in the deck are printed

    >>> upgrade_card_list([{'name': 'strike', 'upgrade': False}])
    [{'name': 'strike', 'upgrade': False}]
    >>> upgrade_card_list([{'name': 'strike', 'upgrade': True}, {'name': 'defend', 'upgrade': False}])
    [{'name': 'defend', 'upgrade': False}]
    """
    return [card for card in deck if not card["upgrade"]]


def add_upgrade_card(deck, card):
    """
    Add an upgraded card to the deck

    :param deck: a list of cards
    :param card: a dictionary of a cards stats
    :postcondition: the old card is removed from the deck
    :postcondition: the new upgraded card is added to the deck

    >>> add_upgrade_card([{"name": "strike"}], {"name": "defend"}) # doctest: +SKIP
    >>> add_upgrade_card([], {"name": "bash"}) # doctest: +SKIP
    """
    upgraded_card = card_list_upgraded(card["name"])
    deck.remove(card)
    deck.append(upgraded_card)

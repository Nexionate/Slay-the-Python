import random
from text import col


def card_list(wanted):
    """
    A dictionary of all cards

    :param wanted: a non-empty string
    :precondition: wanted is a string of the wanted card
    :return: a dictionary of the wanted card

    >>> card_list("strike")
    {'name': 'strike', 'type': 'attack', 'amount': 6, 'energy': 1, 'description': '6 DMG', \
'exhaust': False, 'upgrade': False}
    >>> card_list("defend")
    {'name': 'defend', 'type': 'block', 'amount': 5, 'energy': 1, 'description': '5 BLCK', \
'exhaust': False, 'upgrade': False}
    """
    card_dict = {
        "strike": {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG",
                   "exhaust": False, "upgrade": False},
        "defend": {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK",
                   "exhaust": False, "upgrade": False},
        "bash": {"name": "bash", "type": "attack", "amount": 9, "energy": 2, "description": "9 DMG", "exhaust": False,
                 "upgrade": False},
        "bludgeon": {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG",
                     "exhaust": True, "upgrade": False},
        "iron wave": {"name": "iron wave", "type": "hybrid", "amount": 5, "energy": 1, "description": "5 DMG, 5 BLCK",
                      "exhaust": False, "upgrade": False},
        "anger": {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                  "exhaust": True, "upgrade": False},
        "barricade": {"name": "barricade", "type": "block", "amount": 12, "energy": 2, "description": "12 BLCK",
                      "exhaust": False, "upgrade": False},
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
    {'name': 'strike+', 'type': 'attack', 'amount': 9, 'energy': 1, 'description': '9 DMG', \
'exhaust': False, 'upgrade': True}
    >>> card_list_upgraded("defend")
    {'name': 'defend+', 'type': 'block', 'amount': 8, 'energy': 1, 'description': '8 BLCK', \
'exhaust': False, 'upgrade': True}
    """
    card_dict_upgraded = {
        "strike": {"name": "strike+", "type": "attack", "amount": 9, "energy": 1, "description": "9 DMG",
                   "exhaust": False, "upgrade": True},
        "defend": {"name": "defend+", "type": "block", "amount": 8, "energy": 1, "description": "8 BLCK",
                   "exhaust": False, "upgrade": True},
        "bash": {"name": "bash+", "type": "attack", "amount": 13, "energy": 1, "description": "13 DMG",
                 "exhaust": False, "upgrade": True},
        "bludgeon": {"name": "bludgeon+", "type": "attack", "amount": 25, "energy": 2, "description": "25 DMG",
                     "exhaust": True, "upgrade": True},
        "iron wave": {"name": "iron wave+", "type": "hybrid", "amount": 7, "energy": 1, "description": "7 DMG, 7 BLCK",
                      "exhaust": False, "upgrade": True},
        "anger": {"name": "anger+", "type": "attack", "amount": 9, "energy": 0, "description": "9 DMG",
                  "exhaust": False, "upgrade": True},
        "barricade": {"name": "barricade+", "type": "block", "amount": 16, "energy": 2, "description": "16 BLCK",
                      "exhaust": False, "upgrade": False},
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
    return {"name": "burn", "type": "debuff", "amount": 2, "energy": 1,
            "description": col("red", "2 SELF DMG") + col("!black", "( if in hand by end of turn)"),
            "exhaust": True}


def random_card_reward():
    """
    Generate a random card reward

    :postcondition: a random card is selected
    :return: a dictionary of a card

    #>>> random_card_reward()    # doctest: +SKIP
    {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False}
    #>>> random_card_reward()    # doctest: +SKIP
    {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                      "exhaust": True, "upgrade": False}
    """
    card_reward_random = ["strike", "defend", "bash", "bludgeon", "iron wave", "anger", "barricade"]

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

    #>>> show_deck_upgrade([{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False}]) # doctest: +SKIP
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

    #>>> upgrade_card_list([{'name': 'strike', 'upgrade': False}])
    [{'name': 'strike', 'upgrade': False}]
    #>>> upgrade_card_list([{'name': 'strike', 'upgrade': True}, {'name': 'defend', 'upgrade': False}])
    [{'name': 'defend', 'upgrade': False}]
    """
    upgrade_list = []
    for card in deck:
        if not card["upgrade"]:
            upgrade_list.append(card)

    # show_deck_upgrade(upgrade_list)
    return upgrade_list


def add_upgrade_card(deck, card):
    """
    Add an upgraded card to the deck

    :param deck: a list of cards
    :param card: a dictionary of a cards stats
    :postcondition: the old card is removed from the deck
    :postcondition: the new upgraded card is added to the deck

    #>>> add_upgrade_card([{"name": "strike"}], {"name": "defend"}) # doctest: +SKIP
    #>>> add_upgrade_card([], {"name": "bash"}) # doctest: +SKIP
    """
    upgraded_card = card_list_upgraded(card["name"])
    deck.remove(card)
    deck.append(upgraded_card)

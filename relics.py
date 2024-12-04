import random
from text import col

"""
Ethan O'Connor
A01435041
Set E
"""

# I couldn't update this in time to make a function and fix all problems with turning into function
# I beg for mercy Chris
CONST_RELIC_POOL = [
    {"name": 'strike dummy', "description": 'adds +3 DMG to all strikes', "effect": 3, "one-time": False,
     "rarity": "uncommon"},

    {"name": 'oddly smooth stone', "description": 'adds +1 to all block', "effect": 1, "one-time": False,
     "rarity": "common"},

    {"name": 'regal pillow', "description": 'resting at campfires completely heals you ', "effect": 60,
     "one-time": False, "rarity": "common"},

    {"name": 'blood vial', "description": 'heal 3HP before every battle', "effect": 3, "one-time": False,
     "rarity": "common"},

    {"name": 'old coin', "description": 'immediately gain 300 gold', "effect": 300, "one-time": True,
     "rarity": "uncommon"},

    {"name": 'strawberry', "description": 'gain 10 Max HP', "effect": 10, "one-time": True, "rarity": "common"},

    {"name": 'prepared slug', "description": 'gain 8 block the first turn of combat', "effect": 8, "one-time": False,
     "rarity": "uncommon"}, ]

CONST_SHOP_RELIC_POOL = [
    {"name": 'coffee dripper', "description": 'permanently gain +1 Max Energy', "effect": 1, "one-time": True,
     "rarity": "rare"},
    {"name": 'philosophers stone', "description": 'permanently gain +1 Max Energy', "effect": 1, "one-time": True,
     "rarity": "rare"}]


def get_relic():
    """
    Retrieve a random relic

    :postcondition: a relic is randomly chosen
    :return: a dictionary of a relic's stats

    >>> relic_list = [{"name": 'prepared slug', "description": 'gain 8 block the first turn of combat', \
    "effect": 8, "one-time": False, "rarity": "uncommon"}]      # doctest: +SKIP
    >>> get_relic()         # doctest: +SKIP
    {"name": 'prepared slug', "description": 'gain 8 block the first turn of combat', \
    "effect": 8, "one-time": False, "rarity": "uncommon"}
    >>> relic_list = []  # doctest: +SKIP
    >>> get_relic()  # doctest: +SKIP
    congrats, you made me run out of relics
    """
    try:
        return CONST_RELIC_POOL.pop(0)
    except IndexError:
        print("congrats, you made me run out of relics")


def return_relic(relic):
    """
    Return a random relic back to the pool

    :param relic: a dictionary of a relic's stats'
    :postcondition: the relic is appended to the pool
    """
    CONST_RELIC_POOL.append(relic)


def create_relics():
    """
    Shuffle the relic pool

    :postcondition: the relic pool is shuffled
    """

    random.shuffle(CONST_RELIC_POOL)


def print_shop_relics(shop_list):
    """
    Print the available shop relics

    :param shop_list: a non-empty list
    :precondition: shop_list is a non-empty list
    :precondition: shop_list contains a list of dictionaries of relic stats
    :postcondition: the available relics are printed
    >>> a_shop_list = [({"name": 'regal pillow', "description": "resting at campfires completely heals you", "effect": 60,\
                       "one-time": False, "rarity": "common"}, 143), \
                       ({"name": 'oddly smooth stone', "description": 'adds +1 to all block', "effect": 1, \
                       "one-time": False, "rarity": "common"}, 165)]        # doctest: +SKIP
    >>> print_shop_relics(a_shop_list)                                      # doctest: +SKIP
    1) regal pillow - 143 gold
    - resting at campfires completely heals you
    <BLANKLINE>
    2) oddly smooth stone - 165 gold
    - adds +1 to all block
    <BLANKLINE>
     >>> a_shop_list = [({"name": 'regal pillow', "description": "resting at campfires completely heals you", "effect": 60,\
                       "one-time": False, "rarity": "common"}, 143)]        # doctest: +SKIP
    >>> print_shop_relics(a_shop_list)                                      # doctest: +SKIP
    1) regal pillow - 143 gold
    - resting at campfires completely heals you
    <BLANKLINE>
    """
    for counter in range(len(shop_list)):
        relic_counter = shop_list[counter]
        relic = relic_counter[0]
        cost = relic_counter[1]

        print(
            str(counter + 1) + ") " + col("!magenta", str(relic['name'])) + " - " + col("yellow", str(cost) + " gold"))
        print(col("magenta", "- " + (relic['description'])) + "\n")


def shop_relic():
    """
    Generate the shop relics

    Generates three relics plus a shop relic for the player to purchase
    :postcondition: three random relics are generated
    :postcondition: one special relic is chosen
    :postcondition: the relic "old coin" cannot be in the shop
    :postcondition: each relic has a price generated
    :return: a list of all shop relics

    >>> shop_relic()         # doctest: +SKIP
    [({"name": 'strike dummy', "description": 'adds +3 DMG to all strikes',
      "effect": 3, "one-time": False, "rarity": "uncommon"}, 175),
     ({"name": 'oddly smooth stone', "description": 'adds +1 to all block',
       "effect": 1, "one-time": False, "rarity": "common"}, 165),
     ({"name": 'regal pillow', "description": 'resting at campfires completely heals you ',
       "effect": 60,
       "one-time": False, "rarity": "common"}, 143),
     ({"name": 'coffee dripper', "description": 'permanently gain +1 Max Energy', "effect": 1,
       "one-time": True,
       "rarity": "rare"}, 275)]
    >>> shop_relic()         # doctest: +SKIP
    [({"name": 'blood vial', "description": 'heal 3HP before every battle', "effect": 3, "one-time": False,
     "rarity": "common"}, 151),
     ({"name": 'strawberry', "description": 'gain 10 Max HP', "effect": 10, "one-time": True, "rarity": "common"}, 145),
     ({"name": 'oddly smooth stone', "description": 'adds +1 to all block',
       "effect": 1, "one-time": False, "rarity": "common"}, 149),
     ({"name": 'philosophers stone', "description": 'permanently gain +1 Max Energy', "effect": 1, "one-time": True,
     "rarity": "rare"}, 275)]
    """
    print("")

    shop_list = []
    for counter in range(3):
        load_relic = get_relic()

        if load_relic["name"] == "old coin":  # no point in selling a relic that gives you more money
            return_relic(load_relic)
            load_relic = get_relic()

        if load_relic["rarity"] == "common":
            gold_price = random.randint(140, 160)
        elif load_relic["rarity"] == "uncommon":
            gold_price = random.randint(190, 220)
        else:
            gold_price = random.randint(250, 280)
        relic_dict = (load_relic, gold_price)

        shop_list.append(relic_dict)
    shop_list.append((random.choice(CONST_SHOP_RELIC_POOL), 275))

    # print_shop_relics(shop_list)
    return shop_list


def print_relic_description(relic):
    """
    Print the description of a relic

    :param relic: a dictionary
    :precondition: relic is a dictionary of a relic's stats
    :postcondition: the relic description is printed
    :postcondition: relics with the effect "one-time" have their effect printed

    >>> a_relic = {"name": 'old coin', "description": 'immediately gain 300 gold', "effect": 300, \
    "one-time": True, "rarity": "uncommon"}     # doctest: +SKIP
    >>> print_relic_description(a_relic)        # doctest: +SKIP
    old coin 300
    - immediately gain 300 gold

    >>> a_relic = {"name": 'strike dummy', "description": 'adds +3 DMG to all strikes', \
                      "effect": 3, "one-time": False, "rarity": "uncommon"}     # doctest: +SKIP
    >>> print_relic_description(a_relic)                                        # doctest: +SKIP
    strike dummy
    - adds +3 DMG to all strikes
    """
    if relic["one-time"]:
        print(col("!magenta", str(relic['name'])) + " " + col("!black", str(relic['effect'])))
    else:
        print(col("!magenta", str(relic['name'])))
    print(col("magenta", "- " + str(relic['description'])))


def relic_one_time_buff(relic, player):
    """
    Apply a one-time relic buff
    :param relic: a dictionary containing the relics stats
    :param player: a dictionary containing the players stats
    :precondition: relic is a dictionary of a relic's stats
    :precondition: player is a well-formed dictionary containing the player stats
    :postcondition: the relics effect is permanently applied to the players stats
    :postcondition: the relics effect is updated

    >>> a_relic = {"name": 'old coin', "description": 'immediately gain 300 gold', "effect": 300, \
    "one-time": True, "rarity": "uncommon"}
    >>> relic_one_time_buff(a_relic, {"Gold": 0, "Max HP": 50})

    >>> a_relic = {"name": 'prepared slug', "description": 'gain 8 block the first turn of combat',\
    "effect": 8, "one-time": False, "rarity": "uncommon"}
    >>> relic_one_time_buff(a_relic, {"Gold": 0, "Max HP": 50})
    """
    if relic['one-time']:
        if relic['name'] == "old coin":
            player["Gold"] += 300
            relic["effect"] = "This relic has been used up"

        elif relic['name'] == "strawberry":
            player["Current HP"] += 10
            player["Max HP"] += 10
            relic["effect"] = "This relic has been used up"

        elif relic['name'] == "coffee dripper":
            player["Max Energy"] += 1
            relic["effect"] = "This relic has been used up"

        elif relic['name'] == "philosophers stone":
            player["Max Draw"] += 2
            relic["effect"] = "This relic has been used up"


def purchase_relic(relic, player):
    """
    Purchase a relic

    :param relic: a list
    :param player: a dictionary containing the players stats
    :precondition: relic is a list containing a dictionary of a relic's stats and the cost
    :precondition: player is a well-formed dictionary containing the player stats
    :postcondition: the players gold is decreased by the relics cost
    :postcondition: the relic is appended to the players stats
    :return: True if the relic is purchased, False otherwise

    >>> a_relic = [{"name": 'old coin', "description": 'immediately gain 300 gold', "effect": 200, \
    "one-time": True, "rarity": "uncommon"}, 150]   # doctest: +SKIP
    >>> purchase_relic(a_relic, {"Gold": 200, "Max HP": 50})    # doctest: +SKIP
    """
    cost = relic[1]
    if player["Gold"] >= cost:
        player["Gold"] -= cost
        player["Relics"].append(relic[0])
        relic_one_time_buff(relic[0], player)  # check if relic is one time use after purchase
        return True
    else:
        return False

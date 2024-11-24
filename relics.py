import random
from text import col

CONST_RELIC_POOL = [
    {"name": 'strike dummy',
    "description": 'adds +3 DMG to all cards with the (strike) keyword',
    "effect": 3, "one-time": False},

    {"name": 'oddly smooth stone',
    "description": 'adds +1 to all block',
    "effect": 1, "one-time": False},

    {"name": 'black belt',
    "description": '15% change to dodge incoming attacks',
    "effect": 0.85, "one-time": False},

    {"name": 'blood vial',
    "description": 'heal 4HP after every battle',
    "effect": 3, "one-time": False},

    {"name": 'old coin',
    "description": 'immediately gain 200 gold',
    "effect": 200, "one-time": True},

    {"name": 'strawberry',
    "description": 'gain 10 Max HP',
    "effect": 10, "one-time": True},

    {"name": 'prepared slug',
    "description": 'gain 8 block the first turn of combat',
    "effect": 8},
]


def get_relic():
    return CONST_RELIC_POOL.pop(0)


def return_relic(relic):
    CONST_RELIC_POOL.append(relic)


def create_relics():
    random.shuffle(CONST_RELIC_POOL)


def shop_relic():
    # shop_list = []
    #for counter in range(3):
        #shop_list.append(get_relic())
    #return shop_list
    pass


def print_relic_description(relic):
    print("Relic: " + col("!magenta", (relic['name'])))
    print(col("magenta", "- " + (relic['description'])))
    return



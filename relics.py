import random
from text import col

CONST_RELIC_POOL = [
    {"name": 'strike dummy',
    "description": 'adds +3 DMG to all cards with the (strike) keyword',
    "effect": 3, "one-time": False, "rarity": "uncommon"},

    {"name": 'oddly smooth stone',
    "description": 'adds +1 to all block',
    "effect": 1, "one-time": False, "rarity": "common"},

    {"name": 'black belt',
    "description": '15% change to dodge incoming attacks',
    "effect": 0.85, "one-time": False, "rarity": "common"},

    {"name": 'blood vial',
    "description": 'heal 4HP before every battle',
    "effect": 4, "one-time": False, "rarity": "common"},

    {"name": 'old coin',
    "description": 'immediately gain 200 gold',
    "effect": 200, "one-time": True, "rarity": "uncommon"},

    {"name": 'strawberry',
    "description": 'gain 10 Max HP',
    "effect": 10, "one-time": True, "rarity": "common"},

    {"name": 'prepared slug',
    "description": 'gain 8 block the first turn of combat',
    "effect": 8, "one-time": False, "rarity": "uncommon"},
]
CONST_SHOP_RELIC_POOL = [
    {"name": 'coffee dripper', "description": 'permanently gain +1 Max Energy', "effect": 1, "one-time": True, "rarity": "rare"},
    {"name": 'philosophers stone', "description": 'permanently gain +1 Max Energy', "effect": 1, "one-time": True, "rarity": "rare"}
]

def get_relic():
    return CONST_RELIC_POOL.pop(0)


def return_relic(relic):
    CONST_RELIC_POOL.append(relic)


def create_relics():
    random.shuffle(CONST_RELIC_POOL)


def print_shop_relics(shop_list):
    for counter in range(len(shop_list)):
        relic_counter = shop_list[counter]
        relic = relic_counter[0]
        cost = relic_counter[1]

        print(str(counter+1) + ") " + col("!magenta", str(relic['name'])) + " - " + col("yellow", str(cost) + " gold"))
        print(col("magenta", "- " + (relic['description'])) + "\n")


def shop_relic():
    print("")
    gold_price = []
    shop_list = []
    for counter in range(3):
        load_relic = get_relic()

        if load_relic["name"] == "old coin":
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

    #print_shop_relics(shop_list)
    return shop_list


def print_relic_description(relic):
    if relic["one-time"]:
        print(col("!magenta", str(relic['name'])) + " " + col("!black", str(relic['effect'])))
    else:
        print(col("!magenta", str(relic['name'])))
    print(col("magenta", "- " + str(relic['description'])))


def relic_one_time_buff(relic, player):
    if relic['one-time']:
        if relic['name'] == "old coin":
            player["Gold"] += 200
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
    cost = relic[1]
    if player["Gold"] >= cost:
        player["Gold"] -= cost
        player["Relics"].append(relic[0])
        relic_one_time_buff(relic[0], player)           # check if relic is one time use after purchase
        return True
    else:
        return False

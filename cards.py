import random
def card_list(wanted):
    card_dict = {
    "strike" : {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False},
    "defend" : {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False},
    "bash" : {"name": "bash", "type": "attack", "amount": 9, "energy": 2, "description": "9 DMG", "exhaust": False},
    "bludgeon" : {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG", "exhaust": True},

    }
    card = card_dict.get(wanted)
    return card


def present_card_reward():
    card_reward_random = ["strike", "defend", "bash", "bludgeon"]

    option = card_list(random.choice(card_reward_random))
    return option

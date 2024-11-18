from colorama import Fore, Back, Style, init
init(autoreset=True)
import random
import time
import relics

import text
import enemy
from relics import get_relic
from relics import create_relics
from cards import card_list
from cards import present_card_reward
from text import col


def card_details(hand):
    for counter in range(len(hand)):
        card = hand[counter]
        for key in card.keys():
            print(str(key) + ": " + str(card[key]))
        print("\n")


def show_cards(hand):
    for counter in range(len(hand)):
        card = hand[counter]
        exhaust_print = ""
        if card["exhaust"] == True:
            exhaust_print =  col("!black", "exhausts")
        yellow_square = col("!yellow", "\u25A1")
        print(str(card["name"]) + " " + str(card["energy"] * yellow_square)  + " - " + str(card["description"]) + " " + exhaust_print)
        # print(str(card["name"]))


def print_player_stats(entity):
    health = entity["Current HP"]
    max_health = entity["Max HP"]
    energy = entity["Current Energy"]
    max_energy = entity["Max Energy"]
    block = entity["Block"]
    block_icon = ""

    squares = health // (max_health // 10)

    green_square = col("green", "\u25A0")
    red_square = col("red", "\u25A0")
    yellow_square = col("!yellow", "\u25A1")
    if block > 0:
        block_icon = col("!cyan", chr(10683) + str(block))


    print((green_square * squares) + (red_square * (10 - squares)) + "  " + (str(health) + "/" + str(max_health) + \
       "  " + block_icon +
       "  " + (energy  * yellow_square ) + " " + (str(energy) + "/" + str(max_energy))))



def draw_hand(draw_pile, hand, discard_pile, amount):
    for count in range(amount):
        if not draw_pile:
            draw_pile.extend(discard_pile)
            discard_pile = []
            random.shuffle(draw_pile)
        hand.append(draw_pile.pop(0))

    return draw_pile, hand, discard_pile


def get_player_input(hand, player, currentEnemy, discard_pile):
    action = input("Enter your action: ")
    action = action.lower()
    move_found = False
    move = ""
    action_index = 0

    if len(action) == 1 and ord(action) in range(49, len(hand) + 49):
        action = int(action)
        move = hand[action - 1]
        action_index = action - 1
        move_found = True

    if not move_found:
        if action == "help":
            print(text.CONST_HELP_TEXT)
        elif action == "end":
            end_player_turn(player, hand, discard_pile)
            player["Current Energy"] = 0
        else:
            for index, item in enumerate(hand):
                if item["name"] == action:
                    move = item
                    action_index = index
                    move_found = True
                    break
    if not move_found:
        if not (action == "help" or action == "end"):
            print("Action not found")

    return move, move_found, action_index


def apply_player_action(player, currentEnemy, enemyIntent ,action, hand, discard_pile, action_index):
    player["Current Energy"] -= action["energy"]
    action_type = action["type"]
    enemyBLCK = currentEnemy["current block"]
    damage = action["amount"]

    if action_type == "block":
        player["Block"] += action["amount"]

    elif action_type == "attack":
        calculated_damage = damage - enemyBLCK
        if calculated_damage <= 0:
            currentEnemy["current block"] -= damage
        elif calculated_damage > 0:
            currentEnemy["current block"] = 0
            currentEnemy["current HP"] -= calculated_damage
    if action["exhaust"] == False:
        discard_pile.append(hand[action_index])
    hand.remove(hand[action_index])

    if player["Current Energy"] == 0:
        end_player_turn(player, hand, discard_pile)


def apply_enemy_action(enemyIntent, currentEnemy, player):
    damage = enemyIntent["damage"]
    block = enemyIntent["block"]
    playerBLCK = player["Block"]

    if damage > 0:
        calculated_damage = damage - playerBLCK
        if calculated_damage <= 0:
            player["Block"] -= damage
        elif calculated_damage > 0:
            player["Block"] = 0
            player["Current HP"] -= calculated_damage
            print("The " + currentEnemy["name"] + " hits you for " + col("!red", str(calculated_damage) + " DMG"))
        time.sleep(1)
    if block > 0:
        currentEnemy["current block"] += block
        print("The " + currentEnemy["name"] + " defends for " + col("cyan", " " + chr(10683) + str(block) + " BLCK"))
        time.sleep(1)
    print(col("!black", "The enemy's turn ends.. \n"))
    time.sleep(1)



def check_energy(energy, card):
    energy_needed = card["energy"]
    requirement = energy >= energy_needed
    if not requirement:
        print(col("!black", "Insufficient Energy!"))
    return requirement


def end_player_turn(player, hand, discard_pile):
    for counter in range(len(hand)):
        discard_pile.append(hand[0])
        hand.remove(hand[0])


def spawn_shop():
    pass



def print_enemy_intent(currentEnemy, enemyIntent):
    message = ""
    between = 0
    block = currentEnemy["current block"]
    block_icon = ""
    if block > 0:
        block_icon = col("cyan", " " + chr(10683) + str(block))

    enemyIntentDMG = col("red", str(enemyIntent["damage"]) + " DMG" )
    enemyIntentBLCK = col("!blue", str(enemyIntent["block"]) + " BLCK")
    enemyIntentHP = col("green", ("(" + str(currentEnemy["current HP"]) + "/" + str(currentEnemy["max HP"])) + ")")

    if enemyIntent["block"] == 0 and enemyIntent["damage"] == 0:
        message += col("magenta", "UNKNOWN")
    else:
        if enemyIntent["damage"] != 0:
            message += "attack for " + enemyIntentDMG
            between = 1         # adds "and" inbetween
        if enemyIntent["block"] != 0:
            if between == 1:
                message += " and "
            message += "defend for " + enemyIntentBLCK

    print("The " + currentEnemy["name"] + enemyIntentHP + block_icon + " intends to " + message + "\n")


def initialize_combat(enemy, deck):
    player_turn = 0
    currentEnemy = enemy
    random.shuffle(deck)
    discard_pile = []
    hand = []
    draw_pile = deck
    return player_turn, hand, discard_pile, draw_pile, currentEnemy


def start_combat(player, enemy, deck):
    """
    Drive the combat
    """
    player_turn, hand, discard_pile, draw_pile, currentEnemy = initialize_combat(enemy, deck)

    while currentEnemy["current HP"] > 0:
        player["Block"] = 0
        player["Current Energy"] = player["Max Energy"]

        enemyIntent = random.choice(currentEnemy["attack"])


        draw_hand(draw_pile, hand, discard_pile, 3)     # change 3 to edit cards drawn
        print(col("!black", "Your turn begins.. "))
        time.sleep(0.75)

        while player["Current Energy"] > 0 and currentEnemy["current HP"] > 0:     # begin players turn
            # checks for enemy HP again to immediatley end players turn
            print_enemy_intent(currentEnemy, enemyIntent)
            show_cards(hand)
            print_player_stats(player)

            action, valid_input, action_index = get_player_input(hand, player, currentEnemy, discard_pile)

            if valid_input:
                valid_energy = check_energy(player["Current Energy"], action)
                if valid_energy:
                    apply_player_action(player, currentEnemy, enemyIntent, action, hand, discard_pile, action_index)

        if currentEnemy["current HP"] > 0:
            currentEnemy["current block"] = 0
            apply_enemy_action(enemyIntent, currentEnemy, player)



def reward_player(player, reward):
    print ( "\n" + col("magenta", chr(10870) * 3 + "LOOT" + chr(10870) * 3))

    gold_reward = random.randint(15, 25) * reward
    player["Gold"] += gold_reward
    print("Got " + col("yellow", str(player["Gold"] )+ " Gold") +  " " + col("!black", "+" + str(gold_reward)))

    loot_relic = get_relic()
    #print(loot_relic)
    print("Got " + col("!magenta", (loot_relic['name']) + "!"))
    print(col("magenta", "- " + (loot_relic['description'])))
    card_option = present_card_reward()
    print(col("magenta", card_option))




def create_deck():
    deck = []
    card_strike = card_list("strike")
    card_defend = card_list("defend")


    for i in range(3):
        deck.append(card_strike)
        deck.append(card_defend)

    deck.append(card_list("bash"))
    deck.append(card_list("bludgeon"))
    return deck




def main():

    # deck = [bash, bludgeon]
    deck = create_deck()
    rooms = 0
    create_relics()

    random.shuffle(deck)

    player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, \
              "Current Energy": 3, "Block": 0, "Gold": 50, "Relics": []}
    if rooms < 3:
        enemyDiffuculty = random.choice(enemy.enemies_easy)
        reward = 1

    start_combat(player, enemyDiffuculty, deck)
    reward_player(player, reward)



if __name__ == '__main__':
    main()

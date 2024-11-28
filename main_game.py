from colorama import Fore, Back, Style, init
init(autoreset=True)
import random
import time
import relics
import copy
import cards
import text
import enemy
from events import decide_event
from text import lbl, CONST_MAP_HELP
from relics import print_shop_relics
from relics import relic_one_time_buff
from relics import print_relic_description
from text import print_shop_intro
from relics import return_relic
from relics import shop_relic
from relics import get_relic
from relics import create_relics
from relics import purchase_relic
from cards import add_upgrade_card
from cards import upgrade_card_list
from cards import card_list
from cards import add_new_card
from cards import random_card_reward
from text import col
from text import print_campfire
from initialize_game import initialize_game_start
from initialize_game import print_board


def card_details(card):
    for key in card.keys():
        print(str(key) + ": " + str(card[key]))
    print("")


def print_player_relics(player):
    """
    Print the player's current relics

    :param player: a dictionary of the player
    :precondition: player is a well-defined dictionary containing the player's stats
    :postcondition: player's current relics are printed

    #>>> player = {"Relics": [{"name": 'blood vial', "description": 'heal 3HP before every battle', "effect": 3, \
    "one-time": False, "rarity": "common"}]}
    #>>> print_player_relics(player)
    ⩶⩶⩶⩶⩶⩶RELICS⩶⩶⩶⩶⩶⩶
    blood vial
    - heal 3HP before every battle

    #>>> player = {"Relics": [{"name": 'blood vial', "description": 'heal 3HP before every battle', "effect": 3, \
    "one-time": False, "rarity": "common"}, {"name": 'strawberry', "description": 'gain 10 Max HP',"effect": 10, \
    "one-time": True, "rarity": "common"}]}
    #>>> print_player_relics(player)
    ⩶⩶⩶⩶⩶⩶RELICS⩶⩶⩶⩶⩶⩶
    blood vial
    - heal 3HP before every battle
    strawberry
    - gain 10 Max HP
    """
    if len(player["Relics"]) == 0:
        print(col("!black", "You have no relics, duh"))
    else:
        print("\n" + col("magenta", chr(10870) * 6 + "RELICS" + chr(10870) * 6))
        for counter in player["Relics"]:
            print_relic_description(counter)


def show_cards(hand):
    for counter in range(len(hand)):
        card = hand[counter]
        exhaust_print = ""
        if card["exhaust"] == True:
            exhaust_print =  col("!black", "exhausts")
        yellow_square = col("!yellow", "\u25A1")
        print( str(counter + 1) + ") "+ str(card["name"]) + " " + str(card["energy"] * yellow_square)  + " - " + str(card["description"]) + " " + exhaust_print)


def print_player_stats(entity):
    """
    Print the players current stats

    :param entity: a dictionary of the player
    :precondition: player is a well-defined dictionary containing the player's stats
    :postcondition: player's stats are printed

    #>>> player = {"Current HP": 40, "Max HP": 50, "Max Energy": 3, "Current Energy": 3, "Block": 0}   # doctest: +SKIP
    #>>> print_player_stats(player)              # doctest: +SKIP
    ■■■■■■■■■■  40/50 HP   □□□ 3/3 energy

    #>>> player = {"Current HP": 40, "Max HP": 50, "Max Energy": 3, "Current Energy": 1, "Block": 10}   # doctest: +SKIP
    #>>> print_player_stats(player)              # doctest: +SKIP
    ■■■■■■■■■■  40/50 HP  ⦻10 □ 1/3 energy
    """
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

    print(f"{green_square * squares}{red_square * (10 - squares)}  {str(health)}/{str(max_health)}"
          f"{col("!green", " HP ")} {block_icon} {energy  * yellow_square} {str(energy)}/{str(max_energy)}"
          f"{col("!yellow", " energy")}")

    # print((green_square * squares) + (red_square * (10 - squares)) + "  " + (str(health) + "/" + str(max_health) + \
    #    col("!green", " HP  ")  + block_icon +
    #    "  " + (energy  * yellow_square ) + " " + (str(energy) + "/" + str(max_energy)) + col("!yellow", " energy")))


def draw_hand(draw_pile, hand, discard_pile, amount):
    """
    Draw cards to the players hand

    :param draw_pile: a list
    :param hand: a list
    :param discard_pile: a list
    :param amount: a non-zero positive integer
    :precondition: draw_pile is a list of shuffled cards
    :precondition: hand is a list of cards
    :precondition: discard_pile is a list of previously played cards
    :postcondition: hand is drawn from the draw_pile
    :postcondition: if the draw_pile is empty, append the discard_pile to the draw_pile and shuffle
    :return: all lists draw_pile, hand and discard_pile

    #>>> draw_hand([1, 2, 3], [], [], 1)
    ([2, 3], [1], [])
    #>>> draw_hand([1], [], [2, 3], 1)
    ([], [1], [2, 3])
    """
    for count in range(amount):
        if not draw_pile:
            draw_pile.extend(discard_pile)
            discard_pile = []
            random.shuffle(draw_pile)
        hand.append(draw_pile.pop(0))

    return draw_pile, hand, discard_pile


def get_player_input(hand, player, currentEnemy, discard_pile):
    """

    :param hand:
    :param player:
    :param currentEnemy:
    :param discard_pile:
    :return:
    """
    action = input("Enter your action: ")
    action = action.lower()
    move_found = False
    move = ""
    action_index = 0

    # sneaky way to ensure input is int and inside the bounds without using try and except
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


def apply_player_action(player, currentEnemy, enemyIntent, action, hand, discard_pile, action_index):
    """
    Apply the players action

    :param enemyIntent: a dictionary of the enemies intended actions
    :param currentEnemy: a dictionary of the current enemy
    :param player: a dictionary of the player
    :param action: a dictionary of the action
    :param hand: a list
    :param discard_pile: a list
    :param action_index: an integer
    :precondition: action is a well-defined dictionary containing the actions characteristics
    :precondition: currentEnemy is a well-defined dictionary containing the enemy's characteristics
    :precondition: discard_pile is a list
    :precondition: hand is a list
    :precondition: action_index is a positive integer
    :precondition: enemyIntent is a defined dictionary containing the enemies intended actions for their turn
    :precondition: player is a well-defined dictionary containing the player's stats
    :postcondition: players action is applied to itself or the enemy
    :postcondition: players action is removed from hand and appended to discard_pile
    :postcondition: players actions are printed
    """
    player["Current Energy"] -= action["energy"]
    action_type = action["type"]
    action_name = action["name"]
    enemyBLCK = currentEnemy["current block"]
    damage = action["amount"]

    if action_type == "block":
        if apply_player_relic(player, "smooth stone"):
            player["Block"] += 1
        player["Block"] += action["amount"]

    elif action_type == "attack" or action_type == "hybrid":
        if apply_player_relic(player, "strike dummy")  and action["name"] == ("strike" or "strike+"):
            damage += 3
        calculated_damage = damage - enemyBLCK
        if calculated_damage <= 0:
            currentEnemy["current block"] -= damage
        elif calculated_damage > 0:
            currentEnemy["current block"] = 0
            currentEnemy["current HP"] -= calculated_damage
        if action_type == "hybrid":
            if apply_player_relic(player, "smooth stone"):
                player["Block"] += 1
            player["Block"] += action["amount"]
    if action["exhaust"] == False:
        discard_pile.append(hand[action_index])
    hand.remove(hand[action_index])

    if player["Current Energy"] == 0:
        end_player_turn(player, hand, discard_pile)


def apply_enemy_action(enemyIntent, currentEnemy, player, draw_pile):
    """
    Apply the enemies action

    :param enemyIntent: a dictionary of the enemies intended actions
    :param currentEnemy: a dictionary of the current enemy
    :param player: a dictionary of the player
    :param draw_pile: a list
    :precondition: currentEnemy is a well-defined dictionary containing the enemy's characteristics
    :precondition: draw_pile is a list
    :precondition: enemyIntent is a defined dictionary containing the enemies intended actions for their turn
    :precondition: player is a well-defined dictionary containing the player's stats
    :postcondition: enemies action is applied to itself or the player
    :postcondition: the enemies action is printed
    """

    damage = enemyIntent["damage"]
    block = enemyIntent["block"]
    playerBLCK = player["Block"]

    if damage > 0:
        calculated_damage = damage - playerBLCK                 #calculate the damage after blocking
        if calculated_damage <= 0:
            player["Block"] -= damage
        elif calculated_damage > 0:                             #if block is less than incoming damage, remove all block
            player["Block"] = 0
            player["Current HP"] -= calculated_damage
            print("The " + currentEnemy["name"] + " hits you for " + col("!red", str(calculated_damage) + " DMG"))
        time.sleep(1)
    if block > 0:
        currentEnemy["current block"] += block
        print("The " + currentEnemy["name"] + " defends for " + col("cyan", " " + chr(10683) + str(block) + " BLCK"))
        time.sleep(1)
    if "debuff" in enemyIntent:                                 # the only enemy that debuffs is the boss!
        debuff = enemyIntent["debuff"]
        if debuff > 0:
            print("The " + currentEnemy["name"] + " adds " + col("!red", str(debuff) + " burns") + " to your " + col("!green", "Draw pile"))
            for counter in range(debuff):
                draw_pile.append(cards.DEBUFF_CARDS)
    print(col("!black", "The enemy's turn ends.. \n"))
    time.sleep(1)


def check_energy(energy, card):
    """
    Calculate the energy requirement of a card

    :param energy: a positive integer
    :param card: a dictionary of the card
    :precondition: energy is a positive integer
    :precondition: card is a well-defined dictionary containing the cards characteristics
    :return:True if adequite energy, else False

    #>>> check_energy(3, {"name": "strike", "energy": 1})
    True
    #>>> check_energy(2, {"name": "bludgeon", "energy": 2})
    True
    #>>> check_energy(1, {"name": "bash", "energy": 2})       # doctest: +SKIP
    Insufficient Energy!
    False
    """
    energy_needed = card["energy"]
    requirement = energy >= energy_needed
    if not requirement:
        print(col("!black", "Insufficient Energy!"))
    return requirement


def end_player_turn(player, hand, discard_pile):
    for counter in range(len(hand)):
        card_debuff = hand[0]
        if str(card_debuff["name"]) == "burn":
            print(col("red", "The burn hurt you for 2 DMG..."))
            player["Current HP"] -= 2
            time.sleep(0.5)
        discard_pile.append(hand[0])
        hand.remove(hand[0])


def apply_player_relic(player, relic_name):
    for relic in player["Relics"]:              #check if player has any relics and apply buffs accordingly
        if relic["name"] in relic_name:
            if relic_name == "blood vial":                  #blood vial
                player["Current HP"] += int(relic["effect"])
                if player["Current HP"] > player["Max HP"]:
                    player["Current HP"] = player["Max HP"]
            elif relic_name == "smooth stone":                 #smooth stone
                player["Block"] += int(relic["effect"])
            elif relic_name == "strike dummy":              #strike dummy
                return True
            elif relic_name == "regal pillow":           #regal pillow
                return True
            elif relic_name == "prepared slug":           #prepared slug
                player["Block"] = 0
                player["Block"] += int(relic["effect"])
            else:
                print(f"player does not have {relic_name}")


def spawn_event(player, deck):
    decide_event(player, deck)


def spawn_shop(player, deck):
    print(col("!black", "You approach a small shop \n"))
    time.sleep(1.5)
    print_shop_intro()
    relics_sale = shop_relic()
    print_shop_relics(relics_sale)

    player_input = 0
    accepted = range(1, 5)          #this should never go out of bounds... chants the blissfully ignorant developer
    print_player_stats(player)
    while player_input != "exit":
        print("Current gold: " + col("yellow", str(player["Gold"])))

        player_input = input(col("!cyan", "Enter the relic number you want to purchase" + col("!black", "( type *exit* to leave): ")))
        try:
            player_input = int(player_input)
        except ValueError:
            if player_input == "exit":
                break
            else:
                print(col("!black", "invalid input, try again"))
        else:
            if player_input in accepted:
                if (len(relics_sale) - 1) == 0:                               # kicks player out of shop if nothing left
                    time.sleep(0.5)
                    print("\n" + col("!black", "You seem to have bought everything in the shop, impressive"))
                    time.sleep(2.5)
                    break
                wanted_relic = relics_sale[player_input - 1]                        #grab index
                can_purchase = purchase_relic(wanted_relic, player)             #confirm has enough gold

                if can_purchase:
                    print(col("!magenta", "Relic Purchased!"))
                    relics_sale.remove(wanted_relic)                            #remove from shop after purchasing
                    print_shop_relics(relics_sale)                              #reprint updated shop
                else:
                    print(col("!black", "Insufficient Gold!"))
            else:
                print(col("!black", "invalid input, try again"))
    lbl("thaaaaaaank youuuuuuuuu come againnnnnnn", 0.02, "!cyan")
    time.sleep(0.5)
    print(col("!black", "\nTime to leave..."))
    time.sleep(1.5)


def valid_input_fire():
    player_input = input("Enter your action: ")
    action = player_input.lower()
    accepted = ["heal", "rest"]
    not_accepted = ["upgrade", "smith"]
    if action in accepted or action in not_accepted:
        return True, action
    else:
        return False, action


def upgrade_card(deck):
    upgrade_card_list(deck)
    player_input = 0
    accepted = range(1, len(deck) + 1)
    while player_input not in accepted:
        player_input = int(input(col("!cyan", "Enter the card number you want to upgrade: ")))
        #print(player_input)
        #print(player_input in accepted)
        if player_input in accepted:
            card = deck[player_input - 1]
            add_upgrade_card(deck, card)
            lbl("*CLANG*  *CLANG*  *CLANG*", 0.05, "!black")
            time.sleep(0.5)
            print(col("!magenta", "\nThe card has been successfully upgraded!"))
            time.sleep(1.75)
        else:
            print(col("!black", "invalid input, try again"))


def player_sleep(player):
    if apply_player_relic(player, "regal pillow"):
        player["Current HP"] += 40
    player["Current HP"] += 20
    if player["Current HP"] > player["Max HP"]:
        player["Current HP"] = player["Max HP"]
    print("\nYou rest deeply and wake up at " + col("!green",str(player["Current HP"]) + "/" + str(player["Max HP"]) \
        + "HP"))
    time.sleep(2)


def spawn_fire(player, deck):
    print_campfire(player)
    # print(col("!black", "You approach a small campfire, you know you are safe "))
    # time.sleep(1.25)
    # print("The " + col("yellow", "warmth of the fire") + " welcomes you ")
    # time.sleep(1.25)
    # if check_if_goal_attained(player, 5, 5):
    #     print(col("!black", "You know there's no turning back after this"))
    #     time.sleep(0.5)
    # time.sleep(1.25)
    # print("\nYou have the option to " + col("!green", "rest (recover 20HP)") + " or " + col("!blue", "smith (upgrade a card)"))
    # print(col("!black", "You currently have " + str(player["Current HP"]) + "/" + str(player["Max HP"]) + "HP"))
    valid = False
    action = ""

    while not valid:
        valid, action = valid_input_fire()
        if valid:
            if action == "heal" or action == "rest":
                player_sleep(player)
            elif action == "upgrade" or action == "smith":
                upgrade_card(deck)
            if check_if_goal_attained(player, 5, 5):            #final campfire message
                print(col("!black", "You gather your belongings one final time and march towards the boss... \n"))
                time.sleep(0.5)
            else:
                print(col("!black", "Time to get going... \n"))
            time.sleep(1.75)
        else:
            print(col("!black", "invalid input, try again"))


def print_enemy_intent(currentEnemy, enemyIntent):
    """
    Print the enemy intent to the player

    :param currentEnemy: a dictionary of the enemy
    :param enemyIntent: a dictionary containing the enemy's intended action
    :precondition: currentEnemy is a well-formed dictionary containing the player stats
    :precondition: enemyIntent is a well-formed dictionary of the enemy's intended action
    :postcondition: the enemy's intended action is printed
    :postcondition: the enemy's stats are printed

    #>>> currentEnemy = {"name": "mugger", "current HP": 6, "max HP": 36, "current block": 0, "attack pattern": False, \
    "attack": [{"damage": 7, "block": 0}]} # doctest: +SKIP
    #>>> print_enemy_intent (currentEnemy, {'damage': 7, 'block': 0})    # doctest: +SKIP
    The mugger(6/36) intends to attack for 7 DMG
    #>>> currentEnemy = {"name": "mugger", "current HP": 27, "max HP": 36, "current block": 0, "attack pattern": False, \
    "attack": [{"damage": 5, "block": 10}]} # doctest: +SKIP
    #>>> print_enemy_intent (currentEnemy, {'damage': 7, 'block': 0})    # doctest: +SKIP
    The mugger(27/36) intends to attack for 5 DMG and defend for 10 BLCK
    """
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
        message += col("magenta", "UNKNOWN") + col("!black", " (not attack)")
    else:
        if enemyIntent["damage"] != 0:
            message += "attack for " + enemyIntentDMG
            between = 1         # adds "and" inbetween
        if enemyIntent["block"] != 0:
            if between == 1:
                message += " and "
            message += "defend for " + enemyIntentBLCK
        if "debuff" in enemyIntent:
            if enemyIntent["debuff"] != 0:
                message += " and " + col("!red", "debuff you")

    print("The " + currentEnemy["name"] + enemyIntentHP + block_icon + " intends to " + message + "\n")


def initialize_combat(enemy, deck):
    """
    Initialize the combat

    :param enemy: a dictionary of the enemy
    :param deck: a list of cards
    :precondition: enemy is a well-formed dictionary containing the player stats
    :postcondition: currentEnemy is a deep copy of enemy
    :postcondition: deck is randomly shuffled
    :postcondition: draw_pile is a deep copy of deck
    :return: a tuple consisting of player_turn, hand, discard_pile, draw_pile and currentEnemy
    """
    player_turn = 1
    currentEnemy = copy.deepcopy(enemy)
    #enemy["current HP"] = enemy["max HP"]
    random.shuffle(deck)
    discard_pile = []
    hand = []
    draw_pile = copy.deepcopy(deck)
    return player_turn, hand, discard_pile, draw_pile, currentEnemy


def start_combat(player, enemy, deck):
    """
    Drive the combat
    """
    apply_player_relic(player, "blood vial")            #check if player has specific relic
    player_turn, hand, discard_pile, draw_pile, currentEnemy = initialize_combat(enemy, deck)
    enemy_attacks = iter(currentEnemy["attack"])
    while currentEnemy["current HP"] > 0 and player["Current HP"] > 0:
        if player_turn == 1:                                    #apply turn 1 block buff
            apply_player_relic(player, "prepared slug")
        else:
            player["Block"] = 0
        player["Current Energy"] = player["Max Energy"]

        if currentEnemy["attack pattern"] == True:
            enemyIntent = next(enemy_attacks)
        else:
           enemyIntent = random.choice(currentEnemy["attack"])

        draw_hand(draw_pile, hand, discard_pile, player["Max Draw"])     # change 3 to edit cards drawn
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
            apply_enemy_action(enemyIntent, currentEnemy, player, draw_pile)
            player_turn += 1


def valid_input_reward():
    """
    Asks the player to input either "yes", "take", "no" or "skip"

    :postcondition: prints a warning if player input is invalid
    :return: True if input is valid, else False
    :return: Action if input is valid, else None

    #>>> choice = "yes"     # doctest: +SKIP
    #>>> valid_input_reward()       # doctest: +SKIP
    True, "yes"
    #>>> choice = "skip"     # doctest: +SKIP
    #>>> valid_input_reward()       # doctest: +SKIP
    False
    """
    action = input("Take card? ")
    action = action.lower()
    accepted = ["take", "yes"]
    not_accepted = ["skip", "no"]
    if action in accepted or action in not_accepted:
        return True, action
    else:
        return False


def reward_player(player, reward, deck):
    """
    Determine the reward for the player

    :param player: a dictionary of the player
    :param reward: a positive integer or float
    :param deck: a list of cards
    :precondition: player is a well-formed dictionary containing the player stats
    :precondition: reward is a positive integer or float
    :postcondition: the reward is printed to the player
    :postcondition: the player is offered a card reward
    :postcondition: the player can add a card to the deck
    #>>>
    """
    print ( "\n" + col("magenta", chr(10870) * 3 + "LOOT" + chr(10870) * 3))

    gold_reward = round(random.randint(15, 25) * reward)
    player["Gold"] += gold_reward
    print("Got " + col("yellow", str(player["Gold"] )+ " Gold") +  " " + col("!black", "+" + str(gold_reward)))
    if reward == 1.5:
        loot_relic = get_relic()
        print(print_relic_description(loot_relic))
        player["Relics"].append(loot_relic)
        relic_one_time_buff(loot_relic, player)

    print(col("green", "Card reward: "))
    card_option = random_card_reward()
    card_details(card_option)
    valid_input = False
    action = ""
    while not valid_input:
        valid_input, action = valid_input_reward()
        if valid_input:
            if action == "take" or action == "yes":
                add_new_card(deck, card_option)
                print(col("magenta", "- " + (card_option['name']) + " added to deck!"))
        else:
            print(col("!black", "invalid input, try again"))

    time.sleep(1)
    print(col("!black", "Time to get moving... "))
    time.sleep(2)


def check_board_location(board, player, update):
    """
    Check the player's current location

    :param board: a dictionary of the board
    :param player: a dictionary of the player
    :param update: a boolean
    :precondition: player is a well-formed dictionary containing the player stats
    :postcondition: print the current location's description
    :postcondition: print previously visited locations on board
    :return: a non-empty string of the board's event at the players current location

    #>>> board = {(0, 0): 'fight', (0, 1): 'fight', (1, 0): 'elite', (1, 1): 'fire'}
    #>>> check_board_location(board, {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}, False)
    You are now in: fight at co-ords(0, 1)
    <BLANKLINE>
    'fight'
    #>>> board = {(0, 0): 'fight', (0, 1): 'fight', (1, 0): 'elite', (1, 1): 'fire'}
    #>>> check_board_location(board, {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}, False)
    You are now in: fire at co-ords(1, 1)
    <BLANKLINE>
    'fire'
    """
    player_cords = (player["X-coordinate"], player["Y-coordinate"])
    if update:                                  # overwrites old locations to let player know
        board[player_cords] = col("!black", "empty")
    else:
        if player_cords in board:
            print("You are now in: " + board[player_cords] + " at co-ords" + str(player_cords) + "\n")
        return board[player_cords]


def get_user_choice(player):
    """
    Print the player movement options

    Asks the player to input one of 4 options: W A S D
    :postcondition: prints a warning if the player input is invalid
    :return: a non-empty string containing "A" or "S" or "W" or "D"

    #>>> choice = "W"    # doctest: +SKIP
    #>>> get_user_choice()   # doctest: +SKIP
    W
    #>>> choice = "D"    # doctest: +SKIP
    #>>> get_user_choice()   # doctest: +SKIP
    D
    #>>> choice = "F"    # doctest: +SKIP
    #>>> get_user_choice()   # doctest: +SKIP
    "INVALID MOVEMENT INPUT"
    """
    movements_print = ["W - Move up", "A - Move left", "S - Move down", "D - Move right"]
    movements_valid = ("W", "A", "S", "D")
    print("MOVEMENT OPTIONS")

    for move in movements_print:
        print(move)

    wanted_movement = ""

    while wanted_movement not in movements_valid:
        wanted_movement = input("Enter your movement (or other action) here: ")
        wanted_movement = wanted_movement.upper()

        if wanted_movement in movements_valid:
            return wanted_movement
        elif wanted_movement == "HELP":
            print("\n")
            print(CONST_MAP_HELP)
            time.sleep(4)
        elif wanted_movement == "GOLD":
            print("Current gold: " + col("yellow", str(player["Gold"])))
            time.sleep(2)
        elif wanted_movement == "RELIC" or wanted_movement == "RELICS":
            print_player_relics(player)
            time.sleep(2)
        else:
            print("\nINVALID MOVEMENT INPUT")


def projected_movement(player, movement):
    """
    Calculate the projected movement

    :param player: a dictionary of the player
    :param movement: a one letter string of the movement
    :precondition: player is a well-formed dictionary containing the player stats
    :precondition: movement is a non-empty string containing "A" or "S" or "W" or "D"
    :postcondition: the correct vector of the players movement
    :return: dictionary of character's projected coordinates

    #>>> projected_movement({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}, "D")
    (1, 0)
    #player>>> projected_movement({"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5}, "W")
    (2, 1)
    """

    if movement == "W":
        projected_cords = (player["X-coordinate"], player["Y-coordinate"] - 1)
    elif movement == "A":
        projected_cords = (player["X-coordinate"] - 1, player["Y-coordinate"])
    elif movement == "S":
        projected_cords = (player["X-coordinate"], player["Y-coordinate"] + 1)
    elif movement == "D":
        projected_cords = (player["X-coordinate"] + 1, player["Y-coordinate"])
    else:
        print("something has gone very wrong here")
        return "Error"
    return projected_cords


def validate_move(board, player, movement):
    """
    Determine the validity of the player's wanted movement

    :param board: a dictionary of the board
    :param character: a dictionary of the character
    :param movement: a non-empty string
    :precondition: character is a well-formed dictionary containing the character stats
    :precondition: movement is a non-empty string containing "A" or "S" or "W" or "D"
    :return: True if move is valid, else False

    #>>> validate_move({(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'hills', (1, 1): 'dark forest'},\
{"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}, "W") # doctest: +SKIP
     <BLANKLINE> INVALID MOVEMENT False
     #>>> validate_move({(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'hills', (1, 1): 'dark forest'},\
{"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}, "N") # doctest: +SKIP
     True
    """
    valid_cords = projected_movement(player, movement)

    if valid_cords not in board:
        print("\nINVALID MOVEMENT")
        return False
    else:
        return True


def move_character(player, movement):
    """
    Update the characters position

    :param character: a dictionary of the character
    :param movement: a non-empty string
    :precondition: character is a well-formed dictionary containing the character stats
    :precondition: movement is a non-empty string containing "A" or "S" or "W" or "D"
    :postcondition: update character location in its dictionary

    #>>> move_character({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}, 'S')
    {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
    #>>> move_character({"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5}, 'D')
    {'X-coordinate': 3, 'Y-coordinate': 2, 'Current HP': 5}
    """
    move_cords = projected_movement(player, movement)
    player["X-coordinate"] = move_cords[0]
    player["Y-coordinate"] = move_cords[1]
    return player

def check_if_goal_attained(player, rows, columns):
    """
    Determine if the character has reached the goal

    :param character: a dictionary of the character
    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: character is a well-formed dictionary containing the character stats
    :return: True if goal is attained, else False

    #>>> check_if_goal_attained({"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}, 4, 4)
    True
    #>>> check_if_goal_attained({"X-coordinate": 2, "Y-coordinate": 1, "Current HP": 5}, 4, 4)
    False
    """
    return player["X-coordinate"] == (rows - 1) and player["Y-coordinate"] == (columns - 1)


def calculate_enemy_diffuculty(event):
    """
    Calculate the enemy diffuculty and reward

    :param event: a non-empty string
    :precondition: event is a non-empty string
    :postcondition: reward is calculated by the event
    :postcondition: a chosen enemy is randomly selected from a list
    :return: a dictionary with the stats of the chosen enemy

    #>>> calculate_enemy_diffuculty("fight") # doctest: +SKIP
    ({'name': 'mugger', 'current HP': 36, 'max HP': 36, 'current block': 0, 'attack pattern': False, 'attack': \
    [{'damage': 7, 'block': 0}, {'damage': 11, 'block': 0}, {'damage': 5, 'block': 7}, {'damage': 0, 'block': 8}]}, 1)

    #>>> calculate_enemy_diffuculty("elite") # doctest: +SKIP
    ({"name": "gremlin nob", "current HP": 53, "max HP": 53, "current block": 0, "attack pattern": True, "attack":
    [{"damage": 0, "block": 0}, {"damage": 8, "block": 0}, {"damage": 16, "block": 0}, {"damage": 20, "block": 0},
    {"damage": 20, "block": 0}, {"damage": 20, "block": 0}]}, 1.5)
    """
    if event == "fight":
        enemy_chosen = random.choice(enemy.enemies_easy)
        reward = 1
    elif event == "elite":
        enemy_chosen = random.choice(enemy.enemies_hard)
        reward = 1.5
    elif event == "boss":
        enemy_chosen = enemy.enemies_boss
        #print(enemy_chosen)
        reward = 2
    return enemy_chosen, reward


def main():
    rooms, deck, player, board = initialize_game_start()

    while not check_if_goal_attained(player, 5, 5) and player["Current HP"] > 0:
        print_board(board, player)
        movement = get_user_choice(player)
        valid_move = validate_move(board, player, movement)

        if valid_move:
            move_character(player, movement)

            event = check_board_location(board, player, False)

            if event == "fight" or event == "elite":
                enemy, reward = calculate_enemy_diffuculty(event)
                start_combat(player, enemy, deck)
                if player["Current HP"] > 0:
                    reward_player(player, reward, deck)
            elif event == "shop":
                spawn_shop(player, deck)
            elif event == "event":
                spawn_event(player, deck)
            elif event == "fire":
                spawn_fire(player, deck)
                if check_if_goal_attained(player, 5, 5):        #final boss after fire
                    enemy, reward = calculate_enemy_diffuculty("boss")
                    start_combat(player, enemy, deck)

            check_board_location(board, player, True)

    if not player["Current HP"] > 0:
        print("\n" + col("!red", "GAME OVER"))
    if check_if_goal_attained and player["Current HP"] > 0:
        print("\n" + col("!green", "YOU WON"))

if __name__ == '__main__':
    main()

from colorama import Fore, Back, Style, init
init(autoreset=True)
import random
import time
import relics
import copy

import text
import enemy
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
from initialize_game import initialize_game_start
from initialize_game import print_board


def card_details(card):
    for key in card.keys():
        print(str(key) + ": " + str(card[key]))
    print("")


def print_player_relics(player):
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
       col("!green", " HP  ")  + block_icon +
       "  " + (energy  * yellow_square ) + " " + (str(energy) + "/" + str(max_energy)) + col("!yellow", " energy")))


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

    elif action_type == "attack" or action_type == "hybrid":
        calculated_damage = damage - enemyBLCK
        if calculated_damage <= 0:
            currentEnemy["current block"] -= damage
        elif calculated_damage > 0:
            currentEnemy["current block"] = 0
            currentEnemy["current HP"] -= calculated_damage
        if action_type == "hybrid":
            player["Block"] += action["amount"]
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


def spawn_shop(player, deck):
    print(col("!black", "You approach a small shop \n"))
    #time.sleep(1.5)
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



def spawn_fire(player, deck):
    print(col("!black", "You approach a small campfire, you know you are safe "))
    time.sleep(1.25)
    print("The " + col("yellow", "warmth of the fire") + " welcomes you \n")
    time.sleep(1.25)
    if check_if_goal_attained(player, 5, 5):
        print(col("!black", "You know there's no turning back after this"))
    time.sleep(1.25)
    print("You have the option to " + col("!green", "rest (recover 20HP)") + " or " + col("!blue", "smith (upgrade a card)"))
    print(col("!black", "You currently have " + str(player["Current HP"]) + "/" + str(player["Max HP"]) + "HP"))
    valid = False
    action = ""

    while not valid:
        valid, action = valid_input_fire()
        if valid:
            if action == "heal" or action == "rest":
                player["Current HP"] += 20
                if player["Current HP"] > player["Max HP"]:
                    player["Current HP"] = player["Max HP"]
                print("\nYou rest deeply and wake up at " + col("!green", str(player["Current HP"]) + "/" + str(player["Max HP"]) + "HP"))
                time.sleep(2)

            elif action == "upgrade" or action == "smith":
                upgrade_card(deck)
            if check_if_goal_attained(player, 5, 5):            #final campfire message
                print(col("!black", "You gather your belongings one final time and march towards the boss"))
                time.sleep(0.5)
            else:
                print(col("!black", "Time to get going... \n"))
            time.sleep(1.75)
        else:
            print(col("!black", "invalid input, try again"))


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
        message += col("magenta", "UNKNOWN") + col("!black", " (not attack)")
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
    player_turn, hand, discard_pile, draw_pile, currentEnemy = initialize_combat(enemy, deck)
    enemy_attacks = iter(currentEnemy["attack"])
    while currentEnemy["current HP"] > 0 and player["Current HP"] > 0:
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
            apply_enemy_action(enemyIntent, currentEnemy, player)


def valid_input_reward():
    action = input("Take card? ")
    action = action.lower()
    accepted = ["take", "yes"]
    not_accepted = ["skip", "no"]
    if action in accepted or action in not_accepted:
        return True, action
    else:
        return False


def reward_player(player, reward, deck):
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
    player_cords = (player["X-coordinate"], player["Y-coordinate"])
    if update:
        # board[player_cords] = col("@blue", col("!white","player"))
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

    :param character: a dictionary of the character
    :param movement: a one letter string of the movement
    :precondition: character is a well-formed dictionary containing the character stats
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
    if event == "fight":
        enemy_chosen = random.choice(enemy.enemies_easy)
        reward = 1
    elif event == "elite":
        enemy_chosen = random.choice(enemy.enemies_hard)
        reward = 1.5
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
            elif event == "fire":
                spawn_fire(player, deck)
                if check_if_goal_attained(player, 5, 5):
                    start_combat(player, enemies_boss, deck)
            check_board_location(board, player, True)

    if not player["Current HP"] > 0:
        print("\n" + col("!red", "GAME OVER"))


if __name__ == '__main__':
    main()

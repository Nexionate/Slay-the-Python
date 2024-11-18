from colorama import Fore, Back, Style, init
init(autoreset=True)
import random

#print(Fore.RED + "This text is red")
def col(colour, word):
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
    return (colour_code + word + Style.RESET_ALL)

help_text = \
    "- To play a card, input its number order or full name. The yellow squares " + col("!yellow", "\u25A1") +" indicate your current energy." \
    "\n- You cannot play a card if you don't have sufficient energy. " \
    "\n- You will gain your Max Energy upon the end of the enemies turn." \
    "" \
    "\n- If you do not have enough energy to play your remaining cards, type" + col("magenta", " \"end\" ") + "to finish your turn" \
    "\n- The " + col("!cyan", chr(10683)) + " icon indicates how much damage will be blocked. " \
    "\n- Cards that " + col("!black", "exhaust") + " can only be used once per battle, and will return to your deck when complete. " \

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




relic_pool = [
    {"name": 'strike dummy',
    "description": 'adds +3 DMG to all cards with the (strike) keyword',
    "effect": 3},

    {"name": 'oddly smooth stone',
    "description": 'adds +1 to all block',
    "effect": 1},

    {"name": 'black belt',
    "description": '15% change to dodge incoming attacks',
    "effect": 0.85},

    {"name": 'blood vial',
    "description": 'heal 4HP after every battle',
    "effect": 3},

    {"name": 'old coin',
    "description": 'immediately gain 200 gold',
    "effect": 200},

    {"name": 'strawberry',
    "description": 'gain 8 Max HP',
    "effect": 8},

    {"name": 'prepared slug',
    "description": 'gain 8 block the first turn of combat',
    "effect": 8},
]

enemies_easy = ({"name": "mugger", "current HP": 30, "max HP": 30, "current block": 0, "attack": [{"damage": 7, "block": 0}, {"damage": 13, "block": 0}, {"damage": 5, "block": 10}, {"damage": 0, "block": 10}]})



def create_relics():
    random.shuffle(relic_pool)


def get_relic():
    x = relic_pool.pop(0)
    print(x)



def draw_hand(draw_pile, hand, discard_pile):
    for count in range(3):
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

    #print(ord(action) - 49)
    #print(len(hand) -1)

    if len(action) == 1 and ord(action) in range(49, len(hand) + 49):

        action = int(action)
        move = hand[action - 1]
        action_index = action - 1
        move_found = True

    if not move_found:
        if action == "help":
            print(help_text)
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
    if block > 0:
        currentEnemy["current block"] += block




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


def start_combat(player, enemy, deck):
    """
    Drive the combat

    """
    player_turn = 0
    currentEnemy = enemy
    random.shuffle(deck)
    discard_pile = []
    hand = []
    draw_pile = deck

    while currentEnemy["current HP"] > 0:
        player["Block"] = 0
        player["Current Energy"] = player["Max Energy"]

        enemyIntent = random.choice(currentEnemy["attack"])
        #print_enemy_intent(currentEnemy, enemyIntent)  # prints intent

        draw_hand(draw_pile, hand, discard_pile)
        print(col("!black", "Your turn begins.. "))

        while player["Current Energy"] > 0 and currentEnemy["current HP"] > 0:     # begin players turn
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
    print("player wins")

            #player["Current Energy"] = 0









def main():
    strike = {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False}
    defend = {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False}
    bash = {"name": "bash", "type": "attack", "amount": 9, "energy": 2, "description": "9 DMG", "exhaust": False}
    bludgeon = {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG", "exhaust": True}
    deck = [bash, bludgeon]

    for i in range(2):
        deck.append(strike)
        deck.append(defend)

    #deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(deck)

    player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 37, "Max HP": 50, "Max Energy": 3, "Current Energy": 3, "Block": 0}
    #hand = shuffle(deck) UNCOMMENT LATER
    start_combat(player, enemies_easy, deck)
    '''
    get_input(hand)
    create_relics()
    get_relic()
    '''


if __name__ == '__main__':
    main()

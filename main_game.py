from colorama import Fore, Back, Style, init
init(autoreset=True)
import random

#print(Fore.RED + "This text is red")


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
            exhaust_print = Fore.DIM + "exhausts" + Style.RESET_ALL
        yellow_square = Fore.LIGHTYELLOW_EX + ("\u25A1") + Style.RESET_ALL
        print(str(card["name"]) + " " + str(card["cost"] * yellow_square)  + " - " + str(card["utility"]))
        # print(str(card["name"]))



def print_player_stats(entity):
    health = entity["Current HP"]
    max_health = entity["Max HP"]
    energy = entity["Current Energy"]
    max_energy = entity["Max Energy"]
    squares = health // (max_health // 10)
    green_square = Fore.GREEN + ("\u25A0") + Style.RESET_ALL
    red_square = Fore.RED + ("\u25A0") + Style.RESET_ALL
    yellow_square = Fore.LIGHTYELLOW_EX + ("\u25A1") + Style.RESET_ALL

    print((green_square * squares) + (red_square * (10 - squares)) + "  " + (str(health) + "/" + str(max_health) + \
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

enemies_easy = ({"name": "mugger", "Current HP": 30, "attack": [{"damage": 7, "block": 0}, {"damage": 13, "block": 0}, {"damage": 5, "block": 10}]})



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
    #print("draw pile: " + str(draw_pile))
    #print("discard pile: " + str(discard_pile))
    #print("hand:" + str(hand))

    #for removing cards
    # for counter in range(len(hand)):
    #     discard_pile.append(hand[0])
    #     hand.remove(hand[0])

    return draw_pile, hand, discard_pile

def get_player_input(hand, player, currentEnemy):
    action = input("Enter your action: ")
    action = action.lower()
    move_found = False


    if len(action) == 1 and ord(action) in range(49, 59):
        action = int(action)
        print("now an int")
        move = hand[action - 1]
        print(move)
    else:
        for index, item in enumerate(hand):
            if item["name"] == action:
                print("yes")
                break

        print("exit early")
        print(action)

    if action == "help":
        print("- To play a card, input its number or full name. The yellow squares indicate your current energy.\n"
              "- You cannot play a card if you don't have sufficient energy. You will gain your Max Energy upon the "
              "end of the enemies turn.\n")


def spawn_shop():
    pass


def print_enemy_intent(currentEnemy, enemyIntent):
    enemyIntentDMG = Fore.RED + str(enemyIntent["damage"]) + " DMG" + Style.RESET_ALL
    enemyIntentBLCK = Fore.LIGHTBLUE_EX + str(enemyIntent["block"]) + " BLCK" + Style.RESET_ALL
    print("The " + currentEnemy[
        "name"] + " intends to attack for " + enemyIntentDMG + " and block for " + enemyIntentBLCK)


def start_combat(player, enemy, deck):
    player_turn = 0
    currentEnemy = enemy
    enemyIntent = random.choice(currentEnemy["attack"])
    print_enemy_intent(currentEnemy, enemyIntent)                # prints intent

    #begin player turn
    if player_turn == 0:
        random.shuffle(deck)
        discard_pile = []
        hand = []
        draw_pile = deck
        player_turn += 1

    while currentEnemy["Current HP"] > 0 and player["Current Energy"] > 0:
        draw_hand(draw_pile, hand, discard_pile)

        #get player input
        print("Your turn begins.. ")
        show_cards(hand)
        print_player_stats(player)

        action = get_player_input(hand, player, currentEnemy)
        player["Current Energy"] = 0









def main():
    strike = {"name": "strike", "cost": 1, "utility": "6 DMG", "exhaust": False}
    defend = {"name": "defend", "cost": 1, "utility": "5 Block", "exhaust": False}
    bash = {"name": "bash", "cost": 2, "utility": "9 DMG", "exhaust": False}
    deck = [strike, defend, bash]

    for i in range(4):
        deck.append(strike)
        deck.append(defend)

    #deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(deck)

    player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 37, "Max HP": 50, "Max Energy": 3, "Current Energy": 3}
    #hand = shuffle(deck) UNCOMMENT LATER
    start_combat(player, enemies_easy, deck)
    '''
    get_input(hand)
    create_relics()
    get_relic()
    '''


if __name__ == '__main__':
    main()

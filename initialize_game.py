import text
from cards import card_list
from relics import create_relics
from text import col
from text import CONST_MAP_HELP
import random


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


def make_character():
    """
    Generate a dictionary of a character

    :postcondition: Character has a description of their X & Y coordinates
    :postcondition: Character has a description of their current HP
    :return: dictionary of character stats
    """
    return {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3,
            "Current Energy": 3, "Block": 0, "Gold": 50, "Relics": []}


def make_board(rows, cols):
    """
    Generate a grid with coordinates and description for each tile

    :param rows: a positive integer
    :param cols: a positive integer
    :precondition: rows >= 0
    :precondition: cols >= 0
    :postcondition: Each coordinate is a tuple with a short description
    :return: a dictionary of the coordinates
    """

    cord_list = []
    cord_dic = {}
    for row_counter in range(rows):
        for col_counter in range(cols):
            conv_to_tuple = (row_counter, col_counter)
            cord_list.append(conv_to_tuple)
    populated_board = populate_board(cord_list, cord_dic, rows, cols)
    return populated_board


def populate_board(cord_list, cord_dic, rows, cols):
    event_chance = ["fight", "fight", "fight", "fight", "fight", "fight", "elite", "event", "fire", "elite"]
    event_counter = {"elite counter": 0, "fire counter": 0, "elite max": 2, "fire max": 2}

    board_exceptions = {(0, 0): "start", (0, 1): "fight", (1, 0): "fight", (1, 1): "fight", (rows - 1, cols - 1): "fire", (rows//2, cols//2): "shop"}
    # board_required = ""
    for counter in cord_list:
        if counter in board_exceptions:
            cord_dic[counter] = board_exceptions[counter]
        else:
            event = random.choice(event_chance)
            if event == "fire" and event_counter["fire counter"] < event_counter["fire max"]:
                event_counter["fire counter"] += 1
                if event_counter["fire counter"] >= event_counter["fire max"]:
                    event_chance.remove("fire")

            elif event == "elite" and event_counter["elite counter"] < event_counter["elite max"]:
                event_counter["elite counter"] += 1
                if event_counter["elite counter"] >= event_counter["elite max"]:
                    event_chance.remove("elite")
                    event_chance.remove("elite")

            cord_dic[counter] = event
    return cord_dic


def print_board(cord_dic, rows, cols):
    print_counter = 0
    print("\n" + col("magenta", chr(10870) * 6 + "MAP" + chr(10870) * 5))
    message = ""
    for counter in cord_dic:
        if cord_dic[counter] == "elite":
            message += col("red", cord_dic[counter] + " ")
        elif cord_dic[counter] == "fire":
            message += col("yellow", cord_dic[counter] + "  ")
        elif cord_dic[counter] == "start":
            message += col("green", cord_dic[counter] + " ")
        elif cord_dic[counter] == "event":
            message += col("blue", cord_dic[counter] + " ")
        elif cord_dic[counter] == "shop":
            message += col("magenta", cord_dic[counter] + "  ")
        else:
            message += cord_dic[counter] + " "
        print_counter += 1

        if print_counter % 5 == 0:
            if print_counter == 25:
                print(message)
            else:

                print(message + "\n")
            message = ""
    print(col("magenta", chr(10870) * 6 + "MAP" + chr(10870) * 5))


def initialize_game_start():
    deck = create_deck()
    rooms = 0
    create_relics()
    random.shuffle(deck)
    player = make_character()
    board = make_board(5, 5)
    #print_board(board, 5, 5)
    print(text.CONST_MAP_HELP)
    return rooms, deck, player, board

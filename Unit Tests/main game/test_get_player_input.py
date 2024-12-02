from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io
from text import col


class Test(TestCase):

    @patch('builtins.input', side_effect=["1"])
    def test_get_player_input_valid_number(self, mock_input):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        hand = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False},
                {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
                 "upgrade": False},
                {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                 "exhaust": True, "upgrade": False}]
        discard_pile = []
        expected = get_player_input(hand, player, discard_pile)
        given = (
            {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
             "upgrade": False}, True, 0)
        self.assertEqual(expected, given)

    @patch('builtins.input', side_effect=["4"])
    def test_get_player_input_valid_number_last_card(self, mock_input):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        hand = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False},
                {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
                 "upgrade": False},
                {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                 "exhaust": True, "upgrade": False}]
        discard_pile = []
        expected = get_player_input(hand, player, discard_pile)
        given = (
            {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
             "exhaust": True, "upgrade": False}, True, 3)
        self.assertEqual(expected, given)

    @patch('builtins.input', side_effect=["strike"])
    def test_get_player_input_valid_name(self, mock_input):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        hand = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False},
                {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
                 "upgrade": False},
                {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                 "exhaust": True, "upgrade": False}]
        discard_pile = []
        expected = get_player_input(hand, player, discard_pile)
        given = (
            {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
             "upgrade": False}, True, 0)
        self.assertEqual(expected, given)

    @patch('builtins.input', side_effect=["strike"])
    def test_get_player_input_valid_proper_index(self, mock_input):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        hand = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False},
                {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
                 "upgrade": False},
                {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                 "exhaust": True, "upgrade": False},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False}
                ]
        discard_pile = []
        expected = get_player_input(hand, player, discard_pile)
        given = (
            {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
             "upgrade": False}, True, 0)
        self.assertEqual(expected, given)

    @patch('builtins.input', side_effect=["5"])
    def test_get_player_input_invalid_index(self, mock_input):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        hand = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False},
                {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
                 "upgrade": False},
                {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                 "exhaust": True, "upgrade": False},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False}
                ]
        discard_pile = []
        expected = get_player_input(hand, player, discard_pile)
        given = ("", False, 0)
        self.assertEqual(expected, given)

    @patch('builtins.input', side_effect=["crying developer"])
    def test_get_player_input_invalid_name(self, mock_input):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        hand = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False},
                {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
                 "upgrade": False},
                {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                 "exhaust": True, "upgrade": False},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False}
                ]
        discard_pile = []
        expected = get_player_input(hand, player, discard_pile)
        given = ("", False, 0)
        self.assertEqual(expected, given)

    @patch('builtins.input', side_effect=["help"])
    def test_get_player_input_help(self, mock_input):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        hand = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False},
                {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
                 "upgrade": False},
                {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                 "exhaust": True, "upgrade": False},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False}
                ]
        discard_pile = []
        expected = get_player_input(hand, player, discard_pile)
        given = ("", False, 0)
        self.assertEqual(expected, given)

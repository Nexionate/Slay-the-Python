
from unittest.mock import patch
from text import col

from unittest import TestCase
from main_game import get_user_choice


class Test(TestCase):
    @patch('builtins.input', side_effect=["S"])
    def test_get_user_choice_south(self, _):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
            "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        actual = get_user_choice(player)
        expected = 'S'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["W"])
    def test_get_user_choice_north(self, _):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        actual = get_user_choice(player)
        expected = 'W'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["D"])
    def test_get_user_choice_east(self, _):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        actual = get_user_choice(player)
        expected = 'D'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["A"])
    def test_get_user_choice_west(self, _):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        actual = get_user_choice(player)
        expected = 'A'
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["a", "A"])
    def test_get_user_choice_not_capital(self, _):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        actual = get_user_choice(player)
        expected = 'A'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["x", "W"])
    def test_get_user_choice_incorrect(self, _):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        actual = get_user_choice(player)
        expected = 'W'
        self.assertEqual(expected, actual)
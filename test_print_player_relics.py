from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io

import re


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_relics_two(self, mock_output):
        given = f"\n{col("magenta", "⩶⩶⩶⩶⩶⩶RELICS⩶⩶⩶⩶⩶⩶")}\n" \
                f"{col("!magenta", "blood vial")}\n" \
                f"{col("magenta", "- heal 3HP before every battle")}\n" \
                f"{col("!magenta", "strawberry")} {col("!black", "10")}\n" \
                f"{col("magenta", "- gain 10 Max HP")}\n"

        player = {"Relics": [{"name": 'blood vial', "description": 'heal 3HP before every battle', "effect": 3, \
                              "one-time": False, "rarity": "common"},
                             {"name": 'strawberry', "description": 'gain 10 Max HP', "effect": 10, \
                              "one-time": True, "rarity": "common"}]}
        print_player_relics(player)
        expected = mock_output.getvalue()
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_relics_one(self, mock_output):
        given = f"\n{col("magenta", "⩶⩶⩶⩶⩶⩶RELICS⩶⩶⩶⩶⩶⩶")}\n" \
                f"{col("!magenta", "oddly smooth stone")}\n" \
                f"{col("magenta", "- adds +1 to all block")}\n"

        player = {"Relics": [{"name": 'oddly smooth stone', "description": 'adds +1 to all block',
                              "effect": 1, "one-time": False, "rarity": "common"}]}
        print_player_relics(player)
        expected = mock_output.getvalue()
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_relics_many(self, mock_output):
        given = f"\n{col("magenta", "⩶⩶⩶⩶⩶⩶RELICS⩶⩶⩶⩶⩶⩶")}\n" \
                f"{col("!magenta", "oddly smooth stone")}\n" \
                f"{col("magenta", "- adds +1 to all block")}\n" \
                f"{col("!magenta", "blood vial")}\n" \
                f"{col("magenta", "- heal 3HP before every battle")}\n" \
                f"{col("!magenta", "strawberry")} {col("!black", "10")}\n" \
                f"{col("magenta", "- gain 10 Max HP")}\n" \
                f"{col("!magenta", "prepared slug")}\n" \
                f"{col("magenta", "- gain 8 block the first turn of combat")}\n"

        player = {"Relics": [{"name": 'oddly smooth stone', "description": 'adds +1 to all block',
                              "effect": 1, "one-time": False, "rarity": "common"},
                             {"name": 'blood vial', "description": 'heal 3HP before every battle', "effect": 3, \
                              "one-time": False, "rarity": "common"},
                             {"name": 'strawberry', "description": 'gain 10 Max HP', "effect": 10, \
                              "one-time": True, "rarity": "common"},
                             {"name": 'prepared slug', "description": 'gain 8 block the first turn of combat',
                              "effect": 8, "one-time": False,
                              "rarity": "uncommon"}]}
        print_player_relics(player)
        expected = mock_output.getvalue()
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_relics_empty(self, mock_output):
        given = f"{col("!black", "You have no relics, duh")}\n"
        player = {"Relics": []}
        print_player_relics(player)
        expected = mock_output.getvalue()
        self.assertEqual(expected, given)

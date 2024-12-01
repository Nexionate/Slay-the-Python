from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io
from text import col
import re

class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_card_details_strike(self, mock_output):
        card = {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False}
        given = f"1) strike {col("!yellow", "□")} - 6 DMG\n"
        card_details(card)
        expected = mock_output.getvalue()
        self.assertEqual(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_card_details_defend(self, mock_output):
        card = {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False, "upgrade": False}
        given = f"1) defend {col("!yellow", "□")} - 5 BLCK\n"
        card_details(card)
        expected = mock_output.getvalue()
        self.assertEqual(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_card_details_upgraded_card(self, mock_output):
        card = {"name": "iron wave+", "type": "hybrid", "amount": 7, "energy": 1, "description": "7 DMG, 7 BLCK",
                     "exhaust": False, "upgrade": True}
        given = f"1) iron wave+ {col("!yellow", "□")} - 7 DMG, 7 BLCK\n"
        card_details(card)
        expected = mock_output.getvalue()
        self.assertEqual(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_card_details_exhaust(self, mock_output):
        card = {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                      "exhaust": True, "upgrade": False}
        given = f"1) anger  - 7 DMG{col("!black", " exhausts")}\n"
        card_details(card)
        expected = mock_output.getvalue()
        self.assertEqual(given, expected)



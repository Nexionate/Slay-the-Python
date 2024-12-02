from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io
from text import col
import re


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_cards_one(self, mock_output):
        card = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False}]
        given = f"1) strike {col("!yellow", "□")} - 6 DMG\n"
        show_cards(card)
        expected = mock_output.getvalue()
        self.assertEqual(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_cards_two(self, mock_output):
        card = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False},
                {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
                 "upgrade": False}]
        given = f"1) strike {col("!yellow", "□")} - 6 DMG\n" \
                f"2) defend {col("!yellow", "□")} - 5 BLCK\n"
        show_cards(card)
        expected = mock_output.getvalue()
        self.assertEqual(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_cards_three(self, mock_output):
        card = [{"name": "iron wave+", "type": "hybrid", "amount": 7, "energy": 1, "description": "7 DMG, 7 BLCK",
                 "exhaust": False, "upgrade": True},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False},
                {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
                 "upgrade": False}]
        given = f"1) iron wave+ {col("!yellow", "□")} - 7 DMG, 7 BLCK\n" \
                f"2) strike {col("!yellow", "□")} - 6 DMG\n" \
                f"3) defend {col("!yellow", "□")} - 5 BLCK\n"
        show_cards(card)
        expected = mock_output.getvalue()
        self.assertEqual(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_cards_five(self, mock_output):
        card = [{"name": "iron wave+", "type": "hybrid", "amount": 7, "energy": 1, "description": "7 DMG, 7 BLCK",
                 "exhaust": False, "upgrade": True},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False},
                {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                 "exhaust": True, "upgrade": False},
                {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
                 "upgrade": False},
                {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                 "exhaust": True, "upgrade": False}]
        given = f"1) iron wave+ {col("!yellow", "□")} - 7 DMG, 7 BLCK\n" \
                f"2) strike {col("!yellow", "□")} - 6 DMG\n" \
                f"3) anger  - 7 DMG{col("!black", " exhausts")}\n" \
                f"4) defend {col("!yellow", "□")} - 5 BLCK\n" \
                f"5) anger  - 7 DMG{col("!black", " exhausts")}\n"
        show_cards(card)
        expected = mock_output.getvalue()
        self.assertEqual(given, expected)

from unittest import TestCase

from cards import show_deck_upgrade
from relics import *
from unittest.mock import patch
import io

import re


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_deck_upgrade_none_upgraded_many(self, mock_output):
        deck = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False},
                {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG",
                 "exhaust": True, "upgrade": False},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False},
                {"name": "iron wave", "type": "hybrid", "amount": 5, "energy": 1, "description": "5 DMG, 5 BLCK",
                 "exhaust": False, "upgrade": False}]

        given = "1) strike □ - 6 DMG          --->        strike+ □ - 9 DMG \n" \
                 "2) bludgeon □□ - 18 DMG exhausts         --->        bludgeon+ □□ - 25 DMG exhausts\n" \
                 "3) strike □ - 6 DMG          --->        strike+ □ - 9 DMG \n" \
                 "4) iron wave □ - 5 DMG, 5 BLCK          --->        iron wave+ □ - 7 DMG, 7 BLCK \n" \

        show_deck_upgrade(deck)
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())

        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_deck_upgrade_large(self, mock_output):
        deck = [
            {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
             "upgrade": False},
            {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG",
             "exhaust": True, "upgrade": False},
            {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
             "upgrade": False},
            {"name": "iron wave", "type": "hybrid", "amount": 5, "energy": 1, "description": "5 DMG, 5 BLCK",
             "exhaust": False, "upgrade": False},
            {"name": "iron wave", "type": "hybrid", "amount": 5, "energy": 1, "description": "5 DMG, 5 BLCK",
             "exhaust": False, "upgrade": True}
        ]

        given = "1) strike □ - 6 DMG          --->        strike+ □ - 9 DMG \n" \
                "2) bludgeon □□ - 18 DMG exhausts         --->        bludgeon+ □□ - 25 DMG exhausts\n" \
                "3) strike □ - 6 DMG          --->        strike+ □ - 9 DMG \n" \
                "4) iron wave □ - 5 DMG, 5 BLCK          --->        iron wave+ □ - 7 DMG, 7 BLCK \n" \
                "5) iron wave □ - 5 DMG, 5 BLCK          --->        iron wave+ □ - 7 DMG, 7 BLCK \n" \

        show_deck_upgrade(deck)
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())

        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_deck_upgrade_small(self, mock_output):
        deck = [
            {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG",
             "exhaust": True, "upgrade": False},
            {"name": "iron wave", "type": "hybrid", "amount": 5, "energy": 1, "description": "5 DMG, 5 BLCK",
             "exhaust": False, "upgrade": True}
        ]

        given = "1) bludgeon □□ - 18 DMG exhausts         --->        bludgeon+ □□ - 25 DMG exhausts\n" \
                "2) iron wave □ - 5 DMG, 5 BLCK          --->        iron wave+ □ - 7 DMG, 7 BLCK \n" \

        show_deck_upgrade(deck)
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())

        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_deck_upgrade_one(self, mock_output):
        deck = [
            {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG",
             "exhaust": True, "upgrade": False},
        ]

        given = "1) bludgeon □□ - 18 DMG exhausts         --->        bludgeon+ □□ - 25 DMG exhausts\n" \

        show_deck_upgrade(deck)
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())

        self.assertEqual(expected, given)
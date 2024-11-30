from unittest import TestCase
from cards import *
from unittest.mock import patch
import io

import re


class Test(TestCase):
    def test_card_list_upgraded_strike(self):
        given = {"name": "strike+", "type": "attack", "amount": 9, "energy": 1, "description": "9 DMG", "exhaust": False, "upgrade": True}
        expected = card_list_upgraded("strike")
        self.assertEqual(given, expected)

    def test_card_list_upgraded_defend(self):
        given = {"name": "defend+", "type": "block", "amount": 8, "energy": 1, "description": "8 BLCK", "exhaust": False, "upgrade": True}
        expected = card_list_upgraded("defend")
        self.assertEqual(given, expected)

    def test_card_list_upgraded_bash(self):
        given = {"name": "bash+", "type": "attack", "amount": 13, "energy": 1, "description": "13 DMG", "exhaust": False, "upgrade": True}
        expected = card_list_upgraded("bash")
        self.assertEqual(given, expected)

    def test_card_list_upgraded_invalid(self):
        given = None
        expected = card_list_upgraded("crying developer")
        self.assertEqual(given, expected)
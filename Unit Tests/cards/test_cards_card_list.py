from unittest import TestCase
from cards import *
from unittest.mock import patch
import io

import re


class Test(TestCase):
    def test_card_list_strike(self):
        given = {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False}
        expected = card_list("strike")
        self.assertEqual(given, expected)

    def test_card_list_defend(self):
        given = {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False, "upgrade": False}
        expected = card_list("defend")
        self.assertEqual(given, expected)

    def test_card_list_bash(self):
        given = {"name": "bash", "type": "attack", "amount": 9, "energy": 2, "description": "9 DMG", "exhaust": False, "upgrade": False}
        expected = card_list("bash")
        self.assertEqual(given, expected)

    def test_card_list_invalid(self):
        given = None
        expected = card_list("crying developer")
        self.assertEqual(given, expected)


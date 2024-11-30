from unittest import TestCase

from cards import random_card_reward
from relics import *
from unittest.mock import patch
import io

import re

class Test(TestCase):
    @patch('random.choice', side_effect=["strike"])
    def test_random_card_reward_strike(self, _):
        given = {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False}
        expected = random_card_reward()
        self.assertEqual(expected, given)

    @patch('random.choice', side_effect=["anger"])
    def test_random_card_reward_anger(self, _):
        given = {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                      "exhaust": True, "upgrade": False}
        expected = random_card_reward()
        self.assertEqual(expected, given)

    @patch('random.choice', side_effect=["defend"])
    def test_random_card_reward_defend(self, _):
        given = {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False, "upgrade": False}
        expected = random_card_reward()
        self.assertEqual(expected, given)

    @patch('random.choice', side_effect=["crying developer"])
    def test_random_card_reward_invalid(self, _):
        given = None
        expected = random_card_reward()
        self.assertEqual(expected, given)




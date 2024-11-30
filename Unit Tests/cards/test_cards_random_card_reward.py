from unittest import TestCase

from cards import show_deck_upgrade, random_card_reward
from relics import *
from unittest.mock import patch
import io

import re


class Test(TestCase):
    @patch('random.choice', return_value="strike")
    def test_random_card_reward_strike(self, mock_choice):
        given = {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False}
        expected = random_card_reward()
        self.assertEqual(expected, given)


    @patch('random.choice', return_value="defend")
    def test_random_card_reward_defend(self, mock_choice):
        given = {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False, "upgrade": False}
        expected = random_card_reward()
        self.assertEqual(expected, given)

    @patch('random.choice', return_value="anger")
    def test_random_card_reward_anger(self, mock_choice):
        given = {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                      "exhaust": True, "upgrade": False}
        expected = random_card_reward()
        self.assertEqual(expected, given)

    @patch('random.choice', return_value="bash")
    def test_random_card_reward_bash(self, mock_choice):
        given = {"name": "bash", "type": "attack", "amount": 9, "energy": 2, "description": "9 DMG", "exhaust": False, "upgrade": False}
        expected = random_card_reward()
        self.assertEqual(expected, given)

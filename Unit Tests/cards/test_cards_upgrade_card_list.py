from unittest import TestCase

from cards import upgrade_card_list
from relics import *
from unittest.mock import patch
import io

import re


class Test(TestCase):
    def test_upgrade_card_list_all_available(self):
        deck = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False},
                {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG", "exhaust": True, "upgrade": False},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False},
                {"name": "iron wave", "type": "hybrid", "amount": 5, "energy": 1, "description": "5 DMG, 5 BLCK",
                 "exhaust": False, "upgrade": False}]
        given = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False},
                {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG", "exhaust": True, "upgrade": False},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False},
                {"name": "iron wave", "type": "hybrid", "amount": 5, "energy": 1, "description": "5 DMG, 5 BLCK",
                 "exhaust": False, "upgrade": False}]

        expected = upgrade_card_list(deck)
        self.assertEqual(expected, given)

    def test_upgrade_card_list_one_non_upgraded(self):
        deck = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": True},
                {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG", "exhaust": True, "upgrade": False},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False},
                {"name": "iron wave", "type": "hybrid", "amount": 5, "energy": 1, "description": "5 DMG, 5 BLCK",
                 "exhaust": False, "upgrade": False}]
        given = [{"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG", "exhaust": True, "upgrade": False},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False},
                {"name": "iron wave", "type": "hybrid", "amount": 5, "energy": 1, "description": "5 DMG, 5 BLCK",
                 "exhaust": False, "upgrade": False}]

        expected = upgrade_card_list(deck)
        self.assertEqual(expected, given)

    def test_upgrade_card_list_almost_all_upgraded(self):
        deck = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": True},
                {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG", "exhaust": True, "upgrade": True},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": True},
                {"name": "iron wave", "type": "hybrid", "amount": 5, "energy": 1, "description": "5 DMG, 5 BLCK",
                 "exhaust": False, "upgrade": False}]

        given = [{"name": "iron wave", "type": "hybrid", "amount": 5, "energy": 1, "description": "5 DMG, 5 BLCK",
                 "exhaust": False, "upgrade": False}]

        expected = upgrade_card_list(deck)
        self.assertEqual(expected, given)

    def test_upgrade_card_list_mixed(self):
        deck = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": True},
                {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG", "exhaust": True, "upgrade": False},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False},
                {"name": "iron wave", "type": "hybrid", "amount": 5, "energy": 1, "description": "5 DMG, 5 BLCK",
                 "exhaust": False, "upgrade": True}]
        given = [{"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG", "exhaust": True, "upgrade": False},
                {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False},]

        expected = upgrade_card_list(deck)
        self.assertEqual(expected, given)

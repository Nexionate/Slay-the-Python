from unittest import TestCase
import relics
from relics import *
from unittest.mock import patch
import io
from text import col


class Test(TestCase):
    #@patch("purchase_relic")
    def test_purchase_relic_confirm_gold(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 199, "Relics": []}
        relic = [{"name": 'strike dummy', "description": 'adds +3 DMG to all strikes',
                       "effect": 3, "one-time": False, "rarity": "uncommon"}, 175]
        #mock_get_purchase_relic.return_value = ({"name": 'strike dummy', "description": 'adds +3 DMG to all strikes',
                       #"effect": 3, "one-time": False, "rarity": "uncommon"}, 175)
        given = 24
        purchase_relic(relic, player)
        expected = player["Gold"]
        self.assertEqual(expected, given)

    def test_purchase_relic_confirm_invalid_gold(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        relic = [{"name": 'strike dummy', "description": 'adds +3 DMG to all strikes',
                       "effect": 3, "one-time": False, "rarity": "uncommon"}, 175]
        #mock_get_purchase_relic.return_value = ({"name": 'strike dummy', "description": 'adds +3 DMG to all strikes',
                       #"effect": 3, "one-time": False, "rarity": "uncommon"}, 175)
        given = 99
        purchase_relic(relic, player)
        expected = player["Gold"]
        self.assertEqual(expected, given)

    def test_purchase_relic_confirm_invalid_relic(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        relic = [{"name": 'strike dummy', "description": 'adds +3 DMG to all strikes',
                       "effect": 3, "one-time": False, "rarity": "uncommon"}, 175]
        #mock_get_purchase_relic.return_value = ({"name": 'strike dummy', "description": 'adds +3 DMG to all strikes',
                       #"effect": 3, "one-time": False, "rarity": "uncommon"}, 175)
        given = []
        purchase_relic(relic, player)
        expected = player["Relics"]
        self.assertEqual(expected, given)

    def test_purchase_relic_confirm_valid_relic(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 199, "Relics": []}
        relic = [{"name": 'strike dummy', "description": 'adds +3 DMG to all strikes',
                       "effect": 3, "one-time": False, "rarity": "uncommon"}, 175]
        #mock_get_purchase_relic.return_value = ({"name": 'strike dummy', "description": 'adds +3 DMG to all strikes',
                       #"effect": 3, "one-time": False, "rarity": "uncommon"}, 175)
        given = [{"name": 'strike dummy', "description": 'adds +3 DMG to all strikes',
                  "effect": 3, "one-time": False, "rarity": "uncommon"}]
        purchase_relic(relic, player)
        expected = player["Relics"]
        self.assertEqual(expected, given)


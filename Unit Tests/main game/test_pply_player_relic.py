from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io


class Test(TestCase):
    def test_apply_player_relic_strike_dummy(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": [
                {"name": 'strike dummy', "description": 'adds +3 DMG to all strikes', "effect": 3, "one-time": False,
                 "rarity": "uncommon"}]}
        relic_name = "strike dummy"

        given = True
        expected = apply_player_relic(player, relic_name)
        self.assertEqual(expected, given)

    def test_apply_player_relic_strike_pillow(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": [
                {"name": 'regal pillow', "description": 'resting at campfires completely heals you ', "effect": 60,
                 "one-time": False, "rarity": "common"}]}
        relic_name = "regal pillow"

        given = True
        expected = apply_player_relic(player, relic_name)
        self.assertEqual(expected, given)

    def test_apply_player_relic_stone(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": [
                {"name": 'oddly smooth stone', "description": 'adds +1 to all block', "effect": 1, "one-time": False,
                 "rarity": "common"}]}
        relic_name = "oddly smooth stone"

        given = 1
        apply_player_relic(player, relic_name)
        expected = player["Block"]
        self.assertEqual(expected, given)

    def test_apply_player_relic_slug(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3,
                  "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": [
                {"name": 'prepared slug', "description": 'gain 8 block the first turn of combat', "effect": 8,
                 "one-time": False,
                 "rarity": "uncommon"}]}
        relic_name = "prepared slug"

        given = 8
        apply_player_relic(player, relic_name)
        expected = player["Block"]
        self.assertEqual(expected, given)

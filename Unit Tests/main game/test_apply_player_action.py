from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io

import re


class Test(TestCase):
    def test_apply_player_action_block(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        currentEnemy = {"name": "fat gremlin", "current HP": 25, "max HP": 25, "current block": 8,
                        "attack pattern": False, "attack": [{"damage": 6, "block": 0}, {"damage": 6, "block": 0},
                                                            {"damage": 0, "block": 8}, {"damage": 4, "block": 6}]}
        hand = [{"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
                 "upgrade": False}]
        action = {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK",
                  "exhaust": False,
                  "upgrade": False}
        discard_pile = []
        action_index = 0
        apply_player_action(player, currentEnemy, action, hand, discard_pile, action_index)
        given = 5
        expected = player["Block"]
        self.assertEqual(given, expected)

    def test_apply_player_action_block_with_relic(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99,
                  "Relics": [{"name": 'oddly smooth stone', "description": 'adds +1 to all block', "effect": 1,
                              "one-time": False, "rarity": "common"}]}

        currentEnemy = {"name": "fat gremlin", "current HP": 25, "max HP": 25, "current block": 8,
                        "attack pattern": False, "attack": [{"damage": 6, "block": 0}, {"damage": 6, "block": 0},
                                                            {"damage": 0, "block": 8}, {"damage": 4, "block": 6}]}
        hand = [{"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
                 "upgrade": False}]
        action = {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK",
                  "exhaust": False,
                  "upgrade": False}
        discard_pile = []
        action_index = 0
        apply_player_action(player, currentEnemy, action, hand, discard_pile, action_index)
        given = 6
        expected = player["Block"]
        self.assertEqual(given, expected)

    def test_apply_player_action_attack_enemy_no_block(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99,
                  "Relics": [{"name": 'oddly smooth stone', "description": 'adds +1 to all block', "effect": 1,
                              "one-time": False, "rarity": "common"}]}

        currentEnemy = {"name": "fat gremlin", "current HP": 25, "max HP": 25, "current block": 0,
                        "attack pattern": False, "attack": [{"damage": 6, "block": 0}, {"damage": 6, "block": 0},
                                                            {"damage": 0, "block": 8}, {"damage": 4, "block": 6}]}
        hand = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False}]
        action = {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG",
                  "exhaust": False, "upgrade": False}
        discard_pile = []
        action_index = 0

        apply_player_action(player, currentEnemy, action, hand, discard_pile, action_index)
        given = 19
        expected = currentEnemy["current HP"]
        self.assertEqual(given, expected)

    def test_apply_player_action_attack_enemy_some_block(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99,
                  "Relics": [{"name": 'oddly smooth stone', "description": 'adds +1 to all block', "effect": 1,
                              "one-time": False, "rarity": "common"}]}

        currentEnemy = {"name": "fat gremlin", "current HP": 25, "max HP": 25, "current block": 3,
                        "attack pattern": False, "attack": [{"damage": 6, "block": 0}, {"damage": 6, "block": 0},
                                                            {"damage": 0, "block": 8}, {"damage": 4, "block": 6}]}
        hand = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False}]
        action = {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG",
                  "exhaust": False, "upgrade": False}
        discard_pile = []
        action_index = 0

        apply_player_action(player, currentEnemy, action, hand, discard_pile, action_index)
        given = 22
        expected = currentEnemy["current HP"]
        self.assertEqual(given, expected)

    def test_apply_player_action_attack_enemy_full_block(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99,
                  "Relics": [{"name": 'oddly smooth stone', "description": 'adds +1 to all block', "effect": 1,
                              "one-time": False, "rarity": "common"}]}

        currentEnemy = {"name": "fat gremlin", "current HP": 25, "max HP": 25, "current block": 10,
                        "attack pattern": False, "attack": [{"damage": 6, "block": 0}, {"damage": 6, "block": 0},
                                                            {"damage": 0, "block": 8}, {"damage": 4, "block": 6}]}
        hand = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False}]
        action = {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG",
                  "exhaust": False, "upgrade": False}
        discard_pile = []
        action_index = 0

        apply_player_action(player, currentEnemy, action, hand, discard_pile, action_index)
        given = 25
        expected = currentEnemy["current HP"]
        self.assertEqual(given, expected)

    def test_apply_player_action_card_into_discard(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99,
                  "Relics": [{"name": 'oddly smooth stone', "description": 'adds +1 to all block', "effect": 1,
                              "one-time": False, "rarity": "common"}]}

        currentEnemy = {"name": "fat gremlin", "current HP": 25, "max HP": 25, "current block": 10,
                        "attack pattern": False, "attack": [{"damage": 6, "block": 0}, {"damage": 6, "block": 0},
                                                            {"damage": 0, "block": 8}, {"damage": 4, "block": 6}]}
        hand = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
                 "upgrade": False}]
        action = {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG",
                  "exhaust": False, "upgrade": False}
        discard_pile = []
        action_index = 0

        apply_player_action(player, currentEnemy, action, hand, discard_pile, action_index)
        given = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG",
                  "exhaust": False, "upgrade": False}]
        expected = discard_pile
        self.assertEqual(given, expected)

    def test_apply_player_action_card_exhausts(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99,
                  "Relics": [{"name": 'oddly smooth stone', "description": 'adds +1 to all block', "effect": 1,
                              "one-time": False, "rarity": "common"}]}

        currentEnemy = {"name": "fat gremlin", "current HP": 25, "max HP": 25, "current block": 10,
                        "attack pattern": False, "attack": [{"damage": 6, "block": 0}, {"damage": 6, "block": 0},
                                                            {"damage": 0, "block": 8}, {"damage": 4, "block": 6}]}
        hand = [
            {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG", "exhaust": True,
             "upgrade": False}]
        action = {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG",
                  "exhaust": True, "upgrade": False}
        discard_pile = []
        action_index = 0

        apply_player_action(player, currentEnemy, action, hand, discard_pile, action_index)
        given = []
        expected = discard_pile
        self.assertEqual(given, expected)

    def test_apply_player_action_card_removed_from_hand(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99,
                  "Relics": [{"name": 'oddly smooth stone', "description": 'adds +1 to all block', "effect": 1,
                              "one-time": False, "rarity": "common"}]}

        currentEnemy = {"name": "fat gremlin", "current HP": 25, "max HP": 25, "current block": 10,
                        "attack pattern": False, "attack": [{"damage": 6, "block": 0}, {"damage": 6, "block": 0},
                                                            {"damage": 0, "block": 8}, {"damage": 4, "block": 6}]}
        hand = [
            {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG", "exhaust": True,
             "upgrade": False},
            {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
             "upgrade": False}]
        action = {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG",
                  "exhaust": False,
                  "upgrade": False}
        discard_pile = []
        action_index = 1

        apply_player_action(player, currentEnemy, action, hand, discard_pile, action_index)
        given = [
            {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG", "exhaust": True,
             "upgrade": False}]
        expected = hand
        self.assertEqual(given, expected)

from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io


class Test(TestCase):
    def test_end_player_turn_empty_hand(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        hand = [
            {"name": "strike+", "type": "attack", "amount": 9, "energy": 1, "description": "9 DMG", "exhaust": False,
             "upgrade": True},
            {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
             "upgrade": False},
            {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
             "upgrade": False},
            {"name": "bash", "type": "attack", "amount": 9, "energy": 2, "description": "9 DMG", "exhaust": False,
             "upgrade": False}]
        discard_pile = []
        end_player_turn(player, hand, discard_pile)
        given = []
        expected = hand
        self.assertEqual(given, expected)

    def test_end_player_turn_discard_pile(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        hand = [
            {"name": "strike+", "type": "attack", "amount": 9, "energy": 1, "description": "9 DMG", "exhaust": False,
             "upgrade": True},
            {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
             "upgrade": False},
            {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
             "upgrade": False},
            {"name": "bash", "type": "attack", "amount": 9, "energy": 2, "description": "9 DMG", "exhaust": False,
             "upgrade": False}]
        discard_pile = []
        end_player_turn(player, hand, discard_pile)
        given = [
            {"name": "strike+", "type": "attack", "amount": 9, "energy": 1, "description": "9 DMG", "exhaust": False,
             "upgrade": True},
            {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
             "upgrade": False},
            {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
             "upgrade": False},
            {"name": "bash", "type": "attack", "amount": 9, "energy": 2, "description": "9 DMG", "exhaust": False,
             "upgrade": False}]
        expected = discard_pile
        self.assertEqual(given, expected)

    def test_end_player_turn_hand_2(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        hand = [
            {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
             "upgrade": False},
            {"name": "bash", "type": "attack", "amount": 9, "energy": 2, "description": "9 DMG", "exhaust": False,
             "upgrade": False}]
        discard_pile = []
        end_player_turn(player, hand, discard_pile)
        given = [
            {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
             "upgrade": False},
            {"name": "bash", "type": "attack", "amount": 9, "energy": 2, "description": "9 DMG", "exhaust": False,
             "upgrade": False}]
        expected = discard_pile
        self.assertEqual(given, expected)

    def test_end_player_turn_debuff_hurt_player(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        hand = [
            {"name": "burn", "type": "debuff", "amount": 2, "energy": 1,
             "description": col("red", "2 SELF DMG") + col("!black", "( if in hand by end of turn)"), "exhaust": True},
            {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
             "upgrade": False}]
        discard_pile = []
        end_player_turn(player, hand, discard_pile)
        given = 48
        expected = player["Current HP"]
        self.assertEqual(given, expected)

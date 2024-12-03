from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io

import re


class Test(TestCase):
    @patch('random.choice',
           side_effect=[{"name": "mugger", "current HP": 6, "max HP": 36, "current block": 0, "attack pattern": False,
                         "attack": [{"damage": 7, "block": 0}, {"damage": 11, "block": 0}, {"damage": 5, "block": 7},
                                    {"damage": 0, "block": 8}]}])
    def test_calculate_enemy_diffuculty_reward_normal(self, _):
        event = "fight"

        given = ({"name": "mugger", "current HP": 6, "max HP": 36, "current block": 0, "attack pattern": False,
                  "attack": [{"damage": 7, "block": 0}, {"damage": 11, "block": 0}, {"damage": 5, "block": 7},
                             {"damage": 0, "block": 8}]}, 1)
        expected = calculate_enemy_diffuculty(event)
        self.assertEqual(expected, given)

    @patch('random.choice',
           side_effect=[
               {"name": "gremlin nob", "current HP": 53, "max HP": 53, "current block": 0, "attack pattern": True,
                "attack": [{"damage": 0, "block": 0}, {"damage": 8, "block": 0}, {"damage": 16, "block": 0},
                           {"damage": 20, "block": 0}, {"damage": 20, "block": 0}, {"damage": 20, "block": 0}]}])
    def test_calculate_enemy_diffuculty_reward_elite(self, _):
        event = "elite"

        given = ({"name": "gremlin nob", "current HP": 53, "max HP": 53, "current block": 0, "attack pattern": True,
                  "attack": [{"damage": 0, "block": 0}, {"damage": 8, "block": 0}, {"damage": 16, "block": 0},
                             {"damage": 20, "block": 0}, {"damage": 20, "block": 0}, {"damage": 20, "block": 0}]}, 1.5)
        expected = calculate_enemy_diffuculty(event)
        self.assertEqual(expected, given)

    boss_attacks = [{"damage": 8, "block": 0},
                    {"damage": 6, "block": 0, "debuff": 2},
                    {"damage": 12, "block": 0},
                    {"damage": 6, "block": 12},
                    {"damage": 12, "block": 0},
                    {"damage": 6, "block": 0, "debuff": 2}]

    @patch('random.choice',
           side_effect=[
               {"name": "hexaghost", "current HP": 115, "max HP": 115, "current block": 0, "attack pattern": True,
                "attack":
                    [{"damage": 0, "block": 0}] + (boss_attacks * 5)}])
    def test_calculate_enemy_diffuculty_reward_boss(self, _):
        event = "boss"
        boss_attacks = [{"damage": 8, "block": 0},
                        {"damage": 6, "block": 0, "debuff": 2},
                        {"damage": 12, "block": 0},
                        {"damage": 6, "block": 12},
                        {"damage": 12, "block": 0},
                        {"damage": 6, "block": 0, "debuff": 2}]
        given = ({"name": "hexaghost", "current HP": 115, "max HP": 115, "current block": 0, "attack pattern": True,
                  "attack":
                      [{"damage": 0, "block": 0}] + (boss_attacks * 5)}, 2)
        expected = calculate_enemy_diffuculty(event)
        self.assertEqual(expected, given)

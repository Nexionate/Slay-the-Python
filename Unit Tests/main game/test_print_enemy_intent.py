from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io

import re


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_enemy_intent_block(self, mock_output):
        currentEnemy = {"name": "fat gremlin", "current HP": 25, "max HP": 25, "current block": 0,
                        "attack pattern": False}
        enemyIntent = {"damage": 0, "block": 8}
        print_enemy_intent(currentEnemy, enemyIntent)
        given = "The fat gremlin(25/25) intends to defend for 8 BLCK\n\n"
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_enemy_intent_attack_and_block(self, mock_output):
        currentEnemy = {"name": "fat gremlin", "current HP": 17, "max HP": 25, "current block": 0,
                        "attack pattern": False}
        enemyIntent = {"damage": 8, "block": 3}
        print_enemy_intent(currentEnemy, enemyIntent)
        given = "The fat gremlin(17/25) intends to attack for 8 DMG and defend for 3 BLCK\n\n"
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_enemy_intent_big_attack(self, mock_output):
        currentEnemy = {"name": "gremlin nob", "current HP": 53, "max HP": 53, "current block": 0,
                        "attack pattern": True,
                        "attack": [{"damage": 0, "block": 0}, {"damage": 8, "block": 0}, {"damage": 16, "block": 0}]}

        enemyIntent = {"damage": 16, "block": 0}
        print_enemy_intent(currentEnemy, enemyIntent)
        given = "The gremlin nob(53/53) intends to attack for 16 DMG\n\n"
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_enemy_intent_already_block(self, mock_output):
        currentEnemy = {"name": "gremlin nob", "current HP": 53, "max HP": 53, "current block": 10,
                        "attack pattern": True,
                        "attack": [{"damage": 0, "block": 0}, {"damage": 8, "block": 0}, {"damage": 16, "block": 0}]}

        enemyIntent = {"damage": 16, "block": 0}
        print_enemy_intent(currentEnemy, enemyIntent)
        given = "The gremlin nob(53/53)⦻10 intends to attack for 16 DMG\n\n"
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_enemy_intent_unknown(self, mock_output):
        currentEnemy = {"name": "fat gremlin", "current HP": 25, "max HP": 25, "current block": 0,
                        "attack pattern": False}
        enemyIntent = {"damage": 0, "block": 0}
        print_enemy_intent(currentEnemy, enemyIntent)
        given = "The fat gremlin(25/25) intends to UNKNOWN (not attack)\n\n"
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_enemy_intent_debuff_attack(self, mock_output):
        currentEnemy = {"name": "fat gremlin", "current HP": 25, "max HP": 25, "current block": 0,
                        "attack pattern": False}
        enemyIntent = {"damage": 6, "block": 0, "debuff": 2}
        print_enemy_intent(currentEnemy, enemyIntent)
        given = "The fat gremlin(25/25) intends to attack for 6 DMG and debuff you\n\n"
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_enemy_intent_debuff_block(self, mock_output):
        currentEnemy = {"name": "fat gremlin", "current HP": 25, "max HP": 25, "current block": 0,
                        "attack pattern": False}
        enemyIntent = {"damage": 0, "block": 6, "debuff": 2}
        print_enemy_intent(currentEnemy, enemyIntent)
        given = "The fat gremlin(25/25) intends to defend for 6 BLCK and debuff you\n\n"
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())
        self.assertEqual(expected, given)

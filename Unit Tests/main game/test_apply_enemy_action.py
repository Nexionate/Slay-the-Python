from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io


class Test(TestCase):

    @patch('time.sleep', return_value=None)
    def test_apply_enemy_action_block(self, mock_sleep):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        currentEnemy = {"name": "fat gremlin", "current HP": 25, "max HP": 25, "current block": 0,
                        "attack pattern": False}
        enemyIntent = {"damage": 0, "block": 8}
        draw_pile = []
        apply_enemy_action(enemyIntent, currentEnemy, player, draw_pile)
        given = 8
        expected = currentEnemy["current block"]
        self.assertEqual(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('time.sleep', return_value=None)
    def test_apply_enemy_action_block_print(self, mock_sleep, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        currentEnemy = {"name": "mugger", "current HP": 36, "max HP": 36, "current block": 0, "attack pattern": False}
        enemyIntent = {"damage": 0, "block": 8}
        draw_pile = []
        apply_enemy_action(enemyIntent, currentEnemy, player, draw_pile)
        given = f"The mugger defends for {col("cyan", " ⦻8 BLCK")}\n{col("!black", "The enemy's turn ends.. \n")}\n"
        expected = mock_output.getvalue()
        self.assertEqual(given, expected)

    @patch('time.sleep', return_value=None)
    def test_apply_enemy_action_hit_player_HP(self, mock_sleep):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        currentEnemy = {"name": "mugger", "current HP": 36, "max HP": 36, "current block": 0, "attack pattern": False}
        enemyIntent = {"damage": 7, "block": 0}
        draw_pile = []
        apply_enemy_action(enemyIntent, currentEnemy, player, draw_pile)
        given = 43
        expected = player["Current HP"]
        self.assertEqual(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('time.sleep', return_value=None)
    def test_apply_enemy_action_hit_player_print(self, mock_sleep, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        currentEnemy = {"name": "mugger", "current HP": 36, "max HP": 36, "current block": 0, "attack pattern": False}
        enemyIntent = {"damage": 7, "block": 0}
        draw_pile = []
        apply_enemy_action(enemyIntent, currentEnemy, player, draw_pile)
        given = f"The mugger hits you for {col("!red", "7 DMG")}\n{col("!black", "The enemy's turn ends.. \n")}\n"
        expected = mock_output.getvalue()
        self.assertEqual(given, expected)

    @patch('time.sleep', return_value=None)
    def test_apply_enemy_action_block_and_attack_HP(self, mock_sleep):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        currentEnemy = {"name": "mugger", "current HP": 36, "max HP": 36, "current block": 0, "attack pattern": False}
        enemyIntent = {"damage": 7, "block": 7}
        draw_pile = []
        apply_enemy_action(enemyIntent, currentEnemy, player, draw_pile)
        given = (43, 7)
        expected = (player["Current HP"], currentEnemy["current block"])
        self.assertEqual(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('time.sleep', return_value=None)
    def test_apply_enemy_action_block_and_attack_print(self, mock_sleep, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        currentEnemy = {"name": "mugger", "current HP": 36, "max HP": 36, "current block": 0, "attack pattern": False}
        enemyIntent = {"damage": 7, "block": 7}
        draw_pile = []
        apply_enemy_action(enemyIntent, currentEnemy, player, draw_pile)
        given = f"The mugger hits you for {col("!red", "7 DMG")}\n" \
                f"The mugger defends for {col("cyan", " ⦻7 BLCK")}\n" \
                f"{col("!black", "The enemy's turn ends.. \n")}\n"
        expected = mock_output.getvalue()
        self.assertEqual(given, expected)

    @patch('time.sleep', return_value=None)
    def test_apply_enemy_action_hit_player_blocked(self, mock_sleep):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 3, "Gold": 99, "Relics": []}
        currentEnemy = {"name": "mugger", "current HP": 36, "max HP": 36, "current block": 0, "attack pattern": False}
        enemyIntent = {"damage": 7, "block": 0}
        draw_pile = []
        apply_enemy_action(enemyIntent, currentEnemy, player, draw_pile)
        given = 46
        expected = player["Current HP"]
        self.assertEqual(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('time.sleep', return_value=None)
    def test_apply_enemy_action_hit_player_print(self, mock_sleep, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 3, "Gold": 99, "Relics": []}
        currentEnemy = {"name": "mugger", "current HP": 36, "max HP": 36, "current block": 0, "attack pattern": False}
        enemyIntent = {"damage": 7, "block": 0}
        draw_pile = []
        apply_enemy_action(enemyIntent, currentEnemy, player, draw_pile)
        given = f"The mugger hits you for {col("!red", "4 DMG")}\n{col("!black", "The enemy's turn ends.. \n")}\n"
        expected = mock_output.getvalue()
        self.assertEqual(given, expected)

    @patch('time.sleep', return_value=None)
    def test_apply_enemy_action_debuff_player_cards(self, mock_sleep):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 3, "Gold": 99, "Relics": []}
        currentEnemy = {"name": "mugger", "current HP": 36, "max HP": 36, "current block": 0, "attack pattern": False}
        enemyIntent = {"damage": 0, "block": 0, "debuff": 2}
        draw_pile = []
        apply_enemy_action(enemyIntent, currentEnemy, player, draw_pile)
        given = [{"name": "burn", "type": "debuff", "amount": 2, "energy": 1,
                  "description": col("red", "2 SELF DMG") + col("!black", "( if in hand by end of turn)"),
                  "exhaust": True}, {"name": "burn", "type": "debuff", "amount": 2, "energy": 1,
                                     "description": col("red", "2 SELF DMG") + col("!black",
                                                                                   "( if in hand by end of turn)"),
                                     "exhaust": True}]
        expected = draw_pile
        self.assertEqual(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('time.sleep', return_value=None)
    def test_apply_enemy_action_debuff_player_print(self, mock_sleep, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 3, "Gold": 99, "Relics": []}
        currentEnemy = {"name": "mugger", "current HP": 36, "max HP": 36, "current block": 0, "attack pattern": False}
        enemyIntent = {"damage": 0, "block": 0, "debuff": 2}
        draw_pile = []

        apply_enemy_action(enemyIntent, currentEnemy, player, draw_pile)
        given = (f"The mugger adds {col("!red", "2 burns")} to your {col("!green", "Draw pile")}\n"
                 f"{col("!black", "The enemy's turn ends.. \n")}\n")
        expected = mock_output.getvalue()
        self.assertEqual(given, expected)

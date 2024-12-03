from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io
import re


# f"2) oddly smooth stone - 165 gold\n- adds +1 to all block\n\n"
class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_purchase_shop_enough_gold_item_2(self, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 199, "Relics": []}
        relics_sale = [
            [{"name": 'strike dummy', "description": 'adds +3 DMG to all strikes', "effect": 3, "one-time": False,
              "rarity": "uncommon"}, 220],

            [{"name": 'oddly smooth stone', "description": 'adds +1 to all block', "effect": 1, "one-time": False,
              "rarity": "common"}, 160],

            [{"name": 'regal pillow', "description": 'resting at campfires completely heals you ', "effect": 60,
              "one-time": False, "rarity": "common"}, 150],

            [{"name": 'blood vial', "description": 'heal 3HP before every battle', "effect": 3, "one-time": False,
              "rarity": "common"}, 153]]
        player_input = 2
        valid_purchase_shop(player, relics_sale, player_input)
        given = f"Relic Purchased!\n" \
                f"1) strike dummy - 220 gold\n- adds +3 DMG to all strikes\n\n" \
                f"2) regal pillow - 150 gold\n- resting at campfires completely heals you \n\n" \
                f"3) blood vial - 153 gold\n- heal 3HP before every battle\n\n"
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_purchase_shop_enough_gold_item_3(self, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 199, "Relics": []}
        relics_sale = [
            [{"name": 'strike dummy', "description": 'adds +3 DMG to all strikes', "effect": 3, "one-time": False,
              "rarity": "uncommon"}, 220],

            [{"name": 'oddly smooth stone', "description": 'adds +1 to all block', "effect": 1, "one-time": False,
              "rarity": "common"}, 160],

            [{"name": 'regal pillow', "description": 'resting at campfires completely heals you ', "effect": 60,
              "one-time": False, "rarity": "common"}, 150],

            [{"name": 'blood vial', "description": 'heal 3HP before every battle', "effect": 3, "one-time": False,
              "rarity": "common"}, 153]]
        player_input = 3
        valid_purchase_shop(player, relics_sale, player_input)
        given = f"Relic Purchased!\n" \
                f"1) strike dummy - 220 gold\n- adds +3 DMG to all strikes\n\n" \
                f"2) oddly smooth stone - 160 gold\n- adds +1 to all block\n\n" \
                f"3) blood vial - 153 gold\n- heal 3HP before every battle\n\n"
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_purchase_shop_all_purchased(self, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 299, "Relics": []}
        relics_sale = [
            [{"name": 'strike dummy', "description": 'adds +3 DMG to all strikes', "effect": 3, "one-time": False,
              "rarity": "uncommon"}, 220]]
        player_input = 1
        valid_purchase_shop(player, relics_sale, player_input)
        given = f"Relic Purchased!\n"
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_purchase_shop_not_enough_gold(self, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 199, "Relics": []}
        relics_sale = [
            [{"name": 'strike dummy', "description": 'adds +3 DMG to all strikes', "effect": 3, "one-time": False,
              "rarity": "uncommon"}, 220],

            [{"name": 'oddly smooth stone', "description": 'adds +1 to all block', "effect": 1, "one-time": False,
              "rarity": "common"}, 160],

            [{"name": 'regal pillow', "description": 'resting at campfires completely heals you ', "effect": 60,
              "one-time": False, "rarity": "common"}, 150],

            [{"name": 'blood vial', "description": 'heal 3HP before every battle', "effect": 3, "one-time": False,
              "rarity": "common"}, 153]]
        player_input = 1
        valid_purchase_shop(player, relics_sale, player_input)
        given = f"Insufficient Gold!\n"
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())
        self.assertEqual(expected, given)

from unittest import TestCase
from relics import *
from unittest.mock import patch
import io

import re


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_shop_relics_full_stock(self, mock_output):
        shop_list = [({"name": 'strike dummy', "description": 'adds +3 DMG to all strikes',
                      "effect": 3, "one-time": False, "rarity": "uncommon"}, 175),
                     ({"name": 'oddly smooth stone', "description": 'adds +1 to all block',
                       "effect": 1, "one-time": False, "rarity": "common"}, 165),
                     ({"name": 'regal pillow', "description": 'resting at campfires completely heals you ',
                       "effect": 60,
                       "one-time": False, "rarity": "common"}, 143),
                     ({"name": 'coffee dripper', "description": 'permanently gain +1 Max Energy', "effect": 1,
                       "one-time": True,
                       "rarity": "rare"}, 275)]
        given = (f"1) strike dummy - 175 gold\n- adds +3 DMG to all strikes\n\n"
                 f"2) oddly smooth stone - 165 gold\n- adds +1 to all block\n\n"
                 f"3) regal pillow - 143 gold\n- resting at campfires completely heals you \n\n"
                 f"4) coffee dripper - 275 gold\n- permanently gain +1 Max Energy\n\n")

        print_shop_relics(shop_list)
        expected = re.sub(r'\x1b\[.*?m', '',mock_output.getvalue())

        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_shop_relics_half_stock(self, mock_output):
        shop_list = [({"name": 'strike dummy', "description": 'adds +3 DMG to all strikes',
                       "effect": 3, "one-time": False, "rarity": "uncommon"}, 175),
                     ({"name": 'oddly smooth stone', "description": 'adds +1 to all block',
                       "effect": 1, "one-time": False, "rarity": "common"}, 165)]
        given = (f"1) strike dummy - 175 gold\n- adds +3 DMG to all strikes\n\n"
                 f"2) oddly smooth stone - 165 gold\n- adds +1 to all block\n\n")

        print_shop_relics(shop_list)
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())

        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_shop_relics_middle_bought(self, mock_output):
        shop_list = [({"name": 'strike dummy', "description": 'adds +3 DMG to all strikes',
                       "effect": 3, "one-time": False, "rarity": "uncommon"}, 175),
                     ({"name": 'regal pillow', "description": 'resting at campfires completely heals you ',
                       "effect": 60,
                       "one-time": False, "rarity": "common"}, 143),
                     ({"name": 'coffee dripper', "description": 'permanently gain +1 Max Energy', "effect": 1,
                       "one-time": True,
                       "rarity": "rare"}, 275)]
        given = (f"1) strike dummy - 175 gold\n- adds +3 DMG to all strikes\n\n"
                 f"2) regal pillow - 143 gold\n- resting at campfires completely heals you \n\n"
                 f"3) coffee dripper - 275 gold\n- permanently gain +1 Max Energy\n\n")

        print_shop_relics(shop_list)
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())

        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_shop_relics_all_bought(self, mock_output):
        shop_list = []
        given = ""

        print_shop_relics(shop_list)
        expected = re.sub(r'\x1b\[.*?m', '', mock_output.getvalue())

        self.assertEqual(expected, given)

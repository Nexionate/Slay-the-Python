from unittest import TestCase
from relics import *


class Test(TestCase):
    def test_relic_one_time_buff_gold(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        relic = {"name": 'old coin', "description": 'immediately gain 300 gold', "effect": 300,
                 "one-time": True, "rarity": "uncommon"}
        relic_one_time_buff(relic, player)
        given = 399
        self.assertEqual(player["Gold"], given)

    def test_relic_one_time_buff_strawberry(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        relic = {"name": 'strawberry',
                 "description": 'gain 10 Max HP',
                 "effect": 10, "one-time": True, "rarity": "common"}
        relic_one_time_buff(relic, player)
        given = 60
        self.assertEqual(player["Max HP"], given)

    def test_relic_one_time_buff_coffee(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        relic = {"name": 'coffee dripper', "description": 'permanently gain +1 Max Energy', "effect": 1,
                 "one-time": True,
                 "rarity": "rare"}
        relic_one_time_buff(relic, player)
        given = 4
        self.assertEqual(player["Max Energy"], given)

    def test_relic_one_time_buff_stone(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        relic = {"name": 'philosophers stone', "description": 'permanently gain +1 Max Energy', "effect": 1,
                 "one-time": True,
                 "rarity": "rare"}
        relic_one_time_buff(relic, player)
        given = 6
        self.assertEqual(player["Max Draw"], given)

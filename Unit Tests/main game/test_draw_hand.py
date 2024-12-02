from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io
from text import col
import re
import random


#  {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
#              "upgrade": False},
#             {"name": "defend", "type": "block", "amount": 5, "energy": 1, "description": "5 BLCK", "exhaust": False,
#              "upgrade": False},
#             {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
#              "upgrade": False},
#             {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False,
#              "upgrade": False},
#             {"name": "bash", "type": "attack", "amount": 9, "energy": 2, "description": "9 DMG", "exhaust": False,
#              "upgrade": False}

class Test(TestCase):
    # @patch('random.choice')
    def test_draw_hand_full_hand(self):
        draw_pile = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        hand = []
        amount = 4
        discard_pile = []

        given = ([5, 6, 7, 8, 9], [1, 2, 3, 4], [])
        expected = draw_hand(draw_pile, hand, discard_pile, amount)
        self.assertEqual(expected, given)

    def test_draw_hand_six_cards(self):
        draw_pile = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        hand = []
        amount = 6
        discard_pile = []

        given = ([7, 8, 9], [1, 2, 3, 4, 5, 6], [])
        expected = draw_hand(draw_pile, hand, discard_pile, amount)
        self.assertEqual(expected, given)

    @patch('random.shuffle', return_value=[9, 8, 7, 6, 5, 4, 3, 2, 1])
    def test_draw_hand_shuffle_discard(self, mock_shuffle):
        draw_pile = []
        hand = []
        discard_pile = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        amount = 4

        given = ([5, 6, 7, 8, 9], [1, 2, 3, 4], [])
        expected = draw_hand(draw_pile, hand, discard_pile, amount)

        self.assertEqual(expected, given)

    @patch('random.shuffle', return_value=[9, 8, 7, 6, 5, 4, 3, 2, 1])
    def test_draw_hand_shuffle_discard_half_full_draw_pile(self, mock_shuffle):
        draw_pile = [1, 2]
        hand = []
        discard_pile = [3, 4, 5, 6, 7, 8, 9]
        amount = 4

        given = ([5, 6, 7, 8, 9], [1, 2, 3, 4], [])
        expected = draw_hand(draw_pile, hand, discard_pile, amount)

        self.assertEqual(expected, given)

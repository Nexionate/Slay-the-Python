from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io

import re


class Test(TestCase):
    @patch('builtins.input', side_effect=["take"])
    def test_valid_input_reward_confirm_take(self, _):
        given = (True, "take")
        expected = valid_input_reward()
        self.assertEqual(expected, given)

    @patch('builtins.input', side_effect=["yes"])
    def test_valid_input_reward_confirm_yes(self, _):
        given = (True, "yes")
        expected = valid_input_reward()
        self.assertEqual(expected, given)

    @patch('builtins.input', side_effect=["no"])
    def test_valid_input_reward_deny_no(self, _):
        given = (True, "no")
        expected = valid_input_reward()
        self.assertEqual(expected, given)

    @patch('builtins.input', side_effect=["skip"])
    def test_valid_input_reward_deny_skip(self, _):
        given = (True, "skip")
        expected = valid_input_reward()
        self.assertEqual(expected, given)

    @patch('builtins.input', side_effect=["crying developer"])
    def test_valid_input_fire_invalid(self, _):
        given = (False, "crying developer")
        expected = valid_input_reward()
        self.assertEqual(expected, given)

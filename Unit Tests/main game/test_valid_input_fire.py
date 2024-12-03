from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io

import re


class Test(TestCase):
    @patch('builtins.input', side_effect=["heal"])
    def test_valid_input_fire_heal(self, _):
        given = (True, "heal")
        expected = valid_input_fire()
        self.assertEqual(expected, given)

    @patch('builtins.input', side_effect=["rest"])
    def test_valid_input_fire_rest(self, _):
        given = (True, "rest")
        expected = valid_input_fire()
        self.assertEqual(expected, given)

    @patch('builtins.input', side_effect=["upgrade"])
    def test_valid_input_fire_upgrade(self, _):
        given = (True, "upgrade")
        expected = valid_input_fire()
        self.assertEqual(expected, given)

    @patch('builtins.input', side_effect=["smith"])
    def test_valid_input_fire_smith(self, _):
        given = (True, "smith")
        expected = valid_input_fire()
        self.assertEqual(expected, given)

    @patch('builtins.input', side_effect=["crying developer"])
    def test_valid_input_fire_invalid(self, _):
        given = (False, "crying developer")
        expected = valid_input_fire()
        self.assertEqual(expected, given)

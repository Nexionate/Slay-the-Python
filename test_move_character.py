from unittest import TestCase
from main_game import move_character


class Test(TestCase):
    def test_move_character_W(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        movement = "W"

        given = move_character(player, movement)
        expected = {"X-coordinate": 0, "Y-coordinate": -1, "Current HP": 5}
        self.assertEqual(expected, given)

    def test_move_character_A(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        movement = "A"

        given = move_character(player, movement)
        expected = {"X-coordinate": -1, "Y-coordinate": 0, "Current HP": 5}
        self.assertEqual(expected, given)

    def test_move_character_S(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        movement = "S"

        given = move_character(player, movement)
        expected = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        self.assertEqual(expected, given)

    def test_move_character_D(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        movement = "D"

        given = move_character(player, movement)
        expected = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        self.assertEqual(expected, given)

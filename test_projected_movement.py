from unittest import TestCase
from main_game import projected_movement


class Test(TestCase):
    def test_projected_movement_W(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}

        actual = projected_movement(player, "W")
        expected = (0, -1)
        self.assertEqual(expected, actual)

    def test_projected_movement_A(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}

        actual = projected_movement(player, "A")
        expected = (-1, 0)
        self.assertEqual(expected, actual)

    def test_projected_movement_S(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}

        actual = projected_movement(player, "S")
        expected = (0, 1)
        self.assertEqual(expected, actual)

    def test_projected_movement_D(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}

        actual = projected_movement(player, "D")
        expected = (1, 0)
        self.assertEqual(expected, actual)

    def test_projected_movement_error(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}

        actual = projected_movement(player, "WEEEEEEEEEEEEEEEEE!")
        expected = "Error"
        self.assertEqual(expected, actual)
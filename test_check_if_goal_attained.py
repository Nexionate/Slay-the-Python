from unittest import TestCase
from main_game import check_if_goal_attained


class Test(TestCase):
    def test_check_if_goal_attained_small_not_reached(self):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        given = check_if_goal_attained(player, 2, 2)
        expected = False
        self.assertEqual(expected, given)

    def test_check_if_goal_attained_small_reached(self):
        player = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        given = check_if_goal_attained(player, 2, 2)
        expected = True
        self.assertEqual(expected, given)

    def test_check_if_goal_attained_med_not_reached(self):
        player = {"X-coordinate": 3, "Y-coordinate": 2, "Current HP": 5}
        given = check_if_goal_attained(player, 5, 5)
        expected = False
        self.assertEqual(expected, given)

    def test_check_if_goal_attained_med_close(self):
        player = {"X-coordinate": 3, "Y-coordinate": 4, "Current HP": 5}
        given = check_if_goal_attained(player, 5, 5)
        expected = False
        self.assertEqual(expected, given)

    def test_check_if_goal_attained_med_reached(self):
        player = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 5}
        given = check_if_goal_attained(player, 5, 5)
        expected = True
        self.assertEqual(expected, given)

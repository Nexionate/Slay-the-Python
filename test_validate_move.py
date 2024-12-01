from unittest import TestCase
from main_game import validate_move


class Test(TestCase):
    def test_validate_move_upper_left_W(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        movement = "W"

        given = validate_move(board, player, movement)
        expected = False
        self.assertEqual(expected, given)

    def test_validate_move_upper_left_A(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        movement = "A"

        given = validate_move(board, player, movement)
        expected = False
        self.assertEqual(expected, given)

    def test_validate_move_upper_left_S(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        movement = "S"

        given = validate_move(board, player, movement)
        expected = True
        self.assertEqual(expected, given)

    def test_validate_move_upper_left_D(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        movement = "D"

        given = validate_move(board, player, movement)
        expected = True
        self.assertEqual(expected, given)

    def test_validate_move_upper_right_W(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        movement = "W"

        given = validate_move(board, player, movement)
        expected = False
        self.assertEqual(expected, given)

    def test_validate_move_upper_right_A(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        movement = "A"

        given = validate_move(board, player, movement)
        expected = True
        self.assertEqual(expected, given)

    def test_validate_move_upper_right_S(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        movement = "S"

        given = validate_move(board, player, movement)
        expected = True
        self.assertEqual(expected, given)

    def test_validate_move_upper_right_D(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        movement = "D"

        given = validate_move(board, player, movement)
        expected = False
        self.assertEqual(expected, given)

    def test_validate_move_bottom_left_W(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        movement = "W"

        given = validate_move(board, player, movement)
        expected = True
        self.assertEqual(expected, given)

    def test_validate_move_bottom_left_A(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        movement = "A"

        given = validate_move(board, player, movement)
        expected = False
        self.assertEqual(expected, given)

    def test_validate_move_bottom_left_S(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        movement = "S"

        given = validate_move(board, player, movement)
        expected = False
        self.assertEqual(expected, given)

    def test_validate_move_bottom_left_D(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        movement = "D"

        given = validate_move(board, player, movement)
        expected = True
        self.assertEqual(expected, given)

    def test_validate_move_bottom_right_W(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        movement = "W"

        given = validate_move(board, player, movement)
        expected = True
        self.assertEqual(expected, given)

    def test_validate_move_bottom_right_A(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        movement = "A"

        given = validate_move(board, player, movement)
        expected = True
        self.assertEqual(expected, given)

    def test_validate_move_bottom_right_S(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        movement = "S"

        given = validate_move(board, player, movement)
        expected = False
        self.assertEqual(expected, given)

    def test_validate_move_bottom_right_D(self):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'swamp', (1, 1): 'dark forest'}
        player = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        movement = "D"

        given = validate_move(board, player, movement)
        expected = False
        self.assertEqual(expected, given)


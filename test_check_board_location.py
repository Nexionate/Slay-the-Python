from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from main_game import check_board_location


class Test(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_board_location_first(self, mock_output):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'hills', (1, 1): 'dark forest'}
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}

        check_board_location(board, player, False)
        expected = "You are now in: coast-side at co-ords(0, 0)\n\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_board_location_second(self, mock_output):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'hills', (1, 1): 'dark forest'}
        player = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}

        check_board_location(board, player, False)
        expected = "You are now in: hills at co-ords(1, 0)\n\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_board_location_third(self, mock_output):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'hills', (1, 1): 'dark forest'}
        player = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}

        check_board_location(board, player, False)
        expected = "You are now in: hills at co-ords(0, 1)\n\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_board_location_fourth(self, mock_output):
        board = {(0, 0): 'coast-side', (0, 1): 'hills', (1, 0): 'hills', (1, 1): 'dark forest'}
        player = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}

        check_board_location(board, player, False)
        expected = "You are now in: dark forest at co-ords(1, 1)\n\n"
        self.assertEqual(expected, mock_output.getvalue())

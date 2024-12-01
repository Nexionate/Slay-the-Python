from unittest import TestCase
from initialize_game import *
from unittest.mock import patch
import io
from colorama import Fore, Back, Style, init
init(autoreset=True)


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_board_shop_colour(self, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        cord_dic = {(0, 0): 'start', (0, 1): 'fight', (0, 2): 'fight', (0, 3): 'fight', (0, 4): 'event',
                    (1, 0): 'fight',
                    (1, 1): 'fight', (1, 2): 'fight', (1, 3): 'fight', (1, 4): 'fight', (2, 0): 'fight',
                    (2, 1): 'fight',
                    (2, 2): 'shop', (2, 3): 'fight', (2, 4): 'fight', (3, 0): 'fight', (3, 1): 'fire', (3, 2): 'fight',
                    (3, 3): 'elite', (3, 4): 'fight', (4, 0): 'fight', (4, 1): 'fight', (4, 2): 'shop', (4, 3): 'fight',
                    (4, 4): '\x1b[41m\x1b[93mfire\x1b[0m\x1b[0m'}
        print_board(cord_dic, player)
        expected = mock_output.getvalue()

        given = Fore.MAGENTA + "shop"

        self.assertIn(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_board_elite_colour(self, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        cord_dic = {(0, 0): 'start', (0, 1): 'fight', (0, 2): 'fight', (0, 3): 'fight', (0, 4): 'event',
                    (1, 0): 'fight',
                    (1, 1): 'fight', (1, 2): 'fight', (1, 3): 'fight', (1, 4): 'fight', (2, 0): 'fight',
                    (2, 1): 'fight',
                    (2, 2): 'shop', (2, 3): 'fight', (2, 4): 'fight', (3, 0): 'fight', (3, 1): 'fire', (3, 2): 'fight',
                    (3, 3): 'elite', (3, 4): 'fight', (4, 0): 'fight', (4, 1): 'fight', (4, 2): 'shop', (4, 3): 'fight',
                    (4, 4): '\x1b[41m\x1b[93mfire\x1b[0m\x1b[0m'}
        print_board(cord_dic, player)
        expected = mock_output.getvalue()

        given = Fore.RED + "elite"
        self.assertIn(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_board_empty_colour(self, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        cord_dic = {(0, 0): 'start', (0, 1): 'empty', (0, 2): 'fight', (0, 3): 'fight', (0, 4): 'event',
                    (1, 0): 'fight',
                    (1, 1): 'fight', (1, 2): 'fight', (1, 3): 'empty', (1, 4): 'fight', (2, 0): 'fight',
                    (2, 1): 'fight',
                    (2, 2): 'shop', (2, 3): 'fight', (2, 4): 'fight', (3, 0): 'fight', (3, 1): 'fire', (3, 2): 'fight',
                    (3, 3): 'elite', (3, 4): 'fight', (4, 0): 'fight', (4, 1): 'fight', (4, 2): 'shop', (4, 3): 'fight',
                    (4, 4): '\x1b[41m\x1b[93mfire\x1b[0m\x1b[0m'}
        print_board(cord_dic, player)
        expected = mock_output.getvalue()

        given = "empty"
        self.assertIn(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_board_fire_colour(self, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        cord_dic = {(0, 0): 'start', (0, 1): 'empty', (0, 2): 'fight', (0, 3): 'fight', (0, 4): 'event',
                    (1, 0): 'fight',
                    (1, 1): 'fight', (1, 2): 'fight', (1, 3): 'empty', (1, 4): 'fight', (2, 0): 'fight',
                    (2, 1): 'fight',
                    (2, 2): 'shop', (2, 3): 'fight', (2, 4): 'fight', (3, 0): 'fight', (3, 1): 'fire', (3, 2): 'fight',
                    (3, 3): 'elite', (3, 4): 'fight', (4, 0): 'fight', (4, 1): 'fight', (4, 2): 'shop', (4, 3): 'fight',
                    (4, 4): '\x1b[41m\x1b[93mfire\x1b[0m\x1b[0m'}
        print_board(cord_dic, player)
        expected = mock_output.getvalue()

        given = Fore.YELLOW + "fire"
        self.assertIn(given, expected)

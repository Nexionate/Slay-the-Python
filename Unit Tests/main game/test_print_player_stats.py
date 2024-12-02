from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io
from text import col


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_stats_full_health_full_energy(self, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        print_player_stats(player)
        # {col("!cyan", "")}
        expected = mock_output.getvalue()
        given = f"{(col("green", "■") * 10)}  50/50{col("!green", " HP ")} {(col("!yellow", "□") * 3)} 3/3{col("!yellow", " energy")}\n"
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_stats_half_health_full_energy(self, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 34, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        print_player_stats(player)
        # {col("!cyan", "")}
        expected = mock_output.getvalue()
        given = f"{(col("green", "■") * 6)}{(col("red", "■") * 4)}  34/50{col("!green", " HP ")} {(col("!yellow", "□") * 3)} 3/3{col("!yellow", " energy")}\n"
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_stats_low_health_full_energy(self, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 11, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 3, "Block": 0, "Gold": 99, "Relics": []}
        print_player_stats(player)
        # {col("!cyan", "")}
        expected = mock_output.getvalue()
        given = f"{(col("green", "■") * 2)}{(col("red", "■") * 8)}  11/50{col("!green", " HP ")} {(col("!yellow", "□") * 3)} 3/3{col("!yellow", " energy")}\n"
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_stats_half_health_2_energy(self, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 34, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 2, "Block": 0, "Gold": 99, "Relics": []}
        print_player_stats(player)
        # {col("!cyan", "")}
        expected = mock_output.getvalue()
        given = f"{(col("green", "■") * 6)}{(col("red", "■") * 4)}  34/50{col("!green", " HP ")} {(col("!yellow", "□") * 2)} 2/3{col("!yellow", " energy")}\n"
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_stats_half_health_1_energy(self, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 34, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 1, "Block": 0, "Gold": 99, "Relics": []}
        print_player_stats(player)
        # {col("!cyan", "")}
        expected = mock_output.getvalue()
        given = f"{(col("green", "■") * 6)}{(col("red", "■") * 4)}  34/50{col("!green", " HP ")} {(col("!yellow", "□") * 1)} 1/3{col("!yellow", " energy")}\n"
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_stats_half_health_0_energy(self, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 34, "Max HP": 50, "Max Energy": 3, "Max Draw": 4,
                  "Current Energy": 0, "Block": 0, "Gold": 99, "Relics": []}
        print_player_stats(player)
        # {col("!cyan", "")}
        expected = mock_output.getvalue()
        given = f"{(col("green", "■") * 6)}{(col("red", "■") * 4)}  34/50{col("!green", " HP ")} {(col("!yellow", "□") * 0)} 0/3{col("!yellow", " energy")}\n"
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_stats_half_health_4_energy(self, mock_output):
        player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 34, "Max HP": 50, "Max Energy": 4, "Max Draw": 4,
                  "Current Energy": 4, "Block": 0, "Gold": 99, "Relics": []}
        print_player_stats(player)
        # {col("!cyan", "")}
        expected = mock_output.getvalue()
        given = f"{(col("green", "■") * 6)}{(col("red", "■") * 4)}  34/50{col("!green", " HP ")} {(col("!yellow", "□") * 4)} 4/4{col("!yellow", " energy")}\n"
        self.assertEqual(expected, given)

from unittest import TestCase
from relics import *
from unittest.mock import patch
import io
from text import col


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_relic_description_ex1(self, mock_output):
        relic = {"name": 'prepared slug', "description": 'gain 8 block the first turn of combat',
                 "effect": 8, "one-time": False, "rarity": "uncommon"}
        print_relic_description(relic)
        given = mock_output.getvalue()
        expected = f"{col("!magenta", "prepared slug")}\n{col("magenta", "- gain 8 block the first turn of combat")}\n"
        self.assertEqual(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_relic_description_ex2(self, mock_output):
        relic = {"name": 'blood vial', "description": 'heal 3HP before every battle', "effect": 3, "one-time": False, "rarity": "common"}
        print_relic_description(relic)
        given = mock_output.getvalue()
        expected = f"{col("!magenta", "blood vial")}\n{col("magenta", "- heal 3HP before every battle")}\n"
        self.assertEqual(given, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_relic_description_one_time_use(self, mock_output):
        relic = {"name": 'old coin', "description": 'immediately gain 300 gold', "effect": 300,
                 "one-time": True, "rarity": "uncommon"}
        print_relic_description(relic)
        given = mock_output.getvalue()
        expected = f"{col("!magenta", "old coin")} {col("!black", "300")}\n{col("magenta", "- immediately gain 300 gold")}\n"
        self.assertEqual(given, expected)

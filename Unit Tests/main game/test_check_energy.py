from unittest import TestCase
from main_game import *
from unittest.mock import patch
import io


class Test(TestCase):
    def test_check_energy_playable(self):
        energy = 3
        card = {"name": "bash", "type": "attack", "amount": 9, "energy": 2, "description": "9 DMG", "exhaust": False,
                "upgrade": False}
        given = True
        expected = check_energy(energy, card)
        self.assertEqual(expected, given)

    def test_check_energy_playable_2_energy(self):
        energy = 2
        card = {"name": "bash", "type": "attack", "amount": 9, "energy": 2, "description": "9 DMG", "exhaust": False,
                "upgrade": False}
        given = True
        expected = check_energy(energy, card)
        self.assertEqual(expected, given)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_energy_invalid_print(self, mock_output):
        energy = 1
        card = {"name": "bash", "type": "attack", "amount": 9, "energy": 2, "description": "9 DMG", "exhaust": False,
                "upgrade": False}
        given = col("!black", "Insufficient Energy!") + "\n"
        check_energy(energy, card)
        expected = mock_output.getvalue()
        self.assertEqual(expected, given)

    def test_check_energy_invalid(self):
        energy = 1
        card = {"name": "bash", "type": "attack", "amount": 9, "energy": 2, "description": "9 DMG", "exhaust": False,
                "upgrade": False}
        given = False

        expected = check_energy(energy, card)
        self.assertEqual(expected, given)

    def test_check_energy_playable_0_energy(self):
        energy = 2
        card = {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                "exhaust": True, "upgrade": False}
        given = True
        expected = check_energy(energy, card)
        self.assertEqual(expected, given)

    def test_check_energy_playable_0_energy_cost(self):
        energy = 0
        card = {"name": "anger", "type": "attack", "amount": 7, "energy": 0, "description": "7 DMG",
                "exhaust": True, "upgrade": False}
        given = True
        expected = check_energy(energy, card)
        self.assertEqual(expected, given)

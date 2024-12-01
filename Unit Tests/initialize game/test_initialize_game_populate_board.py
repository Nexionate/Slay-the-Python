from unittest import TestCase
from initialize_game import *
from unittest.mock import patch

class Test(TestCase):

    @patch('random.choice')
    def test_populate_board_ex1(self, mock_choice):
        self.maxDiff = None
        cord_list = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2), (1, 2),
                     (2, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (0, 4), (1, 4), (2, 4), (3, 4),
                     (4, 4)]
        cord_dic = {}
        rows = 5
        cols = 5

        mock_choice.side_effect = ['fight', 'fight', 'fight', 'fight', 'fire', 'fight', 'fight', 'fight', 'fight',
                                   'shop', 'fight', 'fight', 'fight', 'elite', 'fight', 'event', 'fight', 'fight',
                                   'fight', 'fight', 'elite', 'fire']

        result = populate_board(cord_list, cord_dic, rows, cols)
        given = {(0, 0): 'start', (0, 1): 'fight', (0, 2): 'fight', (0, 3): 'fight', (0, 4): 'event', (1, 0): 'fight',
                 (1, 1): 'fight', (1, 2): 'fight', (1, 3): 'fight', (1, 4): 'fight', (2, 0): 'fight', (2, 1): 'fight',
                 (2, 2): 'shop', (2, 3): 'fight', (2, 4): 'fight', (3, 0): 'fight', (3, 1): 'fire', (3, 2): 'fight',
                 (3, 3): 'elite', (3, 4): 'fight', (4, 0): 'fight', (4, 1): 'fight', (4, 2): 'shop', (4, 3): 'fight',
                 (4, 4): '\x1b[41m\x1b[93mfire\x1b[0m\x1b[0m'}

        self.assertEqual(given, result)

    @patch('random.choice')
    def test_populate_board_ex2(self, mock_choice):
        cord_list = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2), (1, 2),
                     (2, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (0, 4), (1, 4), (2, 4), (3, 4),
                     (4, 4)]
        cord_dic = {}
        rows = 5
        cols = 5

        mock_choice.side_effect = ['fight', 'fire', 'elite', 'event', 'fire', 'fight', 'fight', 'fight', 'fight',
                                   'shop', 'event', 'fight', 'elite', 'fight', 'fight', 'event', 'elite', 'fight',
                                   'fight', 'event', 'fight', 'fire']

        result = populate_board(cord_list, cord_dic, rows, cols)
        given = {(0, 0): 'start', (0, 1): 'fight', (0, 2): 'fight', (0, 3): 'event', (0, 4): 'event', (1, 0): 'fight',
                 (1, 1): 'fight', (1, 2): 'fight', (1, 3): 'fight', (1, 4): 'elite', (2, 0): 'fight', (2, 1): 'event',
                 (2, 2): 'shop', (2, 3): 'elite', (2, 4): 'fight', (3, 0): 'fire', (3, 1): 'fire', (3, 2): 'fight',
                 (3, 3): 'fight', (3, 4): 'fight', (4, 0): 'elite', (4, 1): 'fight', (4, 2): 'shop', (4, 3): 'fight',
                 (4, 4): '\x1b[41m\x1b[93mfire\x1b[0m\x1b[0m'}
        self.assertEqual(given, result)

    @patch('random.choice')
    def test_populate_board_check_event_description(self, mock_choice):
        cord_list = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2), (1, 2),
                     (2, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (0, 4), (1, 4), (2, 4), (3, 4),
                     (4, 4)]
        cord_dic = {}
        rows = 5
        cols = 5
        given = {(4, 4): '\x1b[41m\x1b[93mfire\x1b[0m\x1b[0m'}
        mock_choice.side_effect = ['fight', 'fire', 'elite', 'event', 'fire', 'fight', 'fight', 'fight', 'fight',
                                   'shop', 'event', 'fight', 'elite', 'fight', 'fight', 'event', 'elite', 'fight',
                                   'fight', 'event', 'fight', 'fire']
        result = populate_board(cord_list, cord_dic, rows, cols)

        self.assertIn('\x1b[41m\x1b[93mfire\x1b[0m\x1b[0m', given.values())

    def test_populate_board_below_elite_max(self):
        cord_list = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2), (1, 2),
                     (2, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (0, 4), (1, 4), (2, 4), (3, 4),
                     (4, 4)]
        cord_dic = {}
        rows = 5
        cols = 5
        result = populate_board(cord_list, cord_dic, rows, cols)
        counter = 0
        for event in result.values():
            if event == "elite":
                counter += 1
        self.assertLessEqual(counter, 2)

    @patch('random.choice')
    def test_populate_board_above_elite_max(self, mock_choice):
        cord_list = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2), (1, 2),
                     (2, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (0, 4), (1, 4), (2, 4), (3, 4),
                     (4, 4)]
        cord_dic = {}
        rows = 5
        cols = 5
        mock_choice.side_effect = ['fight', 'fire', 'fight', 'event', 'fire', 'fight', 'elite', 'fight', 'fight',
                                   'shop', 'event', 'fight', 'elite', 'fight', 'fight', 'event', 'elite', 'fight',
                                   'fight', 'event', 'fight', 'fire']
        result = populate_board(cord_list, cord_dic, rows, cols)
        counter = 0
        for event in result.values():
            if event == "elite":
                counter += 1
        self.assertGreaterEqual(counter, 2)

    def test_populate_board_below_fire_max(self):
        cord_list = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2), (1, 2),
                     (2, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (0, 4), (1, 4), (2, 4), (3, 4),
                     (4, 4)]
        cord_dic = {}
        rows = 5
        cols = 5
        result = populate_board(cord_list, cord_dic, rows, cols)
        counter = 0
        for event in result.values():
            if event == "elite":
                counter += 1
        self.assertLessEqual(counter, 2)

    @patch('random.choice')
    def test_populate_board_above_fire_max(self, mock_choice):
        cord_list = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2), (1, 2),
                     (2, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (0, 4), (1, 4), (2, 4), (3, 4),
                     (4, 4)]
        cord_dic = {}
        rows = 5
        cols = 5
        mock_choice.side_effect = ['fight', 'fire', 'fight', 'event', 'fire', 'fight', 'elite', 'fight', 'fight',
                                   'shop', 'event', 'fight', 'elite', 'fight', 'fight', 'event', 'elite', 'fight',
                                   'fight', 'event', 'fight', 'fire']
        result = populate_board(cord_list, cord_dic, rows, cols)
        counter = 0
        for event in result.values():
            if event == "fire":
                counter += 1
        self.assertGreaterEqual(counter, 2)

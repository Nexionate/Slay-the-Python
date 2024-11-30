from unittest import TestCase

from cards import add_upgrade_card


class Test(TestCase):
    def test_add_upgrade_card_in_deck(self):
        deck = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False}, \
                ]

        card = {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False}

        given = [{"name": "strike+", "type": "attack", "amount": 9, "energy": 1, "description": "9 DMG", "exhaust": False, "upgrade": True}]
        add_upgrade_card(deck, card)
        expected = deck
        self.assertEqual(expected, given)

    def test_add_upgrade_card_if_upgraded(self):
        deck = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False}, \
                ]

        card = {"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False}

        given = True
        add_upgrade_card(deck, card)
        expected = deck[0]["upgrade"]
        self.assertEqual(expected, given)

    def test_add_upgrade_card_multiple_cards(self):
        deck = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False}, \
                {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG", "exhaust": True, "upgrade": False}]

        card = {"name": "bludgeon", "type": "attack", "amount": 18, "energy": 2, "description": "18 DMG", "exhaust": True, "upgrade": False}

        given = [{"name": "strike", "type": "attack", "amount": 6, "energy": 1, "description": "6 DMG", "exhaust": False, "upgrade": False},
                 {"name": "bludgeon+", "type": "attack", "amount": 25, "energy": 2, "description": "25 DMG", "exhaust": True, "upgrade": True}]
        add_upgrade_card(deck, card)
        expected = deck
        self.assertEqual(expected, given)

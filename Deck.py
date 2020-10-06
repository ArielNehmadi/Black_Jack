# Deck class - group of Card class
# Attributes - all_cards(an array of all 52 cards)
# Functions - shuffle , deal_one
import random

from Black_Jack.Card import Card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        """
        This function shuffles the deck (doesn't return anything)
        """
        random.shuffle(self.all_cards)

    def deal_one(self):
        """
        This function take 1 card of the top of all_cards array
        """
        return self.all_cards.pop()

# Deck class - group of Card class
# Attributes - all_cards(an array of all 52 cards)
# Functions - shuffle , deal_one
import random

from Black_Jack.Card import Card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Deck:

    def __init__(self):

        self.all_cards = []
        #
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

# Player class - Main Class
# Attributes - name chips and hand
from Black_Jack.Chips import Chips
from Black_Jack.Hand import Hand


class Player:

    def __init__(self, name):
        self.name = name
        self.chips = Chips()
        self.hand = Hand()

# Hand class
# Attributes - my_hand(an array of the current cards held)
#            - hand_value : sum of card value
#            - bust : the player exceeds 21
#            - stand : the player doesn't hit anymore
#            - ace : number of aces with an 11 value


class Hand:

    def __init__(self):
        self.my_hand = []
        self.hand_value = 0
        self.ace = 0
        # bust False if the player is still in the round

    def print_(self, name):
        """
        Prints the current hand and hand sum
        """
        print(f'{name} current hand is: ')
        for card in self.my_hand:
            print(card)
        print(f'{name} current hand value is: {str(self.hand_value)} \n ')

    def is_bust(self):
        """
        checks if the players hand value exceeds 21
        out: False for Bust, True for not
        """
        if self.hand_value > 21:
            if self.ace > 0:
                self.ace -= 1
                self.hand_value -= 10
            if self.hand_value > 21:
                return False
        else:
            return True

    def hit(self, deck):
        """

        adds the players hit to my_hand
        adds the new card to hand_value
        updates ace sum

        """
        # takes from deck and puts in my_hand
        card = deck.deal_one()
        self.my_hand.append(card)
        # adds the new card value to hand_value
        self.hand_value += self.my_hand[-1].value
        # if new card is an ace adds 1 to self.ace
        if self.my_hand[-1].rank == 'Ace':
            self.ace += 1

    def stand_or_hit(self, deck, name):
        """
        this loop represents the players turn to complete a hand
        asks and validates user input about weather to stand or hit.
        repeat until the player busts or stands
        output: True for Stand , False for Bust
        """
        while self.is_bust():
            while True:

                player_input = input("Do you want to hit or stand? (h = hit , s = stand)")
                if player_input == 'h':
                    self.hit(deck)
                    self.print_(name)
                    break

                elif player_input == 's':
                    return True
                else:
                    print('please enter s or h')
        return False

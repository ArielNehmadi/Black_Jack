# Chips class
# Attributes - total , bet
# Functions - win_bet , lose_bet , take_bet
class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def __str__(self):
        return self.total

    def win_bet(self):
        print('You won the round !!!')
        self.total += self.bet
        print('Current chips: ' + str(self.total))

    def lose_bet(self):
        print('You lost the round !!!')
        self.total -= self.bet
        print('Current chips: ' + str(self.total))

    def take_bet(self):

        while True:
            try:
                print('your current money is: ' + str(self.total))
                bet_amount = int(input('Enter your bet money here:'))
                if 0 < bet_amount <= self.total:
                    self.bet = bet_amount
                    break
                else:
                    print(f'Not Enough Chips, please enter a number matching your current chips count. \n you have: '
                          f'{str(self.total)} chips')

            except:
                print('Invalid input, Please enter a number: ')

        return bet_amount

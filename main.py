# Black Jack by. Ariel Nehmadi

# Imports
from Black_Jack.Deck import Deck
from Black_Jack.Hand import Hand
from Black_Jack.Player import Player

print("Welcome to BlackJack")

# Pre Game set up : Create Player & ask for name , give a cash out option
my_player = Player(input('Enter your name here: '))
cash_in = True

# Game starts here: ext condition(cash out or no more chips)
while cash_in and my_player.chips.total != 0:
    # set up round here

    # Create a deck and shuffle it
    my_deck = Deck()
    my_deck.shuffle()

    # Create a dealer with a hand Class
    dealer = Hand()

    # Add 2 card to Player's hand and 1 card to dealer's hand

    my_player.hand.hit(my_deck)
    my_player.hand.hit(my_deck)
    dealer.hit(my_deck)

    # Print to the player his cards and the dealers card
    my_player.hand.print_(my_player.name)
    dealer.print_('Dealer')

    # Ask for bet
    my_player.chips.take_bet()

    # Players Turn to complete a hand
    # Stand_bust = stand : True , bust : False
    player_stand_bust = my_player.hand.stand_or_hit(my_deck, my_player.name)

    # If player stands, complete dealers hand
    if player_stand_bust:
        # Complete dealers hand

        # Check if bust
        dealer_stand_bust = True
        # hit until hand is above 17
        while dealer.hand_value <= 17:
            dealer.hit(my_deck)
            if not dealer.is_bust():
                dealer_stand_bust = False
        # Print Dealers hand
        dealer.print_('Dealer')

        # Check if the dealer busted
        if dealer_stand_bust:
            # Both dealer and player didn't bust
            # compere their hand values
            if dealer.hand_value > my_player.hand.hand_value:
                # The dealer won
                my_player.chips.lose_bet()
            elif dealer.hand_value < my_player.hand.hand_value:
                # The player won
                my_player.chips.win_bet()
            else:
                # Draw
                print('The round is a DRAW')
        else:
            # The Dealer busted
            # The player won
            print('The dealer Busted')
            my_player.chips.win_bet()
    else:
        # The player has lost
        print('You busted')
        my_player.chips.lose_bet()
    # Clear player hand
    my_player.hand = Hand()

    # check if the player has 0 chips
    if my_player.chips.total != 0:
        # check if the player wants to cash out
        while True:
            players_choice = input('Do you want to cash out? (Y/N)')
            if players_choice == 'Y':
                # The player wants to cash out
                cash_in = False
                break

            elif players_choice == 'N':
                # The player want's another round
                break
            else:
                print('Please enter a valid input (Y/N)')
# Game ends here
# print the players total

if my_player.chips.total < 100:
    print('my god you really are an addict ')
    print(f'you have: {str(my_player.chips.total)} chips')
else:
    print("well you beat a pretty bad computer, I wouldn't brag about that")
    print(f'you have: {str(my_player.chips.total)} chips')
print('\n Thank you for playing BlackJack')

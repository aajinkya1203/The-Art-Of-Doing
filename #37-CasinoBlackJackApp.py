import random
import time
# all classes here
class Card():
    def __init__(self, rank, value, suit):
        self.rank = rank
        self.value = value
        self.suit = suit
    
    def display_card(self):
        print(self.rank,'of',self.suit)

class Deck():
    def __init__(self):
        self.cards = []

    def build_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = {
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            '10':10,
            'J':10,
            'Q':10,
            'K':10,
            'A':11
        }
        for suit in suits:
            for rank, value in ranks.items():
                card = Card( rank, value, suit )
                self.cards.append( card )
    
    def shuffle_deck(self):
        random.shuffle( self.cards )
    
    def deal_card(self):
        card = self.cards.pop()
        return card

class Player():
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self, deck):
        for i in range(2):
            self.hand.append( deck.deal_card() )
    
    def display_hand(self):
        print("\nDeclaring Player's hand:")
        for card in self.hand:
            card.display_card()
        
    def hit(self, deck):
        card = deck.deal_card()
        self.hand.append( card )

    def get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = False
        # Updating the current value of hand_value by adding the current cards value.
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == 'A':
                ace_in_hand = True
        # Treat the Ace as if it were 1 instead of 11
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10
        print('\nTotal value at hand:',self.hand_value)
    
    def update_hand(self, deck):
        # If the value of the players current hand is less than 21
        if self.hand_value < 21:
            choice = input("\nWould you like to hit (y/n): ")
            # asking the user if he/she would like to hit
            if choice.startswith('y'):
                self.hit(deck)
            elif choice.startswith('n'):
                self.playing_hand = False
            else:
                print("Invalid input!\nWe will assume it is a no!")
                self.playing_hand = False
        # the player either has blackjack or is over 21
        else:
            self.playing_hand = False

class Dealer():
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.playing_hand = True
    
    def draw_hand(self, deck):
        for i in range(2):
            self.hand.append( deck.deal_card() )

    def display_hand(self):
        input("\nPress any key to reveal the dealers card:")
        for card in self.hand:
            card.display_card()
            time.sleep(1)

    def get_hand_value(self):
        self.hand_value = 0
        ace_in_hand = False
        # Updating the current value of hand_value by adding the current cards value.
        for card in self.hand:
            self.hand_value += card.value
            if card.rank == 'A':
                ace_in_hand = True
        # Treat the Ace as if it were 1 instead of 11
        if self.hand_value > 21 and ace_in_hand:
            self.hand_value -= 10
        print('\nTotal value at hand:',self.hand_value)
        
    def hit(self, deck):
        self.get_hand_value()
        while self.hand_value < 17:
            card = deck.deal_card()
            self.hand.append( card )
            self.get_hand_value()
        print("\nDealer is set with a total of",len( self.hand ),"cards.")

class Game():
    def __init__(self, amount):
        self.amount = amount
        self.bet = 20
        self.winner = ''
    
    def set_bet(self):
        betting = True
        while betting:
            user_input = int(input("How much would you like to bet (minimum of 20): "))
            if user_input < 20:
                user_input = 20
            
            if user_input > self.amount:
                print("\nYou cannot afford the bet!")
            else:
                self.bet = user_input
                betting = False
        
    def scoring(self, p_hand, d_hand):
        if p_hand == 21:
            print("\nWohoo! You got Black Jack!")
            self.winner = 'p'
        elif d_hand == 21:
            print("\nYaya! Dealer got Black Jack!")
            self.winner = 'd'
        elif p_hand > 21:
            self.winner = 'd'
            print("\nYou went over 21...you loose!")
        elif d_hand > 21:
            self.winner = 'p'
            print("\nDealer went over 21.")
        else:
            if p_hand > d_hand:
                print("\nPlayer's Hand:",p_hand,"\nDealer's Hand:",d_hand)
                print("\nPlayer's hand was greater than the Dealer's hand!\nYou win! :)")
                self.winner = 'p'
            elif p_hand < d_hand:
                print("\nPlayer's Hand:",p_hand,"\nDealer's Hand:",d_hand)
                print("\nDealer's hand was greater than the Player's hand!\nYou lose! :(")
                self.winner ='d'
            else:
                print("\nPlayer's Hand:",p_hand,"\nDealer's Hand:",d_hand)
                print("\nIt was a tie! No one wins!")
                self.winner = "tie"

    def payout(self):
        if self.winner == 'p':
            self.amount += self.bet
        elif self.winner == 'd':
            self.amount -= self.bet

    def display_money(self):
        print("\nCurrent Money: $",self.amount)
    
    def display_money_and_bet(self):
        print("\nCurrent Money: $",self.amount,"\tCurrent Bet: $",self.bet)
    

# real game starts here

# intro messages
print("Welcome to the Black Jack App!")
print('The minimum bet at this table is $20')

# current bet
user_money = int(input("How much money would you like to bet: "))

# creating object of class Game
game = Game( user_money )

# setting a flag to help exit the while loop
playing = True

while True:
    # creating an object of Deck Class
    game_deck = Deck()

    # building the deck
    game_deck.build_deck()

    # shuffling the deck
    game_deck.shuffle_deck()

    # creating object of Player and Dealer object
    player = Player()
    dealer = Dealer()

    # getting game's current money
    game.display_money()

    # getting the bet of the game
    game.set_bet()

    # player and dealer draws a hand
    player.draw_hand(game_deck)
    dealer.draw_hand(game_deck)

    # displaing game's money and bet
    game.display_money_and_bet()

    # revealing the dealer's first hand
    print("\nThe dealer reveals it's first hand as",dealer.hand[0].rank,"of",dealer.hand[0].suit)

    # player's hand
    while player.playing_hand:
        player.display_hand()
        player.get_hand_value()
        player.update_hand(game_deck)

    dealer.hit(game_deck)
    dealer.display_hand()

    game.scoring(player.hand_value, dealer.hand_value)
    game.payout()

    if game.amount < 20:
        playing = False
        print("Sorry, you ran out of money. Please try again.")
    
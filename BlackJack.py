import random

# DECK CLASS - Represents a standard deck of 52 playing cards
class Deck:
    def __init__(self):
        """
        Initialize a new deck of cards.
        Creates 52 cards: 13 ranks in each of 4 suits.
        Ace is initialized with value 11, face cards with value 10.
        """
        self.cards = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
        ]

        # Create a Card object for each suit-rank combination
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """
        Shuffle the deck of cards using random.shuffle().
        Only shuffles if there are at least 2 cards in the deck.
        """
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        """
        Deal a specified number of cards from the deck.
        
        Args:
            number: Number of cards to deal
            
        Returns:
            list: List of dealt Card objects
        """
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()  # Remove and return the top card
                cards_dealt.append(card)
        return cards_dealt


# CARD CLASS - Represents a single playing card
class Card:
    def __init__(self, suit, rank):
        """
        Initialize a card with a suit and rank.
        
        Args:
            suit (str): The card's suit (spades, clubs, hearts, diamonds)
            rank (dict): Dictionary containing the rank and its numerical value
        """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Return string representation of the card (e.g., 'A of spades')"""
        return f"{self.rank['rank']} of {self.suit}"


# HAND CLASS - Represents a player's or dealer's hand of cards
class Hand:
    def __init__(self, dealer=False):
        """
        Initialize a hand of cards.
        
        Args:
            dealer (bool): True if this is the dealer's hand, False for player's hand
        """
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        """Add a list of cards to the hand"""
        self.cards.extend(card_list)

    def calculate_value(self):
        """
        Calculate the total value of the hand.
        Handles the special case of Ace being worth 1 or 11.
        """
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True

        # If hand value exceeds 21 and we have an ace, reduce its value to 1
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        """Calculate and return the current value of the hand"""
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        """Check if the hand is a blackjack (value of 21)"""
        return self.get_value() == 21

    def display(self, show_all_dealer_cards=False):
        """
        Display all cards in the hand.
        
        Args:
            show_all_dealer_cards (bool): If True, show dealer's hidden card
        """
        print(f'''{"Dealer's" if self.dealer else "Your"} Hand: ''')
        for index, card in enumerate(self.cards):
            # Hide dealer's first card unless specified otherwise
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                print("Hidden")
            else:
                print(card)

        if not self.dealer:
            print("Value: ", self.get_value())
        print()


# CLASS GAME - Manages the game flow and rules
class Game:
    def play(self):
        """Main game loop that manages the entire blackjack game"""
        game_number = 0
        games_to_play = 0

        # Get number of games from player with input validation
        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many Games do you want to play? "))
            except:
                print("You must enter a number.")

        # Main game loop
        while game_number < games_to_play:
            game_number += 1

            # Initialize and shuffle deck
            deck = Deck()
            deck.shuffle()

            # Create hands for player and dealer
            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            # Deal initial cards
            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            # Display game header and initial hands
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            # Check for immediate blackjack
            if self.check_winner(player_hand, dealer_hand):
                continue

            # Player's turn - hit or stand
            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                print()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Please Enter 'Hit' or 'Stand' (or H/S): ").lower()
                    print()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()

            # Check if player busted
            if self.check_winner(player_hand, dealer_hand):
                continue

            # Dealer's turn - must hit on 16 or below
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            # Check if dealer busted
            if self.check_winner(player_hand, dealer_hand):
                continue

            # Show final hands and determine winner
            print("Final results")
            print("Your hand: ", player_hand_value)
            print("Dealer's hand: ", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True)

        print("\nThanks for playing the Game !")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        """
        Determine the winner of the current game.
        
        Args:
            player_hand (Hand): The player's hand
            dealer_hand (Hand): The dealer's hand
            game_over (bool): True if this is the final winner check
            
        Returns:
            bool: True if game should end, False if game should continue
        """
        if not game_over:
            # Check for busts and blackjacks
            if player_hand.get_value() > 21:
                print("You Busted! Dealer wins! 😭")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer Busted! You win! 🥳")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both Players have BlackJack. TIE! 😑")
                return True
            elif player_hand.is_blackjack():
                print("You have BlackJack! You win! 🥳")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has BlackJack! Dealer wins! 😭")
                return True
        else:
            # Compare final hand values
            if player_hand.get_value() > dealer_hand.get_value():
                print("You Win! 🥳")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("Tie! 😑")
            else:
                print("Dealer Wins! 😭")
        return False


def play_blackjack():
    """Create and start a new blackjack game"""
    game = Game()
    game.play()


# Only run the game if this file is run directly (not imported)
if __name__ == "__main__":
    play_blackjack()
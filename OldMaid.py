import random

def create_deck():
    """
    Create a standard deck of 52 playing cards.
    Returns a list of dictionaries, where each dictionary represents a card
    with 'rank' and 'suit' key-value pairs.
    """
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    return deck

def remove_queen(deck):
    """
    Remove one random Queen from the deck to create the "Old Maid" card.
    
    Args:
        deck (list): List of card dictionaries
    Returns:
        list: Modified deck with one Queen removed
    """
    queens = [card for card in deck if card['rank'] == 'Queen']
    deck.remove(random.choice(queens))  # Remove one Queen randomly
    return deck

def deal_cards(deck):
    """
    Shuffle and deal cards evenly between two players.
    
    Args:
        deck (list): List of card dictionaries
    Returns:
        tuple: Two lists representing player1's and player2's hands
    """
    random.shuffle(deck)
    player1 = deck[:len(deck)//2]
    player2 = deck[len(deck)//2:]
    return player1, player2

def remove_pairs(hand):
    """
    Remove all pairs of cards with matching ranks from a player's hand.
    
    Args:
        hand (list): List of card dictionaries
    Returns:
        tuple: (Modified hand without pairs, Number of pairs removed)
    """
    ranks = [card['rank'] for card in hand]
    # Find ranks that appear exactly twice (pairs)
    pairs = set([rank for rank in ranks if ranks.count(rank) == 2])
    
    # Create new hand excluding the paired cards
    new_hand = [card for card in hand if card['rank'] not in pairs]
    return new_hand, len(pairs)

def display_hand(hand, player_name):
    """
    Display all cards in a player's hand with numbering.
    
    Args:
        hand (list): List of card dictionaries
        player_name (str): Name of the player whose hand is being displayed
    """
    print(f"\n{player_name}'s hand:")
    for i, card in enumerate(hand):
        print(f"{i + 1}: {card['rank']} of {card['suit']}")

def human_draw_card(human_hand, computer_hand):
    """
    Handle human player's turn to draw a card from computer's hand.
    
    Args:
        human_hand (list): Human player's cards
        computer_hand (list): Computer's cards
    Returns:
        tuple: Updated human and computer hands
    """
    if not computer_hand:
        return human_hand, computer_hand
    
    display_hand(computer_hand, "Computer")
    choice = int(input("Choose a card to draw (1 to {}): ".format(len(computer_hand)))) - 1
    
    # Handle valid and invalid card selections
    if 0 <= choice < len(computer_hand):
        card_drawn = computer_hand.pop(choice)
        human_hand.append(card_drawn)
        print(f"You drew: {card_drawn['rank']} of {card_drawn['suit']}")
    else:
        print("Invalid choice. Drawing a random card.")
        card_drawn = random.choice(computer_hand)
        computer_hand.remove(card_drawn)
        human_hand.append(card_drawn)
        print(f"You drew: {card_drawn['rank']} of {card_drawn['suit']}")
    
    return human_hand, computer_hand

def computer_draw_card(computer_hand, human_hand):
    """
    Handle computer's turn to draw a card from human's hand.
    
    Args:
        computer_hand (list): Computer's cards
        human_hand (list): Human player's cards
    Returns:
        tuple: Updated computer and human hands
    """
    if not human_hand:
        return computer_hand, human_hand
    
    # Computer randomly selects a card from human's hand
    card_drawn = random.choice(human_hand)
    human_hand.remove(card_drawn)
    computer_hand.append(card_drawn)
    print(f"Computer drew a card from you.")
    
    return computer_hand, human_hand

def play_old_maid():
    """
    Main game loop for Old Maid card game.
    Manages game setup, turn rotation, and win condition checking.
    """
    # Initialize game by creating and preparing deck
    deck = create_deck()
    deck = remove_queen(deck)
    human, computer = deal_cards(deck)
    
    # Remove initial pairs from both hands
    human, pairs_human = remove_pairs(human)
    computer, pairs_computer = remove_pairs(computer)
    
    print("Initial pairs removed:")
    print(f"Human has {pairs_human} pairs.")
    print(f"Computer has {pairs_computer} pairs.")
    
    # Main game loop - alternate between human and computer turns
    turn = 0  # 0 for Human, 1 for Computer
    while len(human) > 0 and len(computer) > 0:
        if turn == 0:
            print("\n--- Human's Turn ---")
            display_hand(human, "Your")
            human, computer = human_draw_card(human, computer)
            human, pairs_human = remove_pairs(human)
            print(f"You have {len(human)} cards left.")
        else:
            print("\n--- Computer's Turn ---")
            computer, human = computer_draw_card(computer, human)
            computer, pairs_computer = remove_pairs(computer)
            print(f"Computer has {len(computer)} cards left.")
        
        turn = 1 - turn  # Switch turns between 0 and 1
    
    # Determine and announce the winner
    if len(human) == 1:
        print("\nYou are the Old Maid! You lose!")
    else:
        print("\nThe Computer is the Old Maid! You win!")

# Only run the game if this file is run directly
if __name__ == "__main__":
    play_old_maid()
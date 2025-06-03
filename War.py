import random

def create_deck():
    """
    Create and return a new deck of 52 playing cards.
    Each card is a dictionary containing suit, rank, and numeric value.
    Ace is highest with value 14, followed by King (13), Queen (12), etc.
    """
    deck = []
    suits = ["spades", "clubs", "hearts", "diamonds"]
    ranks = [
        {"rank": "Ace", "value": 14}, {"rank": "2", "value": 2}, {"rank": "3", "value": 3},
        {"rank": "4", "value": 4}, {"rank": "5", "value": 5}, {"rank": "6", "value": 6},
        {"rank": "7", "value": 7}, {"rank": "8", "value": 8}, {"rank": "9", "value": 9},
        {"rank": "10", "value": 10}, {"rank": "Jack", "value": 11}, {"rank": "Queen", "value": 12},
        {"rank": "King", "value": 13}
    ]

    # Create each card by combining suits and ranks
    for suit in suits:
        for rank in ranks:
            deck.append({"suit": suit, "rank": rank["rank"], "value": rank["value"]})
    return deck

def shuffle_deck(deck):
    """
    Shuffle the given deck of cards using random.shuffle().
    Only shuffles if deck has more than one card.
    
    Args:
        deck (list): List of card dictionaries
    Returns:
        list: Shuffled deck of cards
    """
    if len(deck) > 1:
        random.shuffle(deck)
    return deck

def draw_card(deck, player):
    """
    Draw a card from the deck for the specified player.
    
    Args:
        deck (list): List of card dictionaries
        player (str): Name of the player drawing the card
    Returns:
        dict: Drawn card dictionary, or None if deck is empty
    """
    if len(deck) > 0:
        card = deck.pop()  # Remove and return top card
        print(player + " drew the " + printable_card(card))
        return card
    else:
        print("No cards left in the deck!")
        return None

def printable_card(card):
    """
    Convert a card dictionary to a readable string format.
    
    Args:
        card (dict): Card dictionary with rank and suit
    Returns:
        str: String representation of the card (e.g., "Ace of spades")
    """
    return f"{card['rank']} of {card['suit']}"

def handle_round(deck, player_one_score, player_two_score):
    """
    Handle a single round of the War card game.
    
    Args:
        deck (list): Current deck of cards
        player_one_score (int): Current score of player one
        player_two_score (int): Current score of player two
    Returns:
        tuple: (round_result, updated_player_one_score, updated_player_two_score)
        or None if deck is empty
    """
    # Draw cards for both players
    player_one_card = draw_card(deck, "Player one")
    player_two_card = draw_card(deck, "Player two")

    # Check if deck has enough cards to continue
    if player_one_card is None or player_two_card is None:
        return None, player_one_score, player_two_score

    # Compare cards and determine round winner
    if player_one_card["value"] > player_two_card["value"]:
        winner = "Player one wins!!!"
        player_one_score += 2
    elif player_two_card["value"] > player_one_card["value"]:
        winner = "Player Two wins!!!"
        player_two_score += 2
    else:
        # Cards match - initiate tiebreaker
        winner, player_one_score, player_two_score = handle_tiebreaker(
            deck, player_one_score, player_two_score)
        
    print(winner)
    return winner, player_one_score, player_two_score

def handle_tiebreaker(deck, player_one_score, player_two_score):
    """
    Handle a tiebreaker round when players draw cards of equal value.
    
    Args:
        deck (list): Current deck of cards
        player_one_score (int): Current score of player one
        player_two_score (int): Current score of player two
    Returns:
        tuple: (tiebreaker_result, updated_player_one_score, updated_player_two_score)
    """
    print("It's a tie! Drawing another card for the tiebreaker...")
    player_one_tiebreaker = draw_card(deck, "Player one")
    player_two_tiebreaker = draw_card(deck, "Player two")

    # Check if deck has enough cards for tiebreaker
    if player_one_tiebreaker is None or player_two_tiebreaker is None:
        return "Game over - deck empty", player_one_score, player_two_score

    # Compare tiebreaker cards and determine winner
    if player_one_tiebreaker["value"] > player_two_tiebreaker["value"]:
        winner = "Player one wins the tiebreaker!!!"
        player_one_score += 2
    elif player_two_tiebreaker["value"] > player_one_tiebreaker["value"]:
        winner = "Player Two wins the tiebreaker!!!"
        player_two_score += 2
    else:
        winner = "No One wins the tiebreaker! It's still a tie!"
    
    return winner, player_one_score, player_two_score

def display_final_result(player_one_score, player_two_score):
    """
    Display the final game result and declare the winner.
    
    Args:
        player_one_score (int): Final score of player one
        player_two_score (int): Final score of player two
    """
    if player_one_score > player_two_score:
        print("Player one is the overall winner with", player_one_score, "points!")
    elif player_two_score > player_one_score:
        print("Player two is the overall winner with", player_two_score, "points!")
    else:
        print("It's a tie! Both players have", player_one_score, "points!")

def play_war():
    """
    Main game function that controls the flow of the War card game.
    Handles game initialization, round execution, and game termination.
    """
    # Initialize game state
    deck = create_deck()
    deck = shuffle_deck(deck)
    player_one_score = 0
    player_two_score = 0

    # Main game loop - continue until deck is empty or player quits
    while True:
        # Execute one round of play
        result = handle_round(deck, player_one_score, player_two_score)
        
        if result is None:
            print("Game over, the deck is empty!")
            break
            
        # Update scores based on round result
        _, player_one_score, player_two_score = result

        # Show current game state
        print("Player one's score:", player_one_score)
        print("Player two's score:", player_two_score)

        # Check if player wants to continue playing
        user_input = input("Do you want to continue? (yes/no): ").strip().lower()
        if user_input not in ["yes", "y"]:
            print("Game stopped by the user.")
            break

    # Display final game results
    display_final_result(player_one_score, player_two_score)

# Only run the game if this file is run directly (not imported)
if __name__ == "__main__":
    play_war()
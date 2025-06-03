# GameCenter.py
from BlackJack import play_blackjack
from OldMaid import play_old_maid
from War import play_war

def display_menu():
    print("\nWelcome to the Game Center!")
    print("Please choose a game to play:")
    print("1. Blackjack")
    print("2. Old Maid")
    print("3. War")
    print("4. Exit")
    return input("Enter the number of your choice: ")

def run_game(choice):
    if choice == "1":
        print("\nStarting Blackjack...")
        play_blackjack()
    elif choice == "2":
        print("\nStarting Old Maid...")
        play_old_maid()
    elif choice == "3":
        print("\nStarting War...")
        play_war()
    elif choice == "4":
        print("Thank you for visiting the Game Center. Goodbye!")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True

def main():
    while True:
        choice = display_menu()
        if not run_game(choice):
            break

if __name__ == "__main__":
    main()
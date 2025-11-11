import random

def get_computer_choice():
    """Computer randomly picks rock, paper, or scissors"""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player, computer):
    """Compare choices and return the result"""
    if player == computer:
        return "tie"
    
    if (player == 'rock' and computer == 'scissors') or \
       (player == 'paper' and computer == 'rock') or \
       (player == 'scissors' and computer == 'paper'):
        return "player"
    else:
        return "computer"

def play_game():
    """Main game logic for one round"""
    print("\n--- Rock, Paper, Scissors ---")
    print("Choose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        player_choice = 'rock'
    elif choice == '2':
        player_choice = 'paper'
    elif choice == '3':
        player_choice = 'scissors'
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
        return play_game()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(player_choice, computer_choice)
    
    if result == "tie":
        print("It's a tie! 🤝")
    elif result == "player":
        print("You win! 🎉")
    else:
        print("Computer wins! 💻")

def main():
    """Main program - keeps the game running"""
    print("Welcome to Rock-Paper-Scissors!")
    
    play_again = 'yes'
    
    while play_again.lower() in ['yes', 'y']:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ")
    
    print("\nThanks for playing! Goodbye! 👋")

if __name__ == "__main__":
    main()

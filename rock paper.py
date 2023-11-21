import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"

    if (player_choice == 'rock' and computer_choice == 'scissors') or \
       (player_choice == 'paper' and computer_choice == 'rock') or \
       (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    
    print("Welcome to Rock, Paper, Scissors game!")
    
    while True:
        print("\nPlease choose: rock, paper, or scissors. To quit, type 'exit'.")
        player_choice = input("Your choice: ").lower()

        if player_choice == 'exit':
            print("Thanks for playing!")
            break
        
        if player_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

# Start the game
rock_paper_scissors()

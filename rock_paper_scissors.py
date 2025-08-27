"""
rock_paper_scissors.py
----------------------
A simple Rock-Paper-Scissors game against the computer.

Author: Brian Bett
Date: 2025-08-27
"""

import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        return "player"
    else:
        return "computer"

def main():
    print("🪨✂️📄 Rock-Paper-Scissors Game!")
    while True:
        player_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
        if player_choice == "quit":
            print("👋 Thanks for playing!")
            break
        if player_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice. Try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"💻 Computer chose: {computer_choice}")
        
        winner = get_winner(player_choice, computer_choice)
        if winner == "tie":
            print("🤝 It's a tie!")
        elif winner == "player":
            print("🎉 You win!")
        else:
            print("💻 Computer wins!")

if __name__ == "__main__":
    main()


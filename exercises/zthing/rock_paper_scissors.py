import random
import os

score_computer, score_player= 0, 0,
choices = ["rock", "paper", "scissors"]

while score_computer <= 2 and score_player <= 2:
    winner_round = "None"
    os.system("cls" if os.name == "nt" else "clear")
    if score_computer == 2 or score_player == 2:
        if score_computer == 2:
            print(" ____________\n|YOU LOST!!!|", end='\n\n')
        elif score_player == 2:
            print(" __________\n|YOU WON!!!|", end='\n\n')
        play_again = None
        while play_again != 'y' and play_again != 'n':
            play_again = input("Do you want to play again? (y/n):").lower()
        if play_again == 'y':
            score_computer, score_player = 0, 0
        else:
            break
    else:
        computer = random.choice(choices)
        player = input("Rock, Paper or Scissors?: ").lower()
        while player not in choices:
            player = input("Rock, Paper or Scissors?: ").lower()
        if computer == "rock":
            if player == "paper":
                score_player += 1
                winner_round = 'p'
            elif player == "scissors":
                score_computer += 1
                winner_round = 'c'
        elif computer == "paper":
            if player == "scissors":
                score_player += 1
                winner_round = 'p'
            elif player == "rock":
                score_computer += 1
                winner_round = 'c'     
        else: 
            if player == "rock":
                score_player += 1
                winner_round = 'p'
            elif player == "paper":
                score_computer += 1
                winner_round = 'c'
        print("\nComputer's choice: {}\nPlayer's choice: {}".format(computer, player))
        print("\nComputer: {}\nPlayer: {}\n".format(score_computer, score_player))
        if winner_round == 'p':
            print("\n _________________\n|YOU WON THE ROUND|")
        elif winner_round == 'c':
            print("\n __________________\n|YOU LOST THE ROUND|")
        else:
            print("\n ____\n|DRAW|")
        input("\nPress Enter to continue...", end='')
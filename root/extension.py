# Rock Paper Scissors

import random


def get_cpu_choice():
    return random.choice(["rock", "paper", "scissors"])


def get_player_choice():
    while True:
        user_input = input("Enter rock, paper, or scissors: ")
        user_input = user_input.lower()

        if user_input == "rock" or user_input == "paper" or user_input == "scissors":
            return user_input
        else:
            print("Invalid input")


def check_winner(cpu_choice, player_choice):
    if cpu_choice == player_choice:
        return "Tie"
    elif cpu_choice == "rock":
        if player_choice == "paper":
            return "Player"
        else:
            return "CPU"
    elif cpu_choice == "paper":
        if player_choice == "scissors":
            return "Player"
        else:
            return "CPU"
    else:
        if player_choice == "rock":
            return "Player"
        else:
            return "CPU"


def play_round():
    cpu_choice = get_cpu_choice()
    player_choice = get_player_choice()

    print("CPU Choice is", cpu_choice)

    winner = check_winner(cpu_choice, player_choice)
    return winner


player_wins = 0
cpu_wins = 0
ties = 0

while player_wins < 3 and cpu_wins < 3:
    round_winner = play_round()

    if round_winner == "Player":
        print("You won this round")
        player_wins += 1
    elif round_winner == "CPU":
        print("CPU won this round")
        cpu_wins += 1
    else:
        print("This round was a tie")
        ties += 1

    print("Current score is:")
    print("Player wins:", player_wins)
    print("CPU wins:", cpu_wins)
    print("Tie:", ties)

print("Game Over")
if player_wins == 3:
    print("Congratulations! Player won the tournament!")
else:
    print("The CPU won the tournament. Better luck next time!")
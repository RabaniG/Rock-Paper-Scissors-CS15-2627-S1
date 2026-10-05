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


def check_winner(cpu_choice,player_choice):
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


cpu_choice = get_cpu_choice()
player_choice = get_player_choice()

print("CPU Choice is", cpu_choice)

winner = check_winner(cpu_choice, player_choice)

print("The winner is", winner)
from random import choice
import sys

player_name = input("Enter your name: ")
print("Hello,", player_name)


def stepping(position, length):
    step = position + (length + 1) / 2
    if step >= length:
        step = step - length
        return int(step)
    else:
        return int(step)


def get_list(user_list, user_input):
    step_index = user_list.index(user_input)
    required_steps = stepping(step_index, len(user_list))
    rotated_list = user_list[required_steps:] + user_list[:required_steps]
    return rotated_list


def get_score(player):
    rating_file = open("rating.txt", "r")
    for line in rating_file:
        name, score = line.split()
        if name == player:
            return int(score)

    rating_file.close()
    return 0


def game(user_list, user_input, rating):
    computer = choice(user_list)
    user_list = get_list(user_list, user_input)
    if user_list.index(computer) > user_list.index(user_input):
        print(f"Sorry, but the computer chose {computer}")
        return rating
    elif user_list.index(computer) < user_list.index(user_input):
        print(f"Well done. The computer chose {computer} and failed.")
        rating += 100
        return rating
    else:
        print(f"There is a draw ({computer})")
        rating += 50
        return rating


player_score = get_score(player_name)
print("Player name is", player_name, "and his current score is", player_score)

choices = ["!exit", "!rating"]
play_list = ["rock", "paper", "scissors"]

human = input()

if human.find(",") != -1:
    play_list = human
    play_list = list(play_list.split(sep=","))
elif human == "!exit":
    print("Bye!")
    sys.exit()
elif human == "!rating":
    print("Your rating:", player_score)

print("Okay, let's start")
while True:
    while True:
        human = input()
        if human not in choices and human not in play_list:
            print("Invalid input")
        else:
            break
    if human == "!exit":
        print("Bye!")
        break
    if human == "!rating":
        print("Your rating:", player_score)
        continue

    player_score = game(play_list, human, player_score)

from random import choice

player_name = input("Enter your name: ")
print("Hello,", player_name)


def get_score(player):
    rating_file = open("rating.txt", "r")
    for line in rating_file:
        name, score = line.split()
        if name == player:
            return int(score)

    rating_file.close()
    return 0


def game(user_input, rating):
    computer = choice(["rock", "paper", "scissors"])
    lose = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    if user_input == computer:
        print(f"There is a draw ({computer})")
        rating += 50
        return rating
    elif user_input == lose[computer]:
        print(f"Sorry, but the computer chose {computer}")
        return rating
    elif user_input != computer:
        print(f"Well done. The computer chose {computer} and failed.")
        rating += 100
        return rating


player_score = get_score(player_name)
print("Player name is", player_name, "and his current score is", player_score)

choices = ["rock", "paper", "scissors", "!exit", "!rating"]

while True:
    while True:
        human = input()
        if human not in choices:
            print("Invalid input")
        else:
            break
    if human == "!exit":
        print("Bye!")
        break
    if human == "!rating":
        print("Your rating:", player_score)
        continue

    player_score = game(human, player_score)

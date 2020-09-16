from random import choice


def game(user_input):
    computer = choice(["rock", "paper", "scissors"])
    lose = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    if user_input == computer:
        print(f"There is a draw ({computer})")
    elif user_input == lose[computer]:
        print(f"Sorry, but the computer chose {computer}")
    elif user_input != computer:
        print(f"Well done. The computer chose {computer} and failed.")


choices = ["rock", "paper", "scissors", "!exit"]

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

    game(human)

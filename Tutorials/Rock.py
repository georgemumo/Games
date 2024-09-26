import random
import time
choices = ["rock", "paper", "scissors"]

while True:

    computer = random.choice(choices)
    # print(computer)
    player = None
    while player not in choices:
        player = input("Enter your choice to play : rock, paper, or scissors: ").lower()
    # player = input("Enter your choice:Rock, Paper, or Scissors\n ")
    if player == computer:
        print("Computer:",computer)
        print("Player:",player)
        time.sleep(2)
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Computer:", computer)
            print("Player:", player)
            time.sleep(2)
            print("Computer looses!")
            print("You won")
        if computer == "rock":
            print("Computer:", computer)
            print("Player:", player)
            time.sleep(2)
            print("It's a tie!")
        if computer == "paper":
            print("Computer:", computer)
            print("Player:", player)
            time.sleep(2)
            print("Computer wins!")
            print("You loose!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer:", computer)
            print("Player:", player)
            time.sleep(2)
            print("Computer wins!")
            print("You loose")
        if computer == "paper":
            print("Computer:", computer)
            print("Player:", player)
            time.sleep(2)
            print("It's a tie!")
        if computer == "rock":
            print("Computer:", computer)
            print("Player:", player)
            time.sleep(2)
            print("Computer looses!")
            print("You won!")
    elif player == "scissors":
        if computer == "Rock":
            print("Computer:", computer)
            print("Player:", player)
            time.sleep(2)
            print("Computer wins!")
            print("You loose")
        if computer == "scissors":
            print("Computer:", computer)
            print("Player:", player)
            time.sleep(2)
            print("It's a tie!")
        if computer == "paper":
            print("Computer:", computer)
            print("Player:", player)
            time.sleep(2)
            print("Computer looses!")
            print("You won!")
    play_again = input("Would you like to play again? (yes/no)").lower()
    if play_again != "yes":
        break
print("Thanks for playing!")
# print("You chose", player)
# print("Computer chose", computer) 
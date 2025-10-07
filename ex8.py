import random

print("Welcome to rock, paper and scissors!")
choices = ["rock", "paper", "scissors"]

while True:
    player = input("Enter your choice: ")
    player = player.lower()
    computer = random.choice(choices)
    print(f"Computer choice: {computer}")

    if player == computer:
        print("Draw")
    elif player == "rock":
        if computer == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif player == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
        else:
            print("You lose!")
    else:
        print("Invalid choice")

    playAgain = input("Do you want to play again?! Type 'yes' or 'no': ")
    if playAgain.lower() == "no":
        print("Thank you for playing!")
        break

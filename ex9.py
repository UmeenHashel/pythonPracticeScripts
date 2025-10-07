import random

print("Welcome to number guessing game!")
print("I'm thinking of a number between 1 and 9.")

while True:
    randomNum = random.randint(1, 9)
    count = 0

    while True:
        playerChoice = input("Player choose: ")

        if playerChoice.lower() == "exit":
            print("Thank you for playing!")
            exit()

        if not playerChoice.isdigit():
            print("Please enter a valid number!")
            continue

        playerChoice = int(playerChoice)
        count += 1

        if playerChoice == randomNum:
            print("That's right! You win!")
            print("The number was", randomNum)
            print("Total count of guesses: ", count)
        elif playerChoice > randomNum:
            print("Lower!")
        else:
            print("Higher!")




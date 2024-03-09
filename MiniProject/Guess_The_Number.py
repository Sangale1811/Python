import random

target = random.randint(1, 100)

while True:
    userChoice = int(input("Guess the target or Quit : "))

    if (userChoice == "Quit"):
        break

    if (userChoice == target):
        print("Success : Correct Guess!!!")
        break
    elif (userChoice < target):
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")


print("---------------GAME OVER----------------")

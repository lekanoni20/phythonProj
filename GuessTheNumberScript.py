import random

pick = int(input("Enter a number between 0 and 20"))

ComputerValue = random.randint(0, 20)

if ComputerValue == pick:
    print("You guessed right!!!!! Wow!!!")
else:
    print("Your guess is wrong. The correct number is " + str(ComputerValue) + ". Try again!!!")

import random

pick = int(input("Enter a number between 0 and 20"))

ComputerValue = random.randint(0, 20)

if ComputerValue == pick:
    print("You guessed right!!!!! Wow!!!")
elif ComputerValue > pick:
    print("Your number is too low. The correct number is " + str(ComputerValue) + ". Try again!!!")
elif pick > ComputerValue:
    print("Your number is too high. The correct number is " + str(ComputerValue) + ". Try again!!!")

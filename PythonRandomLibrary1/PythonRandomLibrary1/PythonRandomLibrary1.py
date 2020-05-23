#Import random Library 
import random
#User selects a number between 0 and 20
max_number= int (input("Choose a # between 0 and 20..."))
number = random.randint(0,max_number)
#If the number the user selects matches the random num generated the user is correct else user guesses again 
if max_number == number:
    print("Your guess was correct!")
else:
    print("Oh unlucky. Guess again :) the correct answer is")
    print(number)
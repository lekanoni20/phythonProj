#Import random Library 
import random
#User selects a number between 0 and 20
max_number = int (input("Choose a # between 0 and 20..."))
number = random.randint(0,20)
#If the number the user selects matches the random num generated the user is correct else user guesses again 
if max_number == number:
    print("Your guess was correct!")
elif max_number < number:
    print("Your guess is too low")
elif max_number > number:
    print("Your guess is too high")
#else:
    #print("Oh unlucky. Guess again :) the correct answer is")
    #print(number)

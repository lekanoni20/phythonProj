import random

while True:


    print("Pick your choice: ")

    choice = input()
    choice = choice.lower()

    print("My choice is", choice)

    choices = ["rock","paper","scissors"]

    computer_choice = choices[random.randint(0,2)]

    print("Computer choice is", computer_choice)

    if choices in choices:
        if choice == "rock":
            if computer_choice == "rock":
                print("Its a tie!")

            elif computer_choice == "scissors":
                print("You win! Computer chose Scissors")

            elif computer_choice == "paper":
                print("You lose! Computer chose paper")




        if choice == "paper":
            if computer_choice == "paper":
                print("It is a Tie!")

            elif computer_choice == "scissors":
                print("You lose!")

            elif computer_choice == "rock":
                print("Congratulations you win!")


        if choice == "scissors":
            if computer_choice == "scissors":
                print("It is a Tie!")

            elif computer_choice == "rock":
                print("You lose!")

            elif computer_choice == "paper":
                print("Congratulations You win!")

    else:
        print("Your choice is invalid. Please try again")
    
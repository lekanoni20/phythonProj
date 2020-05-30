import random


comp_wins = 0
user_wins = 0


while True:

    print("Pick your choice: ")

    choice = input()
    choice = choice.lower()

    print("My choice is", choice)

    choices = ["rock", "paper", "scissors"]

    computer_choice = choices[random.randint(0, 2)]

    print("Computer choice is", computer_choice)

    if choice in choices:
        if choice == "rock":
            if computer_choice == "rock":
                print("Its a tie!")
                comp_wins = comp_wins + 1
                user_wins = user_wins + 1
                print("You have won " + str(user_wins) + " amount of times")
                print("The computer has won " + str(comp_wins) + " amount of times")


            elif computer_choice == "scissors":
                print("You win! Computer chose Scissors")
                user_wins = user_wins + 1
                print("You have won " + str(user_wins) + " amount of times")
                print("The computer has won " + str(comp_wins) + " amount of times")

            elif computer_choice == "paper":
                print("You lose! Computer chose paper")
                comp_wins = comp_wins + 1
                print("You have won " + str(user_wins) + " amount of times")
                print("The computer has won " + str(comp_wins) + " amount of times")

        if choice == "paper":
            if computer_choice == "paper":
                print("It is a Tie!")
                comp_wins = comp_wins + 1
                user_wins = user_wins + 1
                print("You have won " + str(user_wins) + " amount of times")
                print("The computer has won " + str(comp_wins) + " amount of times")

            elif computer_choice == "scissors":
                print("You lose!")
                comp_wins = comp_wins + 1
                print("You have won " + str(user_wins) + " amount of times")
                print("The computer has won " + str(comp_wins) + " amount of times")

            elif computer_choice == "rock":
                print("Congratulations you win!")
                user_wins = user_wins + 1
                print("You have won " + str(user_wins) + " amount of times")
                print("The computer has won " + str(comp_wins) + " amount of times")

        if choice == "scissors":
            if computer_choice == "scissors":
                print("It is a Tie!")
                comp_wins = comp_wins + 1
                user_wins = user_wins + 1
                print("You have won " + str(user_wins) + " amount of times")
                print("The computer has won " + str(comp_wins) + " amount of times")

            elif computer_choice == "rock":
                print("You lose!")
                comp_wins = comp_wins + 1
                print("You have won " + str(user_wins) + " amount of times")
                print("The computer has won " + str(comp_wins) + " amount of times")

            elif computer_choice == "paper":
                print("Congratulations You win!")
                user_wins = user_wins + 1
                print("You have won " + str(user_wins) + " amount of times")
                print("The computer has won " + str(comp_wins) + " amount of times")

    else:
        print("Your choice is invalid. Please try again")

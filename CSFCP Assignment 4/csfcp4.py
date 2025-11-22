# NUMBER GUESSING GAME
# BY --> DAKSH 

import random

# DEFINING THE FUNCTION FOR THE GAME
def number_guessing_game():
    print("\n-------- NUMBER GUESSING GAME --------\n")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # RANDOMIZING THE NUMBER TO BE GUESSED
    number_to_guess = random.randint(1, 100)
    attempts = 0

    # USING LOOP TO GIVE MULTIPLE ATTEMPTS TO THE USER
    while True:
        user_input = input("Enter your guess: ")

        # CHECK IF THE INPUT IS VALID 
        if user_input.isdigit():
            user_guess = int(user_input)
            attempts += 1

            # ADDING HINTS TO THE GAME TO MAKE IT FEEL INTERACTIVE
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(
                    f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
                break  # IF THE GUESS IS RIGHT, THE LOOP BREAKS
        else:
            print("Please enter a valid number.")  # FOR INVALID INPUTS 


# RUNNING THE GAME
number_guessing_game()

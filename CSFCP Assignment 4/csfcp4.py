# NUMBER GUESSING GAME
# BY --> DAKSH

import random


def number_guessing_game():
    print("\n\n--------- NUMBER GUESSING GAME ---------\n\n")
    print("Welcome to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100.")

    # RANDOMIZING THE NUMBER TO BE GUESSED
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    # INITIALIZE TO AVOID REFERENCE ERRORS
    user_guess = None

    try:
        while attempts < max_attempts:

            try:
                user_input = input("Enter your guess: ")
                print("\n")

                # CHECK IF THE INPUT IS VALID
                if user_input.isdigit():
                    user_guess = int(user_input)
                    attempts += 1

                    # ADDING HINTS
                    if user_guess < number_to_guess:
                        print("Too low! Try again.\n")
                    elif user_guess > number_to_guess:
                        print("Too high! Try again.\n")
                    else:
                        print(
                            f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts."
                        )
                        break  # CORRECT GUESS EXITS LOOP
                else:
                    print("Please enter a valid number.\n")

            except ValueError:
                print("Invalid input! Please enter a number.\n")

    except KeyboardInterrupt:
        print("\n\nGame interrupted by user. Exiting...\n")
        return

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}\n")
        return

    # OUT OF ATTEMPTS
    if attempts == max_attempts and user_guess != number_to_guess:
        print(
            f"Sorry, you've used all {max_attempts} attempts. The correct number was {number_to_guess}."
        )


# RUNNING THE GAME
number_guessing_game()

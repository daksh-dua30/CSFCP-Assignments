import random


def number_guessing_game():
    print("\n-------- NUMBER GUESSING GAME --------\n")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    correct_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_input = input("Enter your guess: ")

        # Check if the input is a valid number
        if user_input.isdigit():
            user_guess = int(user_input)
            attempts += 1

            if user_guess < correct_number:
                print("Too low! Try again.")
            elif user_guess > correct_number:
                print("Too high! Try again.")
            else:
                print(
                    f"Congratulations! You've guessed the correct number {correct_number} in {attempts} attempts.")
                break  # Exit the loop if the guess is correct
        else:
            print("Please enter a valid number.")


# Run the game
number_guessing_game()

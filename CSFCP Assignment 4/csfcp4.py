import random


def number_guessing_game():
    print("\n-------- NUMBER GUESSING GAME --------\n")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        user_input = input("Enter your guess: ")

        # Check if the input is a valid number
        if user_input.isdigit():
            user_guess = int(user_input)
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(
                    f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
                break  # Exit the loop if the guess is correct
        else:
            print("Please enter a valid number.")


# Run the game
number_guessing_game()

import random
import time

def single_player_mode():
    print("Welcome to Single-Player Mode!")
    random_number = random.randint(1, 100)
    guesses = 0
    start_time = time.time()

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            guesses += 1

            if guess < random_number:
                print("Higher!")
            elif guess > random_number:
                print("Lower!")
            else:
                end_time = time.time()
                print(f"Congratulations! You guessed it in {guesses} guesses and {end_time - start_time:.2f} seconds.")
                break
        except ValueError:
            print("Please enter a valid number.")

def multiplayer_mode():
    print("Welcome to Multiplayer Mode!")
    random_number = random.randint(1, 100)
    player_turn = 1
    player_scores = {1: 0, 2: 0}

    while True:
        try:
            print(f"Player {player_turn}'s turn!")
            guess = int(input("Guess a number between 1 and 100: "))
            player_scores[player_turn] += 1

            if guess < random_number:
                print("Higher!")
            elif guess > random_number:
                print("Lower!")
            else:
                print(f"Player {player_turn} wins! The number was {random_number}.")
                print(f"Player 1 score: {player_scores[1]} guesses")
                print(f"Player 2 score: {player_scores[2]} guesses")
                break

            player_turn = 2 if player_turn == 1 else 1
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Welcome to the Number Guessing Game by Murali N P!")
    print("Choose a mode:")
    print("1. Single-Player Mode")
    print("2. Multiplayer Mode")
    print("3. Exit")

    while True:
        try:
            choice = int(input("Enter 1, 2, or 3: "))

            if choice == 1:
                single_player_mode()
            elif choice == 2:
                multiplayer_mode()
            elif choice == 3:
                print("Thank you for playing! Goodbye!")
                break
            else:
                print("Please choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid choice.")

if __name__ == "__main__":
    main()

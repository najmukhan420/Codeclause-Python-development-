import random

def number_guessing_game():
    print("Welcome in the Game!")
    print("I have picked a number which is inbetween 1 and 100. Try to guess the value!")

    # Generating a random number
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

       # Check if the guess is right
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Very low value! Please try again.")
        else:
            print("Very high value! Please try again.")

if __name__ == "__main__":
    number_guessing_game()

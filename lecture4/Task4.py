import random

# Computer picks a random number between 1 and 10
secret_number = random.randint(1, 10)

print("🎲 Guess the number (between 1 and 10)")

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():  # check if input is a number
        print("Please enter a valid number!")
        continue

    guess = int(guess)

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! The secret number was", secret_number)
        break

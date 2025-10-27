import random  # import the random module


# Function that returns a random dice roll between 1 and 6
def roll_dice():
    return random.randint(1, 6)
# Main program that rolls until the result is 6
def main():
    result = 0
    while result != 6:
        result = roll_dice()
        print("You rolled:", result)

    print("You got a 6! Game over.")


# Run the main program
if __name__ == "__main__":
    main()
    input("Press Enter to exit...")

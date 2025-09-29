import random

# Ask the user how many dice to roll
num_dice = int(input("How many dice do you want to roll? "))

# Variable to store the total sum
total = 0

# Roll each die using a for loop
for i in range(num_dice):
    roll = random.randint(1, 6)  # Random number between 1 and 6
    print(f"Dice {i+1}: {roll}")
    total += roll

# Print the total sum
print(f"The sum of all dice is: {total}")

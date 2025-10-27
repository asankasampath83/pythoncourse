def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def main():
    # Create a list of integers
    numbers = [5, 10, 15, 20, 25]

    # Call the function
    result = sum_list(numbers)

    # Print the result
    print("The sum of the numbers is:", result)


# Run the main program
if __name__ == "__main__":
    main()

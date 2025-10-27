# Function that returns a new list with all odd numbers removed
def remove_odd_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:  # Check if the number is even
            even_numbers.append(num)
    return even_numbers



def main():
    # Create a list of integers
    numbers = [3, 8, 11, 14, 17, 20, 25, 30]

    # Call the function
    even_list = remove_odd_numbers(numbers)

    # Print both lists
    print("Original list:", numbers)
    print("Even numbers only:", even_list)


if __name__ == "__main__":
    main()



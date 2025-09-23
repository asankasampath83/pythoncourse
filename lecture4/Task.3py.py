numbers = []

while True:

    user_input = input("Enter a number (leave blank to stop): ")

    if user_input == "":  #
        break

    try:
        num = float(user_input)
        numbers.append(num)
    except error:
        print("Invalid input. Please enter a valid number.")

if numbers:
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
else:
    print("No numbers were entered.")





while True:
    inches = float(input("Enter no of inches (negative to stop): "))


    if inches < 0:
        print("Program stop.")
        break

    centimeters = inches * 2.54
    print(f"{inches} inches = {centimeters:.2f} cm")


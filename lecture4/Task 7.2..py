# Function that converts gallons to liters
def gallons_to_liters(gallons):
    return gallons * 3.78541  # 1 US gallon = 3.78541 liters


def main():
    while True:
        gallons = float(input("Enter volume in gallons (negative number to stop): "))

        if gallons < 0:
            print("Program ended.")
            break

        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons = {liters:.2f} liters\n")


if __name__ == "__main__":
    main()


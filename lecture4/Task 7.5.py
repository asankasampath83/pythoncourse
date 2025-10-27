import math


# Function to calculate the unit price per square meter
def unit_price(diameter_cm, price_eur):
    # Calculate pizza area (πr²)
    radius_m = (diameter_cm / 2) / 100  # convert cm to meters
    area_m2 = math.pi * radius_m ** 2
    # Calculate unit price (euros per square meter)
    return price_eur / area_m2


# Main program
def main():
    print("Enter details for the first pizza:")
    diameter1 = float(input("Diameter (cm): "))
    price1 = float(input("Price (€): "))

    print("\nEnter details for the second pizza:")
    diameter2 = float(input("Diameter (cm): "))
    price2 = float(input("Price (€): "))

    # Calculate unit prices
    unit1 = unit_price(diameter1, price1)
    unit2 = unit_price(diameter2, price2)

    # Print results
    print(f"\nFirst pizza unit price:  {unit1:.2f} €/m²")
    print(f"Second pizza unit price: {unit2:.2f} €/m²")

    # Compare values
    if unit1 < unit2:
        print("👉 The first pizza gives better value for money.")
    elif unit2 < unit1:
        print("👉 The second pizza gives better value for money.")
    else:
        print("🍕 Both pizzas have the same value for money.")


# Run the main program
if __name__ == "__main__":
    main()

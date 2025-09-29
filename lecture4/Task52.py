numbers = []

while True:
    n = input("Enter a number (leave blank to quit): ")
    if n == "":
        break
    try:
        numbers.append(float(n))
    except:
        print("Not a valid number, try again.")

numbers.sort(reverse=True)
print("The five greatest numbers are:", numbers[:5])




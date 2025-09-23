# Hemoglobin level test
from xml.sax import make_parser

#helooo

gender = input("Enter biological gender (male/female): ").lower()
hemoglobin = float(input("Enter hemoglobin level (g/L): "))

if gender == "female":
    if hemoglobin < 117:
        print("hemoglobin level is low.")
    elif hemoglobin <= 155:
        print("hemoglobin level is normal.")
    else:
        print("hemoglobin level is high.")
if gender == "male":
    if hemoglobin < 134:
        print("hemoglobin level is low.")
    elif hemoglobin <= 167:
        print("hemoglobin level is normal.")
    else:
        print("hemoglobin level is high.")
else:
    print("Invalid gender input.")

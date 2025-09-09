# Program to check if the ticket is Business Class

# Ask the user for ticket type
ticket_type = input("Enter your ticket type (Economy / Business / First): ")

# Check and decide
if ticket_type.lower() == "business":
    print("✅ Accepted: You are in Business Class.")
else:
    print("❌ Rejected: Not a Business Class ticket.")






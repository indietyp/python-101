"""
Take the total bill amount and the tip percentage from the user and print the tip amount.

Hint: You can use the input() function to take input from the user,
        and the float() function to convert a string to a float.

Hint: The formula for calculating the tip amount is:
        tip = bill * tip_percentage / 100

Example:
    Enter the bill amount: 100
    Enter the tip percentage: 15
    "The tip amount is $15.0"
    "The total amount is $115.0"
"""

bill = input("Enter the bill amount: ")
bill = float(bill)

tip_percentage = input("Enter the tip percentage: ")
tip_percentage = float(tip_percentage)

tip = bill * tip_percentage / 100

print(f"The tip amount is ${tip}")
print(f"The total amount is ${bill + tip}")

"""
Take a number from the user and print the factorial of the number.

Example:
    Enter a number: 5
    The factorial of 5 is 120.
"""

# Write your code below this line 👇

number = input("Enter a number: ")
number = int(number)

factorial = 1

for i in range(1, number + 1):
    factorial *= i

factorial = number

for i in range(number - 1, 0, -1):
    factorial *= i

print(f"The factorial of {number} is {factorial}.")

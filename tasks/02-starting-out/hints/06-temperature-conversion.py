"""
Take the temperature in Celsius from the user and print it in Fahrenheit.

Hint: You can use the input() function to take input from the user,
      and the float() function to convert a string to a float.

Hint: The formula for converting Celsius to Fahrenheit is:
      F = C * 9 / 5 + 32

Example:
    Enter the temperature in Celsius: 37
    98.6
"""

celsius = input("Enter the temperature in Celsius: ")
celsius = float(celsius)

fahrenheit = celsius * 9 / 5 + 32

print(fahrenheit)

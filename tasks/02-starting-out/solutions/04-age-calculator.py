"""
Take the birth year of a person from the user and print their age.

Hint: You can use the input() function to take input from the user,
        and the int() function to convert the input to an integer.

Example:
    Enter your birth year: 1990
    30
"""

import datetime

this_year = datetime.datetime.now().year

birth_year = input("Enter your birth year: ")
birth_year = int(birth_year)

age = this_year - birth_year

print(age)

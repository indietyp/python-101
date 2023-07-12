"""
Take a year from the user and print whether it is a leap year or not.

Hint: You can use the input() function to take input from the user.
      The algorithm for checking if a year is a leap year can be found here:
        https://stackoverflow.com/a/725111/9077988

Example:
    Enter a year: 2020
    2020 is a leap year.
"""

# Write your code below this line 👇

year = input('Enter a year: ')
year = int(year)

is_regular_leap_year = ____________ and ____________
is_exceptional_leap_year = ____________

if is_regular_leap_year or is_exceptional_leap_year:
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')

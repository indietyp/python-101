"""
The variable `password` contains a string, write a program that asks the user for a
password and prints "Access granted" if the password is correct, and "Access denied" if
the password is incorrect.

Hint: You can use the input() function to take input from the user.

Example:
    Enter password: 1234
    Access denied
"""

# Uncomment the two lines below to enable random numbers.
# import utils
# utils.enable_random()

# When executing the tests, the variable `password` will be replaced with a random string.
# When executing your own code this will always be the string "1234".
from utils import password

# Write your code below this line 👇

value = input('Enter password: ')

if _________:
    print('Access granted')
else:
    print('Access denied')

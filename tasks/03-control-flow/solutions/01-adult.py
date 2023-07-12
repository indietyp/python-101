"""
Ask about the age of the user and print if he is an adult or not.
(Assume that an adult is someone who is 18 years or older.)

Hint: You can use the input() function to take input from the user.

Example:
    How old are you? 17
    You are not an adult.
"""

# Write your code below this line 👇

value = input('How old are you? ')
value = int(value)

if value >= 18:
    print('You are an adult.')
else:
    print('You are not an adult.')

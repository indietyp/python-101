"""
You are given a random number between 1 and 100, write a program that asks the user to
guess the number.

The program should print "Too high" if the number is higher than the random number,
"Too low" if the number is lower than the random number,
and "You win" if the number is equal to the random number.

The program should keep asking the user to guess the number until the user guesses the
correct number and should then terminate.

Bonus: Print the number of guesses the user made.

Hint: You can use the input() function to take input from the user.

Example:
    Guess a number: 50
    Too high
    Guess a number: 25
    Too low
    Guess a number: 37
    Too high
    Guess a number: 31
    Too high
    Guess a number: 28
    You win
    You made 5 guesses
"""

# Uncomment the two lines below to enable random numbers.
# import utils
# utils.enable_random()

# When executing the tests, the variable `number` will be replaced with a random number.
# When executing your own code this will always be the number 28.
from utils import number

# Write your code below this line 👇

guesses = 0

while True:
    input_number = input("Guess a number: ")
    input_number = int(input_number)

    guesses += 1

    if input_number > number:
        print("Too high")
    elif input_number < number:
        print("Too low")
    else:
        print("You win")
        print(f"You made {guesses} guesses")

        break

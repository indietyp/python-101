"""
Write a primitive calculator that can add, subtract, multiply and divide two numbers.

The program should ask the user for two numbers and an operator,
and then print the result. This is an extension of 03-primitive-calculator.py
from tasks/02-starting-out.

Optional Tasks:
    - Ask for the operator until the user enters a valid operator.
    - When the user enters an invalid operator, print a message with the valid operators.
    - Add support for the modulo operator (%).
    - Add support for the power operator (**).
    - Add support for the floor division operator (//).
    - Support floating point numbers.

Example:
    Enter a number: 5
    Enter another number: 3
    Enter an operator: +

    8
"""

# Write your code below this line 👇

lhs = input('Enter a number: ')
lhs = ___(lhs)

rhs = input('Enter another number: ')
rhs = ___(rhs)

while True:
    operator = input('Enter an operator: ')

    match operator:
        case '+':
            print(___________)
            break
        case '-':
            print(___________)
            break
        case '*':
            print(___________)
            break
        case '/':
            print(___________)
            break
        case _:
            ____________

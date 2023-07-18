"""
Write a number that takes a number from the user and prints the first n numbers in the
Fibonacci sequence.

First two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the
sum of the previous two.

Hint: You can use `print(a, end=' ')` to print something without a newline.

Example:
    Enter a number: 10
    0 1 1 2 3 5 8 13 21 34
"""

# Write your code below this line 👇

n = input("Enter a number: ")
n = int(n)

a = 0
b = 1

for i in range(0, n):
    print(a, end=" ")

    a_old = a
    b_old = b

    a = b_old
    b = a_old + b_old

    c = a
    a = b
    b = c + b

    # a = 1
    # b = 1

    # a = 1
    # b = 2

print()

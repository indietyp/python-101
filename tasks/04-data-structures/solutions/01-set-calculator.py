"""
Write a program that reads two sets of numbers and prints the result of the following
operations on them:
* "union" - the union of the two sets
* "intersection" - the intersection of the two sets
* "difference" - the difference of the two sets
* "symmetric difference" - the symmetric difference of the two sets

The numbers should be inputted one by one. To stop inputting numbers, the user should
write `done`.

Extra:
    - Parse the input as a single string, which is comma separated, and then split it.
    - Allow the user to also use
        `|` for union,
        `&` for intersection,
        `-` for difference and
        `^` for symmetric difference.

Example:
    First set: 1
    First set: 2
    First set: 3
    First set: 4
    First set: done
    Second set: 3
    Second set: 4
    Second set: 5
    Second set: 6
    Second set: done
    Operation: union
    Output: {1, 2, 3, 4, 5, 6}
"""

# Write your code below this line 👇

a = set()
b = set()
while True:
    value = input("First set: ")
    if value == "done":
        break

    value = int(value)
    a.add(value)

while True:
    value = input("Second set: ")
    if value == "done":
        break

    value = int(value)
    b.add(value)

operation = input("Operation: ")
if operation == "union":
    print(a | b)
elif operation == "intersection":
    print(a & b)
elif operation == "difference":
    print(a - b)
elif operation == "symmetric difference":
    print(a ^ b)
else:
    print("Unknown operation")

# With extras
a = input("First set: ")
a = a.split(",")
a = {int(number.strip()) for number in a}

b = input("Second set: ")
b = b.split(",")
b = {int(number.strip()) for number in b}

operation = input("Operation: ")
if operation == "union" or operation == "|":
    print(a | b)
elif operation == "intersection" or operation == "&":
    print(a & b)
elif operation == "difference" or operation == "-":
    print(a - b)
elif operation == "symmetric difference" or operation == "^":
    print(a ^ b)
else:
    print("Unknown operation")

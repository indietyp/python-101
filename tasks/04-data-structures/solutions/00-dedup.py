"""
Create a program that takes a list of numbers from the user and prints
out the list without duplicates. The list **must** preserve the order.

To input a list of numbers, you should ask the user to input a number until the write
`done`.

Extra:
    - Use a set to solve the problem.
    - Parse the input as a single string, which is comma separated, and then split it.

Example:
    Input: 1
    Input: 2
    Input: 3
    Input: 1
    Input: 2
    Input: done

    Output: [1, 2, 3]
"""

# Write your code below this line 👇

# List solution
numbers = []
while True:
    value = input("Input: ")
    if value == "done":
        break

    value = int(value)
    if value not in numbers:
        numbers.append(value)

print(f"Output: {numbers}")

# Set solution
numbers = set()
while True:
    value = input("Input: ")
    if value == "done":
        break

    value = int(value)
    numbers.add(value)

print(f"Output: {list(numbers)}")

# String solution
numbers = input("Input: ")
numbers = numbers.split(",")
numbers = {int(number.strip()) for number in numbers}
print(f"Output: {list(numbers)}")

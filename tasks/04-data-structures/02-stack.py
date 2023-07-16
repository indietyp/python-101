"""
Implement a stack, where the user can push and pop elements from the stack,
as well as print the stack.
(A stack is a data structure, where the last element that was pushed is the first
one to be popped. It is called LIFO - last in, first out.)

The user should input the commands one by one. To stop inputting commands,
the user should write `done`. The commands are:
- `push` - pushes the value to the stack
- `pop` - pops the value from the stack
- `print` - prints the stack

Extra:
    - Allow for the `push` command to be written as `push <value>`.
    - Allow multiple values to be pushed at once, e.g. `push 1 2 3`.
    - Allow for the `pop` command to be written as `pop <number>`,
        where the number is the number of elements to pop.

Example:
    Input: push
    Value: 1
    Input: push
    Value: 2
    Input: push
    Value: 3
    Input: print
    Output: [1, 2, 3]
    Input: pop
    Input: print
    Output: [1, 2]
"""

# Write your code below this line 👇

stack = []
while True:
    command = input("Input: ")
    if command == "done":
        break
    elif command == "push":
        value = input("Value: ")
        value = int(value)
        stack.append(value)
    elif command == "pop":
        stack.pop()
    elif command == "print":
        print(stack)
    else:
        print("Unknown command")

# With extras

stack = []
while True:
    command = input("Input: ")
    args = command.split()

    match args:
        case ["done"]:
            break
        case ["push", *values]:
            stack.extend(int(value) for value in values)
        case ["pop"]:
            stack.pop()
        case ["pop", number]:
            number = int(number)
            for _ in range(number):
                stack.pop()
        case ["print"]:
            print(stack)
        case _:
            print("Unknown command")

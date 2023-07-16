"""
Implement a queue, where the user can enqueue and dequeue elements from the queue,
as well as print the queue.
(A queue is a data structure, where the first element that was enqueued is the
first element to be dequeued. It is called FIFO - first in, first out.)

The user should input the commands one by one. To stop inputting commands,
the user should write `done`. The commands are:
- `enqueue` - enqueues the value to the queue
- `dequeue` - dequeues the value from the queue
- `print` - prints the queue

Extra:
    - Allow for the `enqueue` command to be written as `enqueue <value>`.
    - Allow multiple values to be enqueued at once, e.g. `enqueue 1 2 3`.
    - Allow for the `dequeue` command to be written as `dequeue <number>`,
        where the number is the number of elements to dequeue.

Example:
    Input: enqueue
    Value: 1
    Input: enqueue
    Value: 2
    Input: enqueue
    Value: 3
    Input: print
    Output: [1, 2, 3]
    Input: dequeue
    Input: print
    Output: [2, 3]
"""

# Write your code below this line 👇

queue = []
while True:
    command = input("Input: ")
    if command == "done":
        break
    elif command == "enqueue":
        value = input("Value: ")
        value = int(value)
        queue.append(value)
    elif command == "dequeue":
        queue.pop(0)
    elif command == "print":
        print(queue)
    else:
        print("Unknown command")

# With extras

queue = []
while True:
    command = input("Input: ")
    args = command.split()

    match args:
        case ["done"]:
            break
        case ["enqueue", *values]:
            queue.extend(int(value) for value in values)
        case ["dequeue"]:
            queue.pop(0)
        case ["dequeue", number]:
            number = int(number)
            for _ in range(number):
                queue.pop(0)
        case ["print"]:
            print(queue)
        case _:
            print("Unknown command")

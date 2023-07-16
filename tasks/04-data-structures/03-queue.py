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

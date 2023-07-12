# Loops

Loops are used to execute a block of code multiple times. In Python there are two types of loops: `for` loops
and `while` loops.

## `for` Loops

`for` loops are used to iterate over a sequence of values. The sequence can be a list, tuple, string, or any other type
of sequence. The `for` loop will iterate over each value in the sequence and execute the code block following the `for`
loop once for each value in the sequence, the value will be assigned to a variable in the code block to the name chosen
in the `for` loop.

```python
for i in [1, 2, 3]:
    print(i)

# > 1
# > 2
# > 3

for i in (1, 2, 3):
    print(i)

# > 1
# > 2
# > 3

for i in "abc":
    print(i)

# > a
# > b
# > c
```

The `for` loop can be followed by an `else` statement. The `else` statement is followed by a code block that will be
executed once the `for` loop has finished iterating over the sequence, and no `break` statement was executed. This is
very seldom used.

```python
for i in [1, 2, 3]:
    print(i)
else:
    print("The for loop has finished iterating")

# > 1
# > 2
# > 3
# > The for loop has finished iterating

for i in [1, 2, 3]:
    print(i)
    break
else:
    print("The for loop has finished iterating")

# > 1
```

## `while` Loops

`while` loops are used to execute a block of code while a condition is `True`. The condition is evaluated before each
execution of the code block. If the condition evaluates to `True` then the code block is executed. If the condition
evaluates to `False` then the code block is skipped.

```python
i = 0
while i < 3:
    print(i)
    i += 1

# > 0
# > 1
# > 2
```

The `while` loop can be followed by an `else` statement. The `else` statement is followed by a code block that will be
executed once the `while` loop has finished iterating, and no `break` statement was executed. This is very seldom used.

```python
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("The while loop has finished iterating")

# > 0
# > 1
# > 2
# > The while loop has finished iterating

i = 0
while i < 3:
    print(i)
    i += 1
    break
else:
    print("The while loop has finished iterating")

# > 0
```

The rule of thumb is: try to use `for` loops when you know how many times you want to iterate, and use `while` loops
when you don't. (meaning prefer `for` loops over `while` loops)

## `break` and `continue`

`break` and `continue` are used to control the flow of a loop. `break` is used to exit the loop immediately, and the
code block following the loop will be executed. `continue` is used to skip the rest of the code block and continue with
the next iteration of the loop.

```python
for i in [1, 2, 3]:
    print(i)
    break

# > 1

for i in [1, 2, 3]:
    print(i)
    continue
    print("This code block will not be executed")

# > 1
# > 2
# > 3
```

## `pass`

`pass` is used as a placeholder for code that has not been written yet. It is used to prevent a syntax error when a code
block is required but you don't want to write any code in the code block yet.

```python
if True:
    pass
else:
    print("This code block will not be executed")

for i in [1, 2, 3]:
    pass
```

In more modern versions of Python, `...` can be used instead of `pass`.

```python
if True:
    ...
else:
    print("This code block will not be executed")

for i in [1, 2, 3]:
    ...
```

## `range()`

The `range()` function is used to generate a sequence of numbers. It can be used to generate a sequence of numbers from
a specified start value to a specified end value. The end value is not included in the sequence. The `range` function is
predominately used in `for` loops to iterate over a sequence of numbers, or to iterate a specified number of times.

The `range` function can be called with one, two, or three arguments. If called with one argument, the argument is the
end value of the sequence, the start value is assumed to be `0`, and the step value is assumed to be `1`. If called with
two arguments, the first argument is the start value of the sequence, the second argument is the end value of the
sequence, and the step value is assumed to be `1`. If called with three arguments, the first argument is the start value
of the sequence, the second argument is the end value of the sequence, and the third argument is the step value of the
sequence.

```python
for i in range(1, 4):
    print(i)

# > 1
# > 2
# > 3

for i in range(3):
    print(i)

# > 0
# > 1
# > 2

for i in range(1, 4, 2):
    print(i)

# > 1
# > 3

for i in range(4, 1, -1):
    print(i)

# > 4
# > 3
# > 2
```

[//]: # (TODO: enumerate, zip, sorted and reversed when we go over lists)

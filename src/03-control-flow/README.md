# Control Flow

The goal of this section is to introduce the control flow statements in Python. We will cover the following topics:

* [Conditionals](./00-conditionals.md)
* [Loops](./01-loops.md)
    * [`for` Loops](./01-loops.md#for-loops)
    * [`while` Loops](./01-loops.md#while-loops)
    * [`break` and `continue`](./01-loops.md#break-and-continue)
    * [`pass` Statements](./01-loops.md#pass-statements)
    * [`range()` Function](./01-loops.md#range-function)
* [`match` Statements](./02-match-statements.md)

[//]: # (Exceptions for the future, for now they are too complicated)

## Conditionals

Conditionals are used to control the flow of a program. They allow us to execute certain blocks of code only if certain
conditions are met. In Python a conditional is created using the `if` statement. The `if` statement is followed by an
expression which is evaluated to a boolean value. If the expression evaluates to `True` then the code block following
the `if` statement is executed. If the expression evaluates to `False` then the code block is skipped.

It is important to note that the code block following the `if` statement is indented. This is how Python knows which
block of code is associated with the `if` statement. The code block is indented by 4 spaces by convention and ends when
the indentation returns to the previous level.

```python
if True:
    print("This code block will be executed")
    print("This code block will also be executed")
print("This code block will be executed as well")

if False:
    print("This code block will not be executed")

print("This code block will be executed as well")

if 1 == 1:
    print("This code block will be executed")

if 1 == 2:
    print("This code block will not be executed")
```

The `if` statement can be followed by an `else` statement. The `else` statement is followed by a code block that will be
executed if the expression in the `if` statement evaluates to `False`.

```python
if True:
    print("This code block will be executed")
else:
    print("This code block will not be executed")

if False:
    print("This code block will not be executed")
else:
    print("This code block will be executed")
```

The `if` statement can also be followed by an `elif` statement. The `elif` statement is followed by an expression that
will be evaluated if the expression in the `if` statement evaluates to `False`. If the expression in the `elif`
statement evaluates to `True` then the code block following the `elif` statement will be executed. If the expression in
the `elif` statement evaluates to `False` then the code block following the `elif` statement will be skipped.

```python
if False:
    print("This code block will not be executed")
elif True:
    print("This code block will be executed")
else:
    print("This code block will not be executed")

if False:
    print("This code block will not be executed")
elif False:
    print("This code block will not be executed")
else:
    print("This code block will be executed")
```

The `if` statement can be followed by any number of `elif` statements, but an `else` statement cannot
be followed by an `elif` statement. The `else` statement must be the last statement in the conditional.

```python
if False:
    print("This code block will not be executed")
elif False:
    print("This code block will not be executed")
elif False:
    print("This code block will not be executed")
else:
    print("This code block will be executed")
```

## Loops

Loops are used to execute a block of code multiple times. In Python there are two types of loops: `for` loops
and `while` loops.

### `for` Loops

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

### `while` Loops

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

### `break` and `continue`

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

### `pass`

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

### `range()`

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

## `match` Statements

`match` statements are a relatively new feature in Python. They are used to compare a value to a number of patterns and
execute code based on which pattern matches the value. `match` statements are similar to `switch` statements in other
languages.

```python
match value:
    case pattern1:
        # code to execute if value matches pattern1
        ...
    case pattern2:
        # code to execute if value matches pattern2
        ...
    case pattern3:
        # code to execute if value matches pattern3
        ...
    case _:
        # code to execute if value does not match any of the patterns
        ...
```

There are multiple types of patterns that can be used in a `match` statement. The most common patterns are literal value
patterns, type patterns, and variable patterns.

Literal value patterns are used to match a specific value. The value can be a literal value, a variable, or an
expression that evaluates to a value.

```python
a = 1

match a:
    case 1:
        print("a is 1")
    case 2:
        print("a is 2")
    case 3:
        print("a is 3")
    case _:
        print("a is not 1, 2, or 3")

# > a is 1
```

Type patterns are used to match a specific type. The type can be a built-in type, a user-defined type, or a variable or
expression that evaluates to a type.

```python
a = 1

match a:
    case int():
        print("a is an int")
    case float():
        print("a is a float")
    case str():
        print("a is a str")
    case _:
        print("a is not an int, float, or str")

# > a is an int
```

Variable patterns (also known as binding patterns) are used to match any value. The value is assigned to the variable.

```python
a = 1

match a:
    case x:
        print(f"a is {x}")

# > a is 1
```

The wildcard pattern `_` is used to match any value. It is used as the last pattern in a `match` statement to match any
value that does not match any of the other patterns.

```python
a = 4

match a:
    case 1:
        print("a is 1")
    case 2:
        print("a is 2")
    case 3:
        print("a is 3")
    case _:
        print("a is not 1, 2, or 3")

# > a is not 1, 2, or 3
```

You can also unpack values in a `match` statement. This is useful when you want to match a value against multiple values
at once. This works with tuples, classes, types, dictionaries, and lists.

```python
a = (1, 2)

match a:
    case (1, 2):
        print("a is (1, 2)")
    case (3, 4):
        print("a is (3, 4)")
    case _:
        print("a is not (1, 2) or (3, 4)")

# > a is (1, 2)
```

You can also combine patterns in a `match` statement. This is useful when you want to match a value against multiple
patterns at once.

```python
a = 1

match a:
    case 1 | 2:
        print("a is 1 or 2")
    case 3 | 4:
        print("a is 3 or 4")
    case _:
        print("a is not 1, 2, 3, or 4")

# > a is 1 or 2
```

These patterns can be combined in any way you want.

```python
a = (1, (2, 3))

match a:
    case (1, (x, 3 | 4)):
        print(f"a is (1, ({x}, 3 | 4))")
    case _:
        print("a is not (1, (x, y))")

# > a is (1, (2, 3 | 4))
```

match statements can also have guards. Guards are used to add additional conditions to a pattern. Guards are added to a
pattern using the `if` keyword.

```python
a = 1

match a:
    case x if x > 0:
        print(f"a is {x} and {x} is greater than 0")
    case x if x < 0:
        print(f"a is {x} and {x} is less than 0")
    case _:
        print("a is 0")

# > a is 1 and 1 is greater than 0
```

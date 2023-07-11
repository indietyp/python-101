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

> **Note:** By no means are `match` statements necessary to learn Python. They are a relatively new feature in Python,
> and you can skip this section if you want. You can achieve the same results using `if` statements (we've done so for
> years and survived!).

`match` statements are a relatively new feature in Python. They are used to compare a value to a number of patterns and
execute code based on which pattern matches the value. `match` statements are similar to `switch` statements in other
languages.

Each `case` in a `match` statement is followed by a pattern and a colon. The code block following the `case` statement
is executed if the value matches the pattern.

There are several types of patterns, these include:

* Literal patterns
* Capture patterns
* Wildcard patterns
* Value patterns
* Group patterns
* Sequence patterns
* Mapping patterns
* Class patterns

### Literal Patterns

Literal patterns are used to match a value to a literal value. Literal patterns are written as the literal value.

```python
match 1:
    case 1:
        print("The value is 1")
    case 2:
        print("The value is 2")

# > The value is 1
```

### Capture Patterns

Capture patterns are used to match a value to a variable. Capture patterns are written as a variable name, the variable
name `_` is invalid, as it is used as a wildcard pattern.

```python
match 1:
    case x:
        print(f"The value is {x}")

# > The value is 1
```

### Wildcard Patterns

Wildcard patterns are used to match any value. Wildcard patterns are written as `_`.

```python
match 1:
    case _:
        print("The value is 1")

# > The value is 1
```

### Value Patterns

Value patterns are used to match against the value of a variable. Due to conflicts with capture patterns, value patterns
are only valid if they contain `.` (are accessing an attribute of a variable).

```python
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


color = Color.RED

match color:
    case Color.RED:
        print("The color is red")
    case Color.GREEN:
        print("The color is green")
    case Color.BLUE:
        print("The color is blue")

# > The color is red
```

### Group Patterns

Group patterns are written as `(...)`, they are not required, but can be used to make the code more readable. (They
cannot contain a comma, as otherwise they would be interpreted as a sequence pattern)

```python
match 1:
    case (1):
        print("The value is 1")
    case (2):
        print("The value is 2")

# > The value is 1
```

### Sequence Patterns

Sequence patterns are used to match a value to a sequence of values. Sequence patterns are written as `[...]`. Sequence
patterns can nest other patters as elements and use `*var` to capture the rest of the sequence.

```python
a = [1, 2, 3]

match a:
    case [1, *rest]:
        print(f"The rest of the sequence is {rest}")

# > The rest of the sequence is [2, 3]

match a:
    case [*rest, 3]:
        print(f"The rest of the sequence is {rest}")

# > The rest of the sequence is [1, 2]

match a:
    case [1, *rest, 3]:
        print(f"The rest of the sequence is {rest}")

# > The rest of the sequence is [2]

match a:
    case [1, 2, 3]:
        print("The sequence is [1, 2, 3]")

# > The sequence is [1, 2, 3]

match a:
    case [1, 2, 3, 4]:
        print("The sequence is [1, 2, 3, 4]")
    case [1, 2, 3]:
        print("The sequence is [1, 2, 3]")

# > The sequence is [1, 2, 3]
```

Sequence patterns can also be used to match tuples, in that case the sequence pattern is written as `(...)`.

```python
a = (1, 2, 3)

match a:
    case (1, *rest):
        print(f"The rest of the sequence is {rest}")

# > The rest of the sequence is (2, 3)
```

### Mapping Patterns

Mapping patterns are used to match a value to a mapping of values. Mapping patterns are written as `{...}`. Mapping
patterns can nest other patters as values and use `**var` to capture the rest of the mapping.

```python
a = {"a": 1, "b": 2, "c": 3}

match a:
    case {"a": 1, **rest}:
        print(f"The rest of the mapping is {rest}")

# > The rest of the mapping is {'b': 2, 'c': 3}

match a:
    case {"a": 1, **rest, "c": 3}:
        print(f"The rest of the mapping is {rest}")

# > The rest of the mapping is {'b': 2}

match a:
    case {"a": 1, "b": 2, "c": 3, "d": 4}:
        print("The mapping is {'a': 1, 'b': 2, 'c': 3, 'd': 4}")
    case {"a": 1, "b": 2, "c": 3}:
        print("The mapping is {'a': 1, 'b': 2, 'c': 3}")

# > The mapping is {'a': 1, 'b': 2, 'c': 3}
```

### Class Patterns

Class patterns are used to match a value to a class. Class patterns are written as `ClassName(...)`. Class patterns can
nest other patters as arguments and use `**var` to capture the rest of the mapping.

```python
class A:
    pass


a = A()

match a:
    case A():
        print("The value is an instance of A")

# > The value is an instance of A

match 1:
    case int():
        print("The value is an instance of int")
    case float():
        print("The value is an instance of float")

# > The value is an instance of int
```

### Guard Patterns

Guard patterns are used to match a value to a pattern and then check if a condition is true. Guard patterns are written
as `pattern if condition`.

```python
match 1:
    case x if x > 0:
        print(f"The value is {x}")

# > The value is 1
```

### As Patterns

As patterns are used to match a value to a pattern and then capture the value in a variable. As patterns are written
as `pattern as var`.

```python
match 1:
    case x as y:
        print(f"The value is {x}")
        print(f"The value is also {y}")

# > The value is 1
# > The value is also 1
```

### Or Patterns

Or patterns are used to match a value to multiple patterns. Or patterns are written as `pattern1 | pattern2`.

```python
match 1:
    case 1 | 2:
        print("The value is 1 or 2")

# > The value is 1 or 2

match 2:
    case 1 | 2:
        print("The value is 1 or 2")

# > The value is 1 or 2
```

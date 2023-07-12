# `match` Statements

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

## Literal Patterns

Literal patterns are used to match a value to a literal value. Literal patterns are written as the literal value.

```python
match 1:
    case 1:
        print("The value is 1")
    case 2:
        print("The value is 2")

# > The value is 1
```

## Capture Patterns

Capture patterns are used to match a value to a variable. Capture patterns are written as a variable name, the variable
name `_` is invalid, as it is used as a wildcard pattern.

```python
match 1:
    case x:
        print(f"The value is {x}")

# > The value is 1
```

## Wildcard Patterns

Wildcard patterns are used to match any value. Wildcard patterns are written as `_`.

```python
match 1:
    case _:
        print("The value is 1")

# > The value is 1
```

## Value Patterns

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

```admonish note title="What is an Enum?" collapsible=true

An Enum is a special type of class that is used to represent a set of values. 
Each value in the set is an instance of the class. 

Enums are useful when you want to represent a set of values that are related to each other.

```

## Group Patterns

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

## Sequence Patterns

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

## Mapping Patterns

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

## Class Patterns

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

## Guard Patterns

Guard patterns are used to match a value to a pattern and then check if a condition is true. Guard patterns are written
as `pattern if condition`.

```python
match 1:
    case x if x > 0:
        print(f"The value is {x}")

# > The value is 1
```

## As Patterns

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

## Or Patterns

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

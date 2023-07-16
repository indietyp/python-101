# Enumerations

Enumerations are a way to define a type that can only have a certain set of values. This is useful when you want to
restrict a variable to only be able to have a certain set of values.

Enumerations are created using the `Enum` class from the `enum` module.

```python
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)
# > Color.RED

print(Color.RED.name)
# > RED

print(Color.RED.value)
# > 1
```

## `auto()`

The `auto()` function can be used to automatically assign values to the enumeration members. This is preferable to
manually assigning values because it prevents the values from being accidentally duplicated.

```python
from enum import Enum, auto


class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


print(Color.RED)
# > Color.RED

print(Color.RED.name)
# > RED

print(Color.RED.value)
# > 1
```

## Iterating Over Enumerations

You can iterate over the values of an enumeration by iterating over the enumeration class itself.

```python
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


for color in Color:
    print(color)
# > Color.RED
# > Color.GREEN
# > Color.BLUE
```

## Flags

Flags are enumerations that can be combined using the bitwise operators `|` (or), `&` (and), `^` (xor), `~` (not).

```python
from enum import Flag, auto

class Color(Flag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(Color.RED)
# > Color.RED

print(Color.RED.name)
# > RED

print(Color.RED.value)
# > 1

print(Color.RED | Color.GREEN)
# > Color.RED|GREEN

print(Color.RED | Color.GREEN | Color.BLUE)
# > Color.RED|GREEN|BLUE
```

### Flag Operations

There are multiple operations that can be performed on flags. These include:

* `|` (or) - combines the flags
* `&` (and) - returns the flags that are common to both flags
* `^` (xor) - returns the flags that are not common to both flags
* `~` (not) - returns the flags that are not in the flag
* `==` (equals) - returns true if the flags are equal
* `!=` (not equals) - returns true if the flags are not equal
* `in` - returns true if the flag is in the flag
* `not in` - returns true if the flag is not in the flag

```python
from enum import Flag, auto

class Color(Flag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(Color.RED | Color.GREEN)
# > Color.RED|GREEN

print(Color.RED & Color.GREEN)
# > 0

print(Color.RED ^ Color.GREEN)
# > Color.RED|GREEN

print(~Color.RED)
# > Color.GREEN|BLUE

print(Color.RED == Color.RED)
# > True

print(Color.RED == Color.GREEN)
# > False

print(Color.RED != Color.RED)
# > False

print(Color.RED != Color.GREEN)
# > True

print(Color.RED in Color.RED)
# > True

print(Color.RED in Color.GREEN)
# > False

print(Color.RED not in Color.RED)
# > False

print(Color.RED not in Color.GREEN)
# > True

print(Color.RED in Color.RED | Color.GREEN)
# > True

print(Color.RED in Color.GREEN | Color.BLUE)
# > False
```

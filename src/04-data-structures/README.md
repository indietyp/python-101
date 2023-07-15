# Data Structures

In the previous chapters we have talked about primitive data types, such as `int`, `float`, `bool`, `str`, and `None`.
These are the basic building blocks of any program, but they are not enough to solve most real-world problems. In this
chapter we will introduce more complex data types, which are called **data structures**.

This includes:

* Lists
* Tuples
* Sets
* Dictionaries
* Data classes
* Enumerations

## Lists

Lists are an ordered collection of items. They are created using square brackets `[]` and items are separated by commas,
in contrast to other programming languages, items in a list do not need to be of the same type.

```python
a = [1, 2, 3, 4, 5]
```

Lists are zero-indexed, meaning that the first element has index 0, the second element has index 1, and so on. You can
access elements of a list using square brackets `[]` and the index of the element you want to access.

```python
a = [1, 2, 3, 4, 5]

print(a[0])
# > 1
print(a[1])
# > 2
```

When trying to access an element that does not exist, you will get an `IndexError`.

```python
a = [1, 2, 3, 4, 5]

print(a[5])
# > IndexError: list index out of range
```

Lists are mutable, this means you can manipulate them after they have been created.

There are several methods you can use to modify lists:

* `append`: Add an element to the end of the list
* `insert`: Insert an element at a specific index
* `remove`: Remove an element from the list
* `pop`: Remove an element from end of the list
* `clear`: Remove all elements from the list

`remove` and `pop` will both return the element that was removed.

```python
a = [1, 2, 3, 4, 5]
a.append(6)

print(a)
# > [1, 2, 3, 4, 5, 6]

a.insert(0, 0)

print(a)
# > [0, 1, 2, 3, 4, 5, 6]

a.remove(0)
# > [1, 2, 3, 4, 5, 6]

a.pop()
# > [1, 2, 3, 4, 5]

a.clear()
# > []
```

You can also change the value of an element in a list by assigning a new value to it.

```python
a = [1, 2, 3, 4, 5]

a[0] = 0

print(a)
# > [0, 2, 3, 4, 5]
```

You can also use the `del` keyword to delete an element from a list.

> **Note:** use of `del` is generally discouraged, as it is harder to compose with functions and not as readable.

```python
a = [1, 2, 3, 4, 5]

del a[0]

print(a)
# > [2, 3, 4, 5]
```

### Slicing

You can also access multiple elements of a list at once using **slicing**. Slicing is done using the colon `:` operator.

Slicing has the following syntax:

```python
list[start:stop:step]
```

* `start`: The index of the first element to include in the slice
* `stop`: The index of the first element to exclude from the slice
* `step`: The step size between elements in the slice

```python
a = [1, 2, 3, 4, 5]

print(a[0:2])  # The step size is 1 by default, if omitted
# > [1, 2]

print(a[0:5:2])
# > [1, 3, 5]

print(a[::2])  # You can omit the start and stop values, they will default to the beginning and end of the list
# > [1, 3, 5]

print(a[::-1])  # You can use negative values to count from the end of the list
# > [5, 4, 3, 2, 1]
```

### List Comprehensions

List comprehensions are a way to create lists from other iterables, such as lists, tuples, sets, and dictionaries. They
are created using square brackets `[]`. Their syntax is similar to a `for` loop.

```python
a = [1, 2, 3, 4, 5]

b = [x * 2 for x in a]

print(b)
# > [2, 4, 6, 8, 10]
```

## Tuples

Tuples are an ordered collection of items. They are created using parentheses `()` and items are separated by commas.
They are fundamentally different from lists in that they are **immutable**, meaning that they cannot be changed after
they have been created. Tuples with one element are created by adding a comma after the element (as otherwise it is
impossible to distinguish them from parentheses).

```python
a = (1, 2, 3, 4, 5)

print(a[0])
# > 1

a[0] = 0
# > TypeError: 'tuple' object does not support item assignment
```

An empty tuple is created using `()`.

```python
a = ()
```

## Sets

Sets are an unordered collection of unique items. They are created using curly braces `{}` and items are separated by
commas. They are especially useful for checking if an item is in a collection, as they have a constant time lookup.

```python
a = {1, 2, 3, 4, 5}

print(1 in a)
# > True

print(6 in a)
# > False
```

There are several methods you can use to modify sets:

* `add`: Add an element to the set
* `remove`: Remove an element from the set
* `discard`: Remove an element from the set, if it exists
* `pop`: Remove an element from the set
* `clear`: Remove all elements from the set

`remove` and `pop` will both return the element that was removed.

```python
a = {1, 2, 3, 4, 5}

a.add(6)

print(a)
# > {1, 2, 3, 4, 5, 6}

a.remove(6)
# a = {1, 2, 3, 4, 5}

a.discard(6)
# a = {1, 2, 3, 4, 5}

a.remove(6)
# > KeyError: 6

a.pop()
# > 1

a.clear()
# a = set()
```

> **Note:** Empty sets need to be created using the `set()` function, as `{}` creates an empty dictionary.

### Frozen Sets

Frozen sets are an immutable version of sets. They are created using the `frozenset()` function. (They are what tuples
are to lists).

```python
a = frozenset({1, 2, 3, 4, 5})

print(a[0])
# > TypeError: 'frozenset' object does not support indexing

a.add(6)
# > AttributeError: 'frozenset' object has no attribute 'add'
```

### Operations

You can use the bitwise operators `|`, `&`, `-`, and `^` to perform set operations.

* `|`: Union
* `&`: Intersection
* `-`: Difference
* `^`: Symmetric Difference

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)
# > {1, 2, 3, 4, 5, 6, 7, 8}

print(a & b)
# > {4, 5}

print(a - b)
# > {1, 2, 3}

print(a ^ b)
# > {1, 2, 3, 6, 7, 8}
```

### Set Comprehensions

Set comprehensions are a way to create sets from other iterables, such as lists, tuples, sets, and dictionaries. They
are created using curly braces `{}`. Their syntax is similar to a `for` loop.

```python
a = {1, 2, 3, 4, 5}

b = {x * 2 for x in a}

print(b)
# > {2, 4, 6, 8, 10}
```

## Dictionaries

Dictionaries are an unordered collection of key-value pairs. They are created using curly braces `{}` and items are
separated by commas. Each item is a key-value pair, separated by a colon `:`. Keys must be unique and immutable, while
values can be any type.

```python
a = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

print(a['a'])
# > 1
```

You can use the `in` operator to check if a key exists in a dictionary.

```python
a = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

print('a' in a)
# > True

print('f' in a)
# > False
```

Dictionaries are mutable, so you can add, remove, and change items. Common methods include:

* `update`: Update the dictionary with the key-value pairs from another dictionary
* `clear`: Remove all items from the dictionary
* `pop`: Remove an item from the dictionary
* `setdefault`: Get the value for a key, or set a default value if the key does not exist

> **Note:** `setdefault` is similar to `get`, but will set the value for the key if it does not exist.

> **Note:** `del` is discouraged, as it is not a method and can be confusing.

> **Note:** `update` can be replaced with the `|` operator.

```python
a = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

a['f'] = 6
# a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

del a['f']
# a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

a.pop('e')
# > 5
# a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}

a.update(b)
# a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}

c = a | b

print(c)
# > {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### Dictionary Comprehensions

Dictionary comprehensions are a way to create dictionaries from other iterables, such as lists, tuples, sets, and other
dictionaries. They are created using curly braces `{}`. Their syntax is similar to a `for` loop.

```python
a = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

b = {k: v * 2 for k, v in a.items()}
# b = {1: 'aa', 2: 'bb', 3: 'cc', 4: 'dd', 5: 'ee'}

c = {k: v * 2 for k, v in a.items() if k % 2 == 0}
# c = {2: 'bb', 4: 'dd'}
```

## Data classes

Data classes are a way to create classes that are used to store data. They are created using the `dataclass` decorator
from the `dataclasses` module. They are similar to named tuples, but are mutable and can be inherited from.

They are an easy way to create classes that are used to store data, as they automatically create the `__init__` method.

```python
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    height: float

    def greet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')


person = Person('John', 30, 1.8)

print(person.name)
# > John

person.greet()
# > Hello, my name is John and I am 30 years old.
```

## Enumerations

Enumerations are a way to create classes that are used to store a set of constants. They are created using the `Enum`
class from the `enum` module.

```python
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)
# > Color.RED

print(Color.RED.value)
# > 1

print(Color(1))
# > Color.RED
```

You can also use them to create a flag, which is a set of constants that can be combined using the `|` operator. These
flags kind of act like immutable sets, meaning you can use the `&`, `|`, and `^` operators on them, you can negate them
using the `~` operator, and you can check if they are a subset or superset of another flag using the `<=` and `>=`
operators. To check if a flag contains a value, you can use the `in` operator.

They are immensely useful when trying to represent a finite set of options, which can be combined in different ways.

```python
from enum import Flag, auto


class Color(Flag):
    RED = auto()  # automatically assign a value
    GREEN = auto()
    BLUE = auto()


print(Color.RED | Color.GREEN)
# > Color.RED | Color.GREEN

print(Color.RED | Color.GREEN | Color.BLUE)
# > Color.RED | Color.GREEN | Color.BLUE

print(Color.RED | Color.BLUE)
# > Color.RED | Color.BLUE

print(Color.RED & Color.GREEN)
# > 0

print(Color.RED & Color.RED)
# > Color.RED

print(~Color.RED)
# > Color.GREEN | Color.BLUE

print(Color.RED in Color.RED)
# > True

print(Color.RED in Color.GREEN)
# > False

print(Color.RED in (Color.RED | Color.GREEN))
# > True

print(Color.RED in (Color.GREEN | Color.BLUE))
# > False

print(Color.RED <= Color.RED)
# > True

print(Color.RED <= (Color.RED | Color.GREEN))
# > True

print(Color.RED <= (Color.GREEN | Color.BLUE))
# > False

print(Color.RED >= Color.RED)
# > True

print(Color.RED >= (Color.RED | Color.GREEN))
# > False

print(Color.RED >= (Color.GREEN | Color.BLUE))
# > False

print(Color.RED ^ Color.GREEN)
# > Color.RED | Color.GREEN

print(Color.RED ^ Color.RED)
# > 0
```

# Sets

Sets are unordered collections of unique elements. Meaning there can only be one representative of the same object in a
set. Sets are mutable, meaning they can be changed after they are created. Sets are created using curly braces `{}`.

To be able to use an object as an element in a set, it must be hashable. Hashable objects are objects that have
a `__hash__` method. Immutable objects are hashable, whereas mutable objects are not. This is because the hash of an
object is based on its contents, and mutable objects can change their contents.

```python
a = {1, 2, 3, 4, 5}

print(a)
# > {1, 2, 3, 4, 5}
```

## Empty Sets

Empty sets are created using the `set()` constructor.

```python
a = set()

print(a)
# > set()
```

> **Note:** You cannot create an empty set using `{}` because that creates an empty dictionary.

## Set Methods

Sets have a number of methods that can be used to manipulate them. The most common ones are:

* `add()` - Adds an element to the set.
* `remove()` - Removes an element from the set.
* `discard()` - Removes an element from the set if it is a member.
* `pop()` - Removes and returns an arbitrary element from the set.
* `clear()` - Removes all elements from the set.

```python
a = {1, 2, 3, 4, 5}

a.add(6)
print(a)
# > {1, 2, 3, 4, 5, 6}

a.remove(6)
print(a)
# > {1, 2, 3, 4, 5}

a.discard(5)
print(a)
# > {1, 2, 3, 4}

a.remove(6)
# > KeyError: 6

a.discard(6)
# > No error

a.pop()
print(a)
# > {2, 3, 4}

a.clear()
print(a)
# > set()
```

## Set Membership

You can check if an item is in a set using the `in` operator.

```python
a = {1, 2, 3, 4, 5}

print(1 in a)
# > True

print(6 in a)
# > False
```

## Set Operations

Sets have a number of operations that can be used to manipulate them. The most common ones are:

* `|` (or `union()`) - Returns the union of two sets.
* `&` (or `intersection()`) - Returns the intersection of two sets.
* `-` (or `difference()`) - Returns the difference of two sets.
* `^` (or `symmetric_difference()`) - Returns the symmetric difference of two sets.

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)
# > {1, 2, 3, 4, 5, 6, 7, 8}

print(a & b)
# > {4, 5}

print(a - b)
# > {1, 2, 3}

print(b - a)
# > {8, 6, 7}

print(a ^ b)
# > {1, 2, 3, 6, 7, 8}
```

> **Note:** The methods are equivalent to their operators, but perform the operation in-place.

## Set Comprehensions

Set comprehensions are similar to list comprehensions, but create sets instead of lists.

```python
a = {x for x in range(10)}

print(a)
# > {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
```

## Frozen Sets

Frozen sets are immutable sets. They are created using the `frozenset()` constructor. They are hashable, and can be used
as elements in other sets or as keys in dictionaries.

```python
a = frozenset({1, 2, 3, 4, 5})

print(a)
# > frozenset({1, 2, 3, 4, 5})

a.add(6)
# > AttributeError: 'frozenset' object has no attribute 'add'
```

Because frozensets are immutable, we can use the bitwise operators to perform set operations on them, but not their
corresponding methods.

```python
a = frozenset({1, 2, 3, 4, 5})
b = frozenset({4, 5, 6, 7, 8})

print(a | b)
# > frozenset({1, 2, 3, 4, 5, 6, 7, 8})

print(a & b)
# > frozenset({4, 5})

print(a - b)
# > frozenset({1, 2, 3})

print(b - a)
# > frozenset({8, 6, 7})

print(a ^ b)
# > frozenset({1, 2, 3, 6, 7, 8})
```

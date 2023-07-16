# Dictionaries

Dictionaries are an unordered collection of key-value pairs. They are similar to lists, but instead of accessing
elements by their index, they are accessed by their key. They are created using curly braces `{}`. Items are separated
by commas `,`, and key-value pairs are separated by colons `:`.

```python
a = {'a': 1, 'b': 2, 'c': 3}

print(a)
# > {'a': 1, 'b': 2, 'c': 3}
```

## Accessing Items

Items in a dictionary can be accessed using their key. When accessing a key that doesn't exist, a `KeyError` is raised.

```python
a = {'a': 1, 'b': 2, 'c': 3}

print(a['a'])
# > 1

print(a['b'])
# > 2

print(a['d'])
# > KeyError: 'd'
```

## Adding Items

Items can be added to a dictionary by assigning a value to a new key.

```python
a = {'a': 1, 'b': 2, 'c': 3}

a['d'] = 4

print(a)
# > {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

## Removing Items

Items can be removed from a dictionary using the `del` keyword.

```python
a = {'a': 1, 'b': 2, 'c': 3}

del a['a']

print(a)
# > {'b': 2, 'c': 3}
```

> **Note:** Personal Taste: Personally I prefer using the `pop()` method to remove items from a dictionary, as it
> returns the value of the key that was removed. It is also more composable than the `del` keyword.

## Dictionary Methods

There are several methods that can be used on dictionaries, the most common ones are:

* `keys()`: Returns a list of all the keys in the dictionary.
* `values()`: Returns a list of all the values in the dictionary.
* `items()`: Returns a list of all the key-value pairs in the dictionary.
* `get()`: Returns the value of a key, or a default value if the key doesn't exist.
* `pop()`: Removes a key-value pair from the dictionary and returns the value.
* `clear()`: Removes all key-value pairs from the dictionary.
* `update()`: Updates the dictionary with the key-value pairs from another dictionary.
* `copy()`: Returns a copy of the dictionary.
* `setdefault()`: Returns the value of a key, or sets it to a default value if it doesn't exist.

```python
a = {'a': 1, 'b': 2, 'c': 3}

print(a.keys())
# > dict_keys(['a', 'b', 'c'])

print(a.values())
# > dict_values([1, 2, 3])

print(a.items())
# > dict_items([('a', 1), ('b', 2), ('c', 3)])

print(a.get('a'))
# > 1

print(a.get('d'))
# > None

print(a.get('d', 4))
# > 4

print(a.pop('a'))
# > 1

print(a)
# > {'b': 2, 'c': 3}

print(a.setdefault('b'))
# > 2

print(a.setdefault('d', 4))
# > None

print(a)
# > {'b': 2, 'c': 3, 'd': 4}

a.clear()
print(a)
# > {}

a = {'a': 1, 'b': 2, 'c': 3}
b = {'d': 4, 'e': 5, 'f': 6}

a.update(b)
print(a)
# > {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

c = a.copy()
print(c)
# > {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

c.pop('a')
print(c)
# > {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

print(a)
# > {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# You can also use `|` to merge two dictionaries.
a = {'a': 1, 'b': 2, 'c': 3}
b = {'d': 4, 'e': 5, 'f': 6}

c = a | b
print(c)
# > {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
```

## Dictionary Comprehensions

Dictionary comprehensions are similar to list comprehensions, but instead of creating a list, they create a dictionary.

```python
a = {x: x**2 for x in range(5)}

print(a)
# > {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Iterating Over Dictionaries

Iterating over a dictionary will iterate over its keys.

```python
a = {'a': 1, 'b': 2, 'c': 3}

for key in a:
    print(key)

# > a
# > b
# > c
```

To iterate over the values, you can use the `values()` method.

```python
a = {'a': 1, 'b': 2, 'c': 3}

for value in a.values():
    print(value)

# > 1
# > 2
# > 3
```

To iterate over the key-value pairs, you can use the `items()` method.

```python
a = {'a': 1, 'b': 2, 'c': 3}

for key, value in a.items():
    print(key, value)

# > a 1
# > b 2
# > c 3
```

## Dictionary Membership

You can check if a key exists in a dictionary using the `in` keyword.

```python
a = {'a': 1, 'b': 2, 'c': 3}

print('a' in a)
# > True

print('d' in a)
# > False
```

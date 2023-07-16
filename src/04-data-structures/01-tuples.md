# Tuples

Tuples are an immutable ordered sequence of elements. They are similar to lists, but they are immutable, meaning that
they cannot be changed after they are created. They are created using parentheses instead of square brackets.

```python
a = (1, 2, 3, 4, 5)

print(a)
# > (1, 2, 3, 4, 5)

b = (1, 'a', 2, 'b', 3, 'c')
print(b)
```

> **Note:** Due to their immutable nature they can be used as keys in dictionaries, whereas lists cannot.

Because of their immutable nature, tuples are faster than lists. If you have a sequence of items that you know will not
change, you should use a tuple instead of a list.

## Accessing Items

Indexing of items is the exact same as lists. They are also zero-indexed and allow for negative indexing, and slicing.

When indexing out of bounds, an `IndexError` is raised.

```python
a = (1, 2, 3, 4, 5)

print(a[0])
# > 1

print(a[2])
# > 3

print(a[-1])
# > 5

print(a[-3])
# > 3

print(a[5])
# > IndexError: tuple index out of range
```

## Empty and Single-Item Tuples

Empty tuples are created using `()`.

```python
a = ()

print(a)
# > ()
```

Single-item tuples are created by adding a comma `,` after the item, otherwise it wouldn't be possible to distinguish
between a tuple and a grouping of parentheses.

```python
a = (1,)
b = ('a',)
c = (1, 'a')

print(a)
# > (1,)
print(b)
# > ('a',)
print(c)
# > (1, 'a')
```

## Tuple Packing and Unpacking

Tuple packing is when you create a tuple and assign it to a single variable.

```python
a = 1, 2, 3, 4, 5

print(a)
# > (1, 2, 3, 4, 5)
```

Tuple unpacking is when you assign a tuple to multiple variables.

```python
a = 1, 2, 3, 4, 5

b, c, d, e, f = a

print(b)
# > 1
print(c)
# > 2
print(d)
# > 3
print(e)
# > 4
print(f)
# > 5
```

You can use `*` to unpack the rest of the tuple into a single variable.

```python
a = 1, 2, 3, 4, 5

b, *c, d = a

print(b)
# > 1
print(c)
# > [2, 3, 4]
print(d)
# > 5
```

## Tuple Methods

Tuples have two methods: `count` and `index`.

`count` returns the number of times an item appears in a tuple.

```python

a = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

print(a.count(1))
# > 2

print(a.count(6))
# > 0
```

`index` returns the index of the first occurrence of an item in a tuple.

```python
a = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

print(a.index(1))
# > 0

print(a.index(6))
# > ValueError: tuple.index(x): x not in tuple
```

## Tuple Concatenation and Repetition

Tuples can be concatenated using the `+` operator.

```python
a = (1, 2, 3)
b = (4, 5, 6)

print(a + b)

# > (1, 2, 3, 4, 5, 6)
```

Tuples can be repeated using the `*` operator.

```python
a = (1, 2, 3)

print(a * 3)
# > (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

## Tuple Membership

You can check if an item is in a tuple using the `in` operator.

```python
a = (1, 2, 3, 4, 5)

print(1 in a)
# > True

print(6 in a)
# > False
```

> **Note:** When you see yourself using tuples to primarily check for membership, you should consider using a frozenset
> instead.

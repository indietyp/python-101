# Lists

Lists are an ordered collection of items, they can contain any type of data, and can be modified after creation (they
are mutable). Lists allow for duplicate items, they are indexed, and are iterable.

## Creating Lists

Lists are created using square brackets `[]` and items are separated by commas `,`.

```python
a = [1, 2, 3, 4, 5]

print(a)
# > [1, 2, 3, 4, 5]

b = [1, 'a', 2, 'b', 3, 'c']
print(b)
```

## Accessing Items

Items in a list can be accessed using their index. They are zero-indexed, meaning the first item is at index `0`, the
second item is `1`, and so on. Indexes can also be negative, where `-1` is the last item, `-2` is the second to last
item, etc.

When indexing out of bounds, an `IndexError` is raised.

```python
a = [1, 2, 3, 4, 5]

print(a[0])
# > 1

print(a[2])
# > 3

print(a[-1])
# > 5

print(a[-3])
# > 3

print(a[5])
# > IndexError: list index out of range
```

## Slicing

Slicing is a way to get a subset of a list. It is done by specifying a start index, an end index, and a step. The start
index is inclusive, the end index is exclusive, and the step is the number of items to skip.

They syntax for slicing is `list[start:end:step]`. If any of the values are omitted, they default to the
following: `list[0:len(list):1]`.

```python
a = [1, 2, 3, 4, 5]

print(a[1:3])  # when omitting the step we can also omit the colon
# > [2, 3]

print(a[1:5:2])
# > [2, 4]

print(a[::2])
# > [1, 3, 5]

print(a[1::2])
# > [2, 4]

print(a[::-1])
# > [5, 4, 3, 2, 1]
```

## Modifying Lists

Lists are mutable, meaning they can be modified after creation. This is done by assigning a new value to an index or a
slice.

```python
a = [1, 2, 3, 4, 5]

a[0] = 10
print(a)
# > [10, 2, 3, 4, 5]

a[1:3] = [20, 30]
print(a)
# > [10, 20, 30, 4, 5]

a[1:3] = [40, 50, 60, 70]
print(a)
# > [10, 40, 50, 60, 70, 4, 5]
```

You can also use methods to modify lists. Some of the most common methods are:

* `append(item)` - adds an item to the end of the list
* `extend(list)` - adds all items in the given list to the end of the list
* `insert(index, item)` - inserts an item at the given index
* `remove(item)` - removes the first occurrence of the given item
* `pop()` - removes and returns the last item in the list
* `pop(index)` - removes and returns the item at the given index
* `clear()` - removes all items from the list

```python
a = [1, 2, 3, 4, 5]

a.append(6)
print(a)
# > [1, 2, 3, 4, 5, 6]

a.extend([7, 8, 9])
print(a)
# > [1, 2, 3, 4, 5, 6, 7, 8, 9]

a.insert(0, 0)
print(a)
# > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a.remove(0)
print(a)
# > [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = a.pop()
print(a)
# > [1, 2, 3, 4, 5, 6, 7, 8]
print(b)
# > 9

c = a.pop(0)
print(a)
# > [2, 3, 4, 5, 6, 7, 8]
print(c)
# > 1

a.clear()
print(a)
# > []
```

> **Note:** To remove an item at a specific index, you can use the `del` keyword. `del a[0]`. This is generally
> discouraged as it is not as readable as `a.pop(0)` and does not return the removed item. Usage of `del` is also less
> composable.

## List Comprehensions

List comprehensions are a way to create lists from other iterables. They are a more concise way to create lists than
when using a `for` loop. (The syntax is very reminiscent of the standard `for` loop syntax.)

```python
a = [1, 2, 3, 4, 5]

b = [x * 2 for x in a]
print(b)
# > [2, 4, 6, 8, 10]

# exactly the same as
b = []
for x in a:
    b.append(x * 2)
print(b)
# > [2, 4, 6, 8, 10]
```

List comprehensions can also be used to filter items.

```python
a = [1, 2, 3, 4, 5]

b = [x for x in a if x % 2 == 0]
print(b)
# > [2, 4]

# exactly the same as
b = []
for x in a:
    if x % 2 == 0:
        b.append(x)
print(b)
# > [2, 4]
```

## List Unpacking

List unpacking is a way to assign multiple variables at once from a list. It is done by assigning the variables to the
list.

```python
a = [1, 2, 3, 4, 5]

[e, f, g, h, i] = a

print(e)
# > 1

print(f)
# > 2

print(g)
# > 3

print(h)
# > 4

print(i)
# > 5
```

You can also use the `*` operator to assign the remaining items to a variable.

```python
a = [1, 2, 3, 4, 5]

[e, *f, g] = a

print(e)
# > 1

print(f)
# > [2, 3, 4]

print(g)
# > 5
```

## List Membership

You can check if an item is in a list using the `in` operator.

```python
a = [1, 2, 3, 4, 5]

print(1 in a)
# > True

print(6 in a)
# > False
```

> **Note:** When you see yourself primarily using the `in` operator, you should consider using a `set` instead of
> a `list`, as the `in` operator is much faster on sets.

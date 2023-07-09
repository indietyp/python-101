# Primitive Types

In Python, there are different types of values, we will get into more detail about these types in the data structures
chapter.

Primitive types are the most basic types of values, they are the building blocks of all other types of values. They are
called primitive types because they are not built using other types of values.

Python supports the following primitive types:

* Numeric types
    * `int`
    * `float`
    * `complex`
* Strings
* Booleans
* `None`

## Numeric types

Numeric types are used to represent numbers. Python supports three numeric types: `int`, `float` and `complex`.
The `int` type is used to represent integers, the `float` type is used to represent floating point numbers, and are very
heavily used. The `complex` type is used to represent complex numbers, which are not used very often.

The following example shows how to use numeric types:

```python
print(42)
# > 42
print(42.0)
# > 42.0
print(42 + 0j)
# > (42+0j)
```

Each numeric type has their respective functions, which can be used to convert a value to that type. The following
example shows how to convert a string to a numeric type:

```python
value = "42"
print(int(value))
# > 42
print(float(value))
# > 42.0
print(complex(value))
# > (42+0j)
```

```admonish note title="Deep Dive" collapsible=true

Why do we need different numeric types? Why can't we just use `float` for everything?

The reasons behind this are very technical, but the main reason is that `float` is not precise, and can't 
represent all possible numbers.

So you are probably wondering, why is that the case?
We can look at an example to understand why, imagine storing irrational numbers, like `pi` and `e`, we would need to use infinite memory to store them, as they have infinite digits after the decimal point,
but to be able to use them in a computer, we need to store them in finite memory, so we need to use approximations. These are stored as `float` values, and are approximations of the actual value.
These approximations are very close to the actual value, but they are not exact. This is a problem, as for some operations, we need them to be exact, this is where `int` comes in, `int` is exact, and can represent all possible integers, but it can't represent non-integers, like `pi` and `e`.

Going even deeper, instead of decimal values (base 10), the computer operates on binary values (base 2) and has no concept of floating point numbers. 
This means that we need an efficient way to represent floating point numbers in binary (efficient in multiple ways, like memory usage, execution speed, etc.), and this is where the IEEE 754 standard comes in, it defines a way to represent floating point numbers in binary, and this is what `float` uses.
These values are limited to 64 bits, which means that they can't represent all possible numbers, and this is why `float` is not precise.

This means that `0.123` is actually stored as `00111101111110111110011101101101` in the computer, pretty cool, right?

```

## Strings

Strings are used to represent text. You can construct a string by surrounding a sequence of characters with either
single quotes (`'`) or double quotes (`"`). The following example shows how to construct a string:

```python
print('Hello World!')
# > Hello World!
print("Hello World!")
# > Hello World!
```

You cannot mix single quotes and double quotes, the following example shows what happens when you try to do that:

```python
print('Hello World!")
# > SyntaxError: EOL while scanning string literal
```

You cannot use a new line in a string, the following example shows what happens when you try to do that:

```python
print('Hello
World!')
# > SyntaxError: EOL while scanning string literal
```

To be able to use a newline in a string, you can either use the `\n` escape sequence, or use a multiline string. The
following example shows how to use the `\n` escape sequence:

```python
print('Hello\nWorld!')
# > Hello
# > World!
```

The following example shows how to use a multiline string:

```python
print('''Hello
World!''')
# > Hello
# > World!
```

You can use some of the arithmetic operators with strings, the following example shows how to use the `+` operator with
strings:

```python
print('Hello' + 'World!')
# > HelloWorld!
```

You can also use the `*` operator with strings, the following example shows how to use the `*` operator with strings:

```python
print('Hello' * 3)
# > HelloHelloHello
```

You can also include values in strings using `f-strings`, the following example shows how to use `f-strings`:

```python
name = 'John'
print(f'Hello {name}!')
# > Hello John!
```

## Booleans

Booleans are used to represent truth values. Booleans can only have two values, `True` and `False`.

The following example shows how to use booleans:

```python
print(True)
# > True
print(False)
# > False
```

You can produce booleans using comparison operators, the following example shows how to use comparison operators:

```python
print(1 == 1)
# > True
print(1 != 1)
# > False
```

## `None`

`None` expresses the absence of a value. This value is usually returned by functions that either don't return anything,
or only return something under certain conditions.

The following example shows how to use `None`:

```python
print(None)
# > None
```

# Methods and Functions

We won't get into too much detail about methods and functions in this chapter, as we will get into more detail about
them in the functions chapter.

Functions are pieces of code that can be reused, they are used to perform a specific task. Functions can take inputs,
and can return outputs.

There are two types of functions, methods and functions. Methods are functions that are attached to an object, and are
called using the dot notation. Functions are not attached to an object, and are called using their name.

The following example shows how to call a method:

```python
print('Hello World!'.lower())
# > hello world!
```

The following example shows how to call a function:

```python
print(len('Hello World!'))
# > 12
```

## Built-in Functions

Python comes with a lot of built-in functions and methods with can be used to perform a wide variety of tasks. These
include:

You can find a full list of built-in functions [here](https://docs.python.org/3/library/functions.html).

### `print`

The `print` function is used to print a value to the console. The following example shows how to use the `print`
function:

```python
print('Hello World!')
# > Hello World!
```

### `input`

The `input` function is used to get input from the user. The following example shows how to use the `input` function:

```python
name = input('Enter your name: ')
print(f'Hello {name}!')
# > Enter your name: John
# > Hello John!
```

### `type`

The `type` function is used to get the type of a value. The following example shows how to use the `type` function:

```python
print(type(1))
# > <class 'int'>
print(type(1.0))
# > <class 'float'>
print(type('Hello World!'))
# > <class 'str'>
print(type(True))
# > <class 'bool'>
print(type(None))
# > <class 'NoneType'>
```

### `int`, `float`, `str`, `bool`

The `int`, `float`, `str`, and `bool` functions are used to convert values to integers, floats, strings, and booleans.

The following example shows how to use the `int` function:

```python
print(int(1.0))
# > 1
print(int('1'))
# > 1
print(int(True))
# > 1
print(int(False))
# > 0
```

The following example shows how to use the `float` function:

```python
print(float(1))
# > 1.0
print(float('1'))
# > 1.0
print(float(True))
# > 1.0
print(float(False))
# > 0.0
```

The following example shows how to use the `str` function:

```python
print(str(1))
# > '1'
print(str(1.0))
# > '1.0'
print(str(True))
# > 'True'
print(str(False))
# > 'False'
```

The following example shows how to use the `bool` function:

```python
print(bool(1))
# > True
print(bool(1.0))
# > True
print(bool('Hello World!'))
# > True
print(bool(None))
# > False
```

### `len`

The `len` function is used to get the length of a value. The following example shows how to use the `len` function:

```python
print(len('Hello World!'))
# > 12
```

### `open`

The `open` function is used to open a file. The following example shows how to use the `open` function:

```python
file = open('file.txt', 'r')
print(file.read())
# > Hello World!
file.close()
```

### `help`

The `help` function is used to get help on a function. The following example shows how to use the `help` function:

```python
help(print)
# > Help on built-in function print in module builtins:
# >
# > print(...)
# >     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# >
# >     Prints the values to a stream, or to sys.stdout by default.
# >     Optional keyword arguments:
# >     file:  a file-like object (stream); defaults to the current sys.stdout.
# >     sep:   string inserted between values, default a space.
# >     end:   string appended after the last value, default a newline.
# >     flush: whether to forcibly flush the stream.
```

### `eval`

The `eval` function is used to evaluate a string as a Python expression. The following example shows how to use
the `eval` function:

```python
print(eval('1 + 1'))
# > 2
```

> **Note:** The `eval` function is dangerous, and should not be used unless you know what you are doing.

### Built-in Methods

#### `str`

The `str` has a multitude of methods, some of which are shown below. You can find a full list of methods on
the [Python documentation](https://docs.python.org/3/library/stdtypes.html#string-methods).

##### `lower`

The `lower` method is used to convert a string to lowercase. The following example shows how to use the `lower` method:

```python
print('Hello World!'.lower())
# > hello world!
```

##### `upper`

The `upper` method is used to convert a string to uppercase. The following example shows how to use the `upper` method:

```python
print('Hello World!'.upper())
# > HELLO WORLD!
```

##### `title`

The `title` method is used to convert a string to title case. The following example shows how to use the `title` method:

```python
print('hello world!'.title())
# > Hello World!
```

##### `capitalize`

The `capitalize` method is used to capitalize the first letter of a string. The following example shows how to use the
`capitalize` method:

```python
print('hello world!'.capitalize())
# > Hello world!
```

##### `strip`

The `strip` method is used to remove whitespace from the beginning and end of a string. The following example shows how
to use the `strip` method:

```python
print('   Hello World!   '.strip())
# > Hello World!
```

##### `lstrip`

The `lstrip` method is used to remove whitespace from the beginning of a string. The following example shows how to use
the `lstrip` method:

```python
print('   Hello World!   '.lstrip())
# > Hello World!   
```

##### `rstrip`

The `rstrip` method is used to remove whitespace from the end of a string. The following example shows how to use the
`rstrip` method:

```python
print('   Hello World!   '.rstrip())
# >    Hello World!
```

##### `replace`

The `replace` method is used to replace a substring with another substring. The following example shows how to use the
`replace` method:

```python
print('Hello World!'.replace('World', 'Universe'))
# > Hello Universe!
```

##### `split`

The `split` method is used to split a string into a list of substrings. The following example shows how to use the
`split` method:

```python
print('Hello World!'.split())
# > ['Hello', 'World!']
```

##### `join`

The `join` method is used to join a list of substrings into a string. The following example shows how to use the
`join` method:

```python
print(' '.join(['Hello', 'World!']))
# > Hello World!
```

##### `startswith`

The `startswith` method is used to check if a string starts with a substring. The following example shows how to use the
`startswith` method:

```python
print('Hello World!'.startswith('Hello'))
# > True
```

##### `endswith`

The `endswith` method is used to check if a string ends with a substring. The following example shows how to use the
`endswith` method:

```python
print('Hello World!'.endswith('World!'))
# > True
```

##### `find`

The `find` method is used to find the index of a substring. The following example shows how to use the `find` method:

```python
print('Hello World!'.find('World'))
# > 6
```

##### `removeprefix`

The `removeprefix` method is used to remove a prefix from a string. The following example shows how to use the
`removeprefix` method:

```python
print('Hello World!'.removeprefix('Hello '))
# > World!
```

##### `removesuffix`

The `removesuffix` method is used to remove a suffix from a string. The following example shows how to use the
`removesuffix` method:

```python
print('Hello World!'.removesuffix(' World!'))
# > Hello
```

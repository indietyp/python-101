# Starting Out - The Fundamentals

The goal of this section is to introduce the fundamentals of Python. We will cover the following topics:

* [Program Structure](#program-structure)
* [Comments](#comments)
* [Variables](#variables)
* [Expressions](#expressions)
* [Operators](#operators)
* [Primitive Types](#primitive-types)
* [Functions and Methods](#methods-and-functions)
  * [Common Built-in Functions](#built-in-functions)
  * [Common Built-in Methods](#built-in-methods)

## Program Structure

A Python program is a sequence of statements. A statement is a line of code that performs some action. For example, the
following program prints the string "Hello, World!" to the console:

```python
print("Hello, World!")
```

Programs are executed from top to bottom. The first statement in a program is executed first, followed by the second
statement, and so on. In the above example, the `print` statement is the only statement in the program, so it is
executed first.

Python programs are whitespace sensitive, meaning that the indentation of a line of code is important. The indentation
of a like is the number of spaces at the beginning of the line. The number of spaces used for indentation must be the
same across all lines of code, we choose to use 4 spaces for indentation. This means that if we talk about an
indentation of 2, we mean 8 spaces.

Programs are structured using indentation. Indentation is the number of spaces at the beginning of a line.
Indentation is used during control flow statements, such as `if` statements and `for` loops. We will cover control flow
in a later section.

An example of indentation is shown below:

```python
if True:
    print("Hello, World!")
```

## Comments

Comments are lines of code that are ignored by the Python interpreter. Comments are used to explain what a line (or
multiple lines) of code does.
While other languages like `C` have a distinction between single line comments and multi line comments, Python only has
a single type of comment. Comments are created by starting a line with a `#` character. Everything after the `#`
character is ignored by the Python interpreter.

```python
# This is a comment
print("Hello, World!")  # This is also a comment
# print("This line is commented out") <- this will not be executed
```

Lines that are comments are usually grayed out in IDEs and text editors.

We will use comments throughout this course to explain what a line of code does or to explain the task at hand that you
need to solve in an exercise.

### Multi Line Comments

Python does not have a multi line comment syntax. However, there is a trick to create multi line comments. Multi line
comments are created by using a multi line string. A multi line string is a string that spans multiple lines. Multi line
strings are created by using three double quotes (`"""`) or three single quotes (`'''`). The following example shows how
to create a multi line string:

```python
"""
This is a multi line string.
This is the second line of the string.
This is the third line of the string.
"""
```

When putting a multi line string at the beginning of a file, it is interpreted as a multi line comment. These comments
are used throughout the exercises in this course to explain the task at hand.

These comments are often referred to as docstrings, because they are used to document a program or function as a whole,
instead of a single line of code.

> **Note:** Multi line comments are also valid in other places in a Python program, they are also used to create
> documentation for functions and classes. We will cover functions and classes in a later section.

~~~admonish info title="Trivia" collapsible=true

Multi line comments are not ignored by the Python interpreter, they are actually stored in memory. 
This means that they can be accessed at runtime.
This is used by the `help` function to display the documentation of a function or class.

To for example access the documentation of a function programmatically, you can use the `__doc__` attribute of the function.

```python
def my_function():
    """This is the documentation of my_function"""
    pass
    
print(my_function.__doc__)
# > This is the documentation of my_function 
```

~~~

## Variables

Variables are used to store values in memory. Variables are created by assigning a value to a name. The name of a
variable can be chosen freely, but it must follow the following rules:

* The name must start with a letter or an underscore (`_`)
* The name can only contain letters, numbers and underscores (`_`)
* The name cannot be a reserved keyword
* The name cannot contain spaces
* The name cannot start with a number
* The name is case sensitive

Additionally in this course, we will enforce the following rules:

* The name must be descriptive
* The name must be in `snake_case` (all lowercase, words separated by underscores)
* The name must be in English
* Constants must be in `UPPER_SNAKE_CASE` (all uppercase, words separated by underscores)
    * A constant is a variable that is not supposed to change during the execution of a program

Variables are created by assigning a value to a name using the assignment operator (`=`). The assignment operator is a
binary operator, meaning that it takes two operands. The left operand is the name of the variable, the right operand is
the value that is assigned to the variable.

The following example shows how to create a variable:

```python
my_variable = 42
print(my_variable)
# > 42
```

The above example creates a variable named `my_variable` and assigns the value `42` to it. The value of a variable can
be changed by assigning a new value to it.

```python
my_variable = 42
print(my_variable)
# > 42

my_variable = 43
print(my_variable)
# > 43
```

Variables can be used in expressions. The value of the variable is used in the expression. The following example shows a
variable being used in an expression:

```python
my_variable = 42
print(my_variable + 1)
# > 43
```

## Expressions

Expressions are combinations of values, variables and operators. Expressions are evaluated by the Python interpreter. An
expression can be a single value, a variable or a combination of values, variables and operators.

The following example shows a single value being used as an expression:

```python
print(42)
# > 42
```

The following example shows a variable being used as an expression:

```python
my_variable = 42
print(my_variable)
# > 42
```

The following example shows a combination of values, variables and operators being used as an expression:

```python
print(42 + 1)
# > 43
```

## Operators

Operators are used to perform operations on values and variables. Operators are used in expressions, they are used to
combine values, variables and other operators. Operators can be used to perform arithmetic operations, comparison and to
combine values.

There are different types of operators that are supported by Python, these include:

* Arithmetic operators
    * Addition (`+`)
    * Subtraction (`-`)
    * Multiplication (`*`)
    * Division (`/`)
    * Floor division (`//`)
    * Modulo (`%`)
    * Exponentiation (`**`)
    * Negation (`-`)
* Comparison operators
    * Equal to (`==`)
    * Not equal to (`!=`)
    * Greater than (`>`)
    * Greater than or equal to (`>=`)
    * Less than (`<`)
    * Less than or equal to (`<=`)
* Logical operators
    * Logical AND (`and`)
    * Logical OR (`or`)
    * Logical NOT (`not`)
* Assignment operators
    * Assignment (`=`)
    * Expression and assignment (`+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `<<=`, `>>=`)
    * Walrus operator (`:=`)
* Identity operators
    * Identity (`is`)
    * Not identity (`is not`)
* Membership operators
    * Membership (`in`)
    * Not membership (`not in`)
* Bitwise operators (we will not cover these in this course, they only here for completeness)
    * Bitwise AND (`&`)
    * Bitwise OR (`|`)
    * Bitwise XOR (`^`)
    * Bitwise NOT (`~`)
    * Bitwise left shift (`<<`)
    * Bitwise right shift (`>>`)

### Arithmetic operators

Arithmetic operators are used to perform arithmetic operations on values and variables, they obey the rules of
mathematics, this means that `/` binds stronger than `+`. Meaning that `3 + 4 / 2` is evaluated as `3 + (4 / 2)`.

The following example shows how to use arithmetic operators:

```python
print(3 + 4 * 5)
# > 23
```

### Comparison operators

Comparison operators are used to compare values and variables. They return a boolean value (`True` or `False`).

The following example shows how to use comparison operators:

```python
print(3 > 4)
# > False
```

### Logical operators

Logical operators are used to combine boolean values. They return a boolean value (`True` or `False`). Logical operators
are used to combine boolean values, they are used to check if multiple conditions are met.

The following example shows how to use logical operators:

```python
print(True and False)
# > False
```

~~~admonish note title="Trivia" collapsible=true

Unlike other languages, Python accepts any value as a boolean value, before comparing values, Python will convert the values to boolean values.

To check which value would be evaluated to `True` and which value would be evaluated to `False`, you can use the `bool()` function.

Example of common values that are evaluated to `False`:

```python
print(bool(0))
# > False
print(bool(0.0))
# > False
print(bool(''))
# > False
print(bool([]))
# > False
print(bool({}))
# > False
print(bool(None))
# > False
```

Example of common values that are evaluated to `True`:

```python
print(bool(1))
# > True
print(bool(0.1))
# > True
print(bool(' '))
# > True
print(bool([1]))
# > True
print(bool({1: 1}))
# > True
```

~~~

#### Truth tables

Logical operators can be represented using truth tables. Truth tables are used to show the result of a logical operator
when combining two boolean values.

The following truth table shows the result of the logical AND operator (`and`):

| `A`     | `B`     | `A and B` |
|---------|---------|-----------|
| `False` | `False` | `False`   |
| `False` | `True`  | `False`   |
| `True`  | `False` | `False`   |
| `True`  | `True`  | `True`    |

The following truth table shows the result of the logical OR operator (`or`):

| `A`     | `B`     | `A or B` |
|---------|---------|----------|
| `False` | `False` | `False`  |
| `False` | `True`  | `True`   |
| `True`  | `False` | `True`   |
| `True`  | `True`  | `True`   |

The following truth table shows the result of the logical NOT operator (`not`):

| `A`     | `not A` |
|---------|---------|
| `False` | `True`  |
| `True`  | `False` |

### Assignment operators

Assignment operators are used to assign values to variables. Assignment operators are used to assign values to variables
in expressions.

There are different types of assignment operators, these include:

* Simple assignment (`=`)
* Expression and assignment (`+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `<<=`, `>>=`)
* Walrus operator (`:=`)

The simple assignment operator (`=`) is used to assign a value to a variable. The following example shows how to use the
simple assignment operator:

```python
my_variable = 42
print(my_variable)
# > 42
```

The expression and assignment operators are used to combine an expression and an assignment. The following example shows
how to use the expression and assignment operators:

```python
my_variable = 42
my_variable += 1
print(my_variable)
# > 43

# equivalent to:
my_variable = 42
my_variable = my_variable + 1
print(my_variable)
# > 43
```

The `variable X= expression` assignment is equivalent to `variable = variable X expression`, where `X`
is one of the following operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`, `&`, `|`, `^`, `<<`, `>>`.

The walrus operator (`:=`) is used to assign a value to a variable and return the value. It is only used in advanced
circumstances, but can be used to propagate a value in a chain of function calls.

The following example shows how to use the walrus operator:

```python
y = (x := 42)
print(x)
# > 42
print(y)
# > 42
```

### Identity operators

Identity operators are used to compare the identity of two objects, we won't cover what identity means in this course,
but you can read more about it [here](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types).

For now it is enough to know that if we want to check if a value is `None`, we can use the identity operator `is`.

~~~admonish note title="Trivia" collapsible=true

You can use the function `id()` to get the identity of an object, if two objects have the same identity, 
they are the same object, and `is` will return `True`.

~~~

### Membership operators

Membership operators are used to check if a value is a member of a collection. We will cover collections in the data
structures part of this course.

For now it is enough to know that if we want to check if a value is in a list, we can use the membership operator `in`.
We can also check if a substring is in a string.

The following example shows how to use the membership operator:

```python
print(1 in [1, 2, 3])
# > True
print('a' in 'abc')
# > True
```

## Primitive Types

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

### Numeric types

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

### Strings

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

### Booleans

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

### `None`

`None` expresses the absence of a value. This value is usually returned by functions that either don't return anything,
or only return something under certain conditions.

The following example shows how to use `None`:

```python
print(None)
# > None
```

## Methods and Functions

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

### Built-in Functions

Python comes with a lot of built-in functions and methods with can be used to perform a wide variety of tasks. These
include:

You can find a full list of built-in functions [here](https://docs.python.org/3/library/functions.html).

#### `print`

The `print` function is used to print a value to the console. The following example shows how to use the `print`
function:

```python
print('Hello World!')
# > Hello World!
```

#### `input`

The `input` function is used to get input from the user. The following example shows how to use the `input` function:

```python
name = input('Enter your name: ')
print(f'Hello {name}!')
# > Enter your name: John
# > Hello John!
```

#### `type`

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

#### `int`, `float`, `str`, `bool`

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

#### `len`

The `len` function is used to get the length of a value. The following example shows how to use the `len` function:

```python
print(len('Hello World!'))
# > 12
```

#### `open`

The `open` function is used to open a file. The following example shows how to use the `open` function:

```python
file = open('file.txt', 'r')
print(file.read())
# > Hello World!
file.close()
```

#### `help`

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

#### `eval`

The `eval` function is used to evaluate a string as a Python expression. The following example shows how to use
the `eval` function:

```python
print(eval('1 + 1'))
# > 2
```

> **Note:** The `eval` function is dangerous, and should not be used unless you know what you are doing.

#### Built-in Methods

##### `str`

The `str` has a multitude of methods, some of which are shown below. You can find a full list of methods on
the [Python documentation](https://docs.python.org/3/library/stdtypes.html#string-methods).

###### `lower`

The `lower` method is used to convert a string to lowercase. The following example shows how to use the `lower` method:

```python
print('Hello World!'.lower())
# > hello world!
```

###### `upper`

The `upper` method is used to convert a string to uppercase. The following example shows how to use the `upper` method:

```python
print('Hello World!'.upper())
# > HELLO WORLD!
```

###### `title`

The `title` method is used to convert a string to title case. The following example shows how to use the `title` method:

```python
print('hello world!'.title())
# > Hello World!
```

###### `capitalize`

The `capitalize` method is used to capitalize the first letter of a string. The following example shows how to use the
`capitalize` method:

```python
print('hello world!'.capitalize())
# > Hello world!
```

###### `strip`

The `strip` method is used to remove whitespace from the beginning and end of a string. The following example shows how
to use the `strip` method:

```python
print('   Hello World!   '.strip())
# > Hello World!
```

###### `lstrip`

The `lstrip` method is used to remove whitespace from the beginning of a string. The following example shows how to use
the `lstrip` method:

```python
print('   Hello World!   '.lstrip())
# > Hello World!   
```

###### `rstrip`

The `rstrip` method is used to remove whitespace from the end of a string. The following example shows how to use the
`rstrip` method:

```python
print('   Hello World!   '.rstrip())
# >    Hello World!
```

###### `replace`

The `replace` method is used to replace a substring with another substring. The following example shows how to use the
`replace` method:

```python
print('Hello World!'.replace('World', 'Universe'))
# > Hello Universe!
```

###### `split`

The `split` method is used to split a string into a list of substrings. The following example shows how to use the
`split` method:

```python
print('Hello World!'.split())
# > ['Hello', 'World!']
```

###### `join`

The `join` method is used to join a list of substrings into a string. The following example shows how to use the
`join` method:

```python
print(' '.join(['Hello', 'World!']))
# > Hello World!
```

###### `startswith`

The `startswith` method is used to check if a string starts with a substring. The following example shows how to use the
`startswith` method:

```python
print('Hello World!'.startswith('Hello'))
# > True
```

###### `endswith`

The `endswith` method is used to check if a string ends with a substring. The following example shows how to use the
`endswith` method:

```python
print('Hello World!'.endswith('World!'))
# > True
```

###### `find`

The `find` method is used to find the index of a substring. The following example shows how to use the `find` method:

```python
print('Hello World!'.find('World'))
# > 6
```

###### `removeprefix`

The `removeprefix` method is used to remove a prefix from a string. The following example shows how to use the
`removeprefix` method:

```python
print('Hello World!'.removeprefix('Hello '))
# > World!
```

###### `removesuffix`

The `removesuffix` method is used to remove a suffix from a string. The following example shows how to use the
`removesuffix` method:

```python
print('Hello World!'.removesuffix(' World!'))
# > Hello
```

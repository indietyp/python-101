# Comments

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

## Multi Line Comments

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

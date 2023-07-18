# Functions and Classes

In this section we will learn about what functions and classes are, how to use them, and how to write our own.

## Functions

Functions are a way to group code together and give it a name. This allows us to reuse code without having to rewrite it
every time. Functions are defined using the `def` keyword.

```python
def my_function():
    print("Hello, world!")
```

We can then call the function using its name and parentheses.

```python
my_function()
# > Hello, world!
```

Functions can also take arguments. Arguments are values that are passed to the function when it is called. These values
can
then be used inside the function.

```python
def my_function(name):
    print("Hello, " + name + "!")
```

Arguments can also have default values. If an argument has a default value, it is optional when calling the function.

```python
def my_function(name="world"):
    print("Hello, " + name + "!")
```

> **Note:** Arguments with default values must come after arguments without default values.

> **Note:** Be aware that default values are evaluated when the function is defined, not when it is called. This means
> that mutable default values can cause unexpected behavior.

Functions can also return values using the `return` keyword. This allows us to use the result of a function in other
code.

```python
def add(a, b):
    return a + b


result = add(1, 2)

print(result)
# > 3
```

> **Note:** If a function does not explicitly return a value, it implicitly returns `None`.

Once execution reaches a `return` statement, the function immediately exits. This means that any code after a `return`
statement will not be executed.

```python
def my_function():
    print("Hello, world!")
    return
    print("This will not be printed.")
```

When we call a function, we will "jump" to the function definition, execute the code inside, and then "jump" back to
where we called the function.

```python
def my_function():
    print("Hello, world!")


print("Before function call.")
my_function()
print("After function call.")

# > Before function call.
# > Hello, world!
# > After function call.
```

We can call other functions from inside a function.

```python
def my_function():
    print("Hello, world!")
    other_function()


def other_function():
    print("This is another function.")


my_function()

# > Hello, world!
# > This is another function.
```

### Function Arguments

Functions can take any number of arguments. When calling a function, we must pass the same number of arguments as there
are parameters in the function definition.

```python
def my_function(a, b, c):
    print(a, b, c)
```

Python differentiates between two types of arguments: positional arguments and keyword arguments. Positional arguments
are arguments that are passed by position. Keyword arguments are arguments that are passed by name.

```python
my_function(1, 2, 3)
# > 1 2 3

my_function(a=1, b=2, c=3)
# > 1 2 3

my_function(1, b=2, c=3)
# > 1 2 3
```

To allow for an arbitrary number of arguments, we can use the `*` operator. This will collect all positional arguments
into a tuple.

```python
def my_function(*args):
    print(args)


my_function(1, 2, 3)
# > (1, 2, 3)
```

Any argument that follows a `*` argument will be a keyword argument, and any argument that is before a `*` argument will
be a positional argument.

```python
def my_function(*args, a):
    print(args)
    print(a)


my_function(1, 2, 3, a=4)
# > (1, 2, 3)
# > 4
```

We can also use the `**` operator to collect keyword arguments into a dictionary.

```python
def my_function(**kwargs):
    print(kwargs)
```

The `**` operator must come after any `*` arguments, and must be the last argument in the function definition.

```python
def my_function(*args, **kwargs):
    print(args)
    print(kwargs)
```

Without allowing for an arbitrary number of arguments, we can still force the caller to use keyword arguments by using
`*` in the function definition.

```python
def my_function(*, a, b):
    print(a, b)


my_function(a=1, b=2)
# > 1 2

my_function(1, 2)
# > TypeError: my_function() takes 0 positional arguments but 2 were given
```

To force the caller to only use position arguments we can use `/` in the function definition.

```python
def my_function(a, b, /):
    print(a, b)


my_function(1, 2)
# > 1 2

my_function(a=1, b=2)
# > TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'a, b'
```

We can freely combine `*`, `/`, and `**` in the function definition.

```python
# a, b are positional-only
# c, d are positional-or-keyword
# e, f are keyword-only
# kwargs is a catch-all for any other keyword arguments
def my_function(a, b, /, c, d, *, e, f, **kwargs):
    print(a, b, c, d, e, f)
    print(kwargs)


my_function(1, 2, 3, 4, e=5, f=6)
# > 1 2 3 4 5 6
# > {}

my_function(1, 2, c=3, d=4, e=5, f=6)
# > 1 2 3 4 5 6
# > {}

my_function(1, 2, 3, d=4, e=5, f=6)
# > 1 2 3 4 5 6
# > {}

my_function(1, 2, 3, 4, 5, 6)
# > TypeError: my_function() takes 4 positional arguments but 6 were given
```

We **cannot** use `*args` and `*` in the same function definition.

```python
def my_function(*args, *):
    pass

# > SyntaxError: invalid syntax
```

### Default Arguments

We can give arguments default values. If an argument has a default value, it is optional when calling the function.

```python
def my_function(a, b, c=3):
    print(a, b, c)


my_function(1, 2)
# > 1 2 3

my_function(1, 2, 4)
# > 1 2 4
```

This also works with the `*`, `/`, and `**` operators.

```python
def my_function(a, b, /, c, d=4, *, e, f=6, **kwargs):
    print(a, b, c, d, e, f)
    print(kwargs)


my_function(1, 2, 3, e=5)
# > 1 2 3 4 5 6

my_function(1, 2, 3, 4, e=7, f=8)
# > 1 2 3 4 7 8
```

A positional argument can only have a default value if all arguments after it also have default values.

> **Note:** This applies to positional-only and positional-or-keyword arguments.

```python
def my_function(a, b=1, c):
    pass

# > SyntaxError: non-default argument follows default argument
```

Any value can be used as a default value, including other variables, but be aware that the default value must be
available and defined when the function is defined.

```python
e = 4


def my_function(a, b, c=3, d=e):
    print(a, b, c, d)


my_function(1, 2)
# > 1 2 3 3

my_function(1, 2, 4)
# > 1 2 4 4
```

The default value is evaluated when the function is defined, not when it is called.

```python
e = 4


def my_function(a, b, c=3, d=e):
    print(a, b, c, d)


e = 5

my_function(1, 2)
# > 1 2 3 4
```

Mutable default values can cause problems, as the default value is evaluated when the function is defined, not when it
is called.

```python
def my_function(a, b, c=[]):
    c.append(a)
    c.append(b)
    print(c)


my_function(1, 2)
# > [1, 2]

my_function(3, 4)
# > [1, 2, 3, 4]
```

### Function Scope

Variables defined inside a function are not available outside of the function.

```python
def my_function():
    a = 1


my_function()
print(a)

# > NameError: name 'a' is not defined
```

Variables defined outside of a function are available inside the function.

```python
a = 1


def my_function():
    print(a)


my_function()
# > 1
```

Variables defined inside a function are not available outside of the function, even if they are defined before the call
to the function.

```python

def my_function():
    print(a)
    a = 1


my_function()
# > UnboundLocalError: local variable 'a' referenced before assignment
```

To manipulate a global variable inside a function, we must use the `global` keyword.

```python
a = 1


def my_function():
    global a
    a = 2


my_function()

print(a)
# > 2
```

> **Note:** It is generally considered bad practice to use global variables.

## Classes

Classes are a way to group data and functions together. Classes are defined using the `class` keyword.

```python
class MyClass:
    pass
```

### Class Attributes

Attributes are variables that belong to a class. They are defined inside the class, but outside of any methods.

```python
class MyClass:
    a = 1
    b = 2

    def my_method(self):
        pass

    def my_other_method(self):
        pass
```

Class attributes are shared between all instances of the class.

```python
class MyClass:
    a = 1
    b = 2

    def my_method(self):
        pass

    def my_other_method(self):
        pass
    
    
my_class_1 = MyClass()
my_class_2 = MyClass()

print(my_class_1.a)
# > 1

print(my_class_2.a)
# > 1

MyClass.a = 3

print(my_class_1.a)
# > 3

print(my_class_2.a)
# > 3
```

### Class Methods

Methods are functions that belong to a class. They are defined inside the class, and are called using the `.` operator.

```python
class MyClass:
    a = 1
    b = 2

    def my_method(self):
        pass

    def my_other_method(self):
        pass


my_class = MyClass()
my_class.my_method()
my_class.my_other_method()
```

They always take `self` as the first argument. `self` is a reference to the instance of the class that the method is
called on.

```python
class MyClass:
    a = 1
    b = 2

    def my_method(self):
        print(self.a)
        print(self.b)

    def my_other_method(self):
        pass


my_class = MyClass()
my_class.my_method()
# > 1
# > 2
```

### Class Constructors

Classes can have a special method called `__init__` that is called when an instance of the class is created. This is
called the constructor.

```python
class MyClass:
    def __init__(self):
        print("Hello World")


my_class = MyClass()
# > Hello World
```

Like a normal method, the constructor takes `self` as the first argument, and can take other arguments.

```python
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


my_class = MyClass(1, 2)
print(my_class.a)

# > 1
```

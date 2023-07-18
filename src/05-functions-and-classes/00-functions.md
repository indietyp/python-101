# Functions

Functions are a way to organize code. They allow us to group related code together and reuse it throughout our program.

When calling a function, we are telling the program to execute the code inside the function, then return to where we
were with the result of the function.

## Defining Functions

Functions are defined using the `def` keyword.

```python
def my_function():
    pass
```

## Calling Functions

Functions are called using the function name followed by parentheses.

```python
def my_function():
    pass


my_function()
```

## Function Arguments

Functions can take arguments. Arguments are variables that are passed to the function when it is called.

```python
def my_function(name):
    print("Hello, " + name + "!")


my_function("world")
# > Hello, world!
```

```admonish info title="Trivia" collapsible=true

In programming we differentiate between arguments and parameters.
Parameters are the variables defined in the function definition.
Arguments are the values passed to the function when it is called. 
In the example above, `name` is a parameter and `"world"` is an argument.

```

## Positional and Keyword Arguments

Arguments can be passed by position or by name. Positional arguments are arguments that are passed by position. Keyword
arguments are arguments that are passed by name.

```python
def my_function(a, b, c):
    print(a, b, c)


my_function(1, 2, 3)
# > 1 2 3

my_function(a=1, b=2, c=3)
# > 1 2 3

my_function(1, b=2, c=3)
# > 1 2 3
```

Keyword arguments can not be passed before positional arguments.

```python
def my_function(a, b, c):
    print(a, b, c)


my_function(a=1, 2, 3)
# > SyntaxError: positional argument follows keyword argument
```

Keyword arguments can be passed in any order.

```python
def my_function(a, b, c):
    print(a, b, c)


my_function(c=3, a=1, b=2)
# > 1 2 3
```

Any parameter that is before a `/` will be a positional-only argument. Any parameter that is after a `/` will
keyword-or-positional parameters. Any parameter that is after a `*` will be a keyword-only argument.

```python
def my_function(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


my_function(1, 2, 3, 4, e=5, f=6)
# > 1 2 3 4 5 6

my_function(1, 2, c=3, d=4, e=5, f=6)
# > 1 2 3 4 5 6

my_function(1, 2, 3, 4, 5, 6)
# > TypeError: my_function() takes 4 positional arguments but 6 were given

my_function(a=1, b=2, c=3, d=4, e=5, f=6)
# > TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'a, b'
```

> **Note:** Usually keyword-or-positional parameters and positional-only parameters cannot be followed after a parameter
> with a default value.
> However, if the parameter is keyword-only, then this is allowed.

```python
def my_function(a, b, /, c=3, d=4, *, e, f):
    print(a, b, c, d, e, f)


my_function(1, 2, e=5, f=6)
# > 1 2 3 4 5 6
```

## Default Arguments

Parameters can have default values. If a parameter has a default value, then it is optional when calling the function.

```python
def my_function(name="world"):
    print("Hello, " + name + "!")


my_function()
# > Hello, world!

my_function("Python")
# > Hello, Python!
```

Positional-only parameters and keyword-or-positional parameters cannot follow parameters with default values.

```python
def my_function(a, b=2, /, c, d=4, *, e, f):
    print(a, b, c, d, e, f)

# > SyntaxError: non-default argument follows default argument
```

Default values are evaluated when the function is defined, not when the function is called. You should always use
immutable values as default values.

```python
def my_function(a, b=[]):
    b.append(a)
    print(b)


my_function(1)
# > [1]

my_function(2)
# > [1, 2]

my_function(3)
# > [1, 2, 3]
```

Any expression is allowed as a default value (this also means that variables can be used as default values, but remember
that the expression is evaluated when the function is defined, not when the function is called).

```python
def my_function(a, b=2 + 2):
    print(a, b)


my_function(1)
# > 1 4

c = 3


def my_function(a, b=c):
    print(a, b)


my_function(1)
# > 1 3

c = 4

my_function(1)
# > 1 3
```

## Return Values

Functions can return values using the `return` keyword.

```python
def my_function():
    return 1


print(my_function())
# > 1
```

Functions can return multiple values by separating them with commas.

```python
def my_function():
    return 1, 2, 3


a, b, c = my_function()

print(a, b, c)
# > 1 2 3
```

> **Note:** If a function does not return a value, then it returns `None`.

## Arbitrary Arguments

Functions can take an arbitrary number of arguments using the `*` operator, any positional argument when calling a
function will be collected into the variable that follows the `*` operator.

```python
def my_function(*args):
    print(args)


my_function(1, 2, 3)
# > (1, 2, 3)
```

To collect keyword arguments, use the `**` operator.

```python
def my_function(**kwargs):
    print(kwargs)


my_function(a=1, b=2, c=3)
# > {'a': 1, 'b': 2, 'c': 3}
```

## Scope

Variables defined inside a function are local to that function. Variables defined outside a function are global.
Variables defined outside a function can be accessed inside a function, but variables defined inside a function cannot
be accessed outside that function.

```python
def my_function():
    a = 1
    print(a)


my_function()


# > 1


def my_function():
    print(a)


a = 1

my_function()


# > 1


def my_function():
    b = 1


my_function()
print(b)
# > NameError: name 'b' is not defined
```

By default, variables from outer scope can only be manipulated or read, but not redefined, you can use the `global`
and `nonlocal` keywords to change this behavior.

```python
a = 0


def my_function():
    global a
    a = 1


print(a)
# > 0

my_function()
print(a)
# > 1
```

```python
def my_function():
    a = 1

    def my_inner_function():
        nonlocal a
        a = 2

    my_inner_function()
    print(a)


my_function()
# > 2
```

> **Note:** It is generally considered bad practice to use global variables.

## Recursion

Functions are able to call themselves, this is called recursion.

```python
def my_function(n):
    if n == 0:
        return 0
    return n + my_function(n - 1)


print(my_function(10))
# > 55
```

Functions are also able to call any other function.

```python
def my_function(n):
    return n + 1


def my_other_function(n):
    return my_function(n) + 1


print(my_other_function(10))
# > 12
```

# Conditionals

Conditionals are used to control the flow of a program. They allow us to execute certain blocks of code only if certain
conditions are met. In Python a conditional is created using the `if` statement. The `if` statement is followed by an
expression which is evaluated to a boolean value. If the expression evaluates to `True` then the code block following
the `if` statement is executed. If the expression evaluates to `False` then the code block is skipped.

It is important to note that the code block following the `if` statement is indented. This is how Python knows which
block of code is associated with the `if` statement. The code block is indented by 4 spaces by convention and ends when
the indentation returns to the previous level.

```python
if True:
    print("This code block will be executed")
    # > This code block will be executed

    print("This code block will also be executed")
    # > This code block will also be executed

print("This code block will be executed as well")
# > This code block will be executed as well

if False:
    print("This code block will not be executed")

print("This code block will be executed as well")
# > This code block will be executed as well

if 1 == 1:
    print("This code block will be executed")
    # > This code block will be executed

if 1 == 2:
    print("This code block will not be executed")
```

The `if` statement can be followed by an `else` statement. The `else` statement is followed by a code block that will be
executed if the expression in the `if` statement evaluates to `False`.

```python
if True:
    print("This code block will be executed")
    # > This code block will be executed
else:
    print("This code block will not be executed")

if False:
    print("This code block will not be executed")
else:
    print("This code block will be executed")
    # > This code block will be executed
```

The `if` statement can also be followed by an `elif` statement. The `elif` statement is followed by an expression that
will be evaluated if the expression in the `if` statement evaluates to `False`. If the expression in the `elif`
statement evaluates to `True` then the code block following the `elif` statement will be executed. If the expression in
the `elif` statement evaluates to `False` then the code block following the `elif` statement will be skipped.

```python
if False:
    print("This code block will not be executed")
elif True:
    print("This code block will be executed")
    # > This code block will be executed
else:
    print("This code block will not be executed")

if False:
    print("This code block will not be executed")
elif False:
    print("This code block will not be executed")
else:
    print("This code block will be executed")
    # > This code block will be executed
```

The `if` statement can be followed by any number of `elif` statements, but an `else` statement cannot
be followed by an `elif` statement. The `else` statement must be the last statement in the conditional.

```python
if False:
    print("This code block will not be executed")
elif False:
    print("This code block will not be executed")
elif False:
    print("This code block will not be executed")
else:
    print("This code block will be executed")
    # > This code block will be executed
```

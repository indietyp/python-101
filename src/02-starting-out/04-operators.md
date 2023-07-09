# Operators

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

## Arithmetic operators

Arithmetic operators are used to perform arithmetic operations on values and variables, they obey the rules of
mathematics, this means that `/` binds stronger than `+`. Meaning that `3 + 4 / 2` is evaluated as `3 + (4 / 2)`.

The following example shows how to use arithmetic operators:

```python
print(3 + 4 * 5)
# > 23
```

## Comparison operators

Comparison operators are used to compare values and variables. They return a boolean value (`True` or `False`).

The following example shows how to use comparison operators:

```python
print(3 > 4)
# > False
```

## Logical operators

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

### Truth tables

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

## Assignment operators

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

## Identity operators

Identity operators are used to compare the identity of two objects, we won't cover what identity means in this course,
but you can read more about it [here](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types).

For now it is enough to know that if we want to check if a value is `None`, we can use the identity operator `is`.

~~~admonish note title="Trivia" collapsible=true

You can use the function `id()` to get the identity of an object, if two objects have the same identity, 
they are the same object, and `is` will return `True`.

~~~

## Membership operators

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

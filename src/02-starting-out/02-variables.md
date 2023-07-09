# Variables

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

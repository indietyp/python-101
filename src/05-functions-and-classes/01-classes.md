# Classes

Classes are a way to group data and functions together. Classes are defined using the `class` keyword.

```python
class MyClass:
    pass
```

## Class Attributes

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

## Class Methods

Methods are functions that belong to a class. They are defined inside the class, and are called on instances of the
class using the `.` operator.

```python

class MyClass:
    a = 1
    b = 2

    def my_method(self):
        print('my_method')

    def my_other_method(self):
        print('my_other_method')


my_class = MyClass()
my_class.my_method()
# > my_method

my_class.my_other_method()
# > my_other_method
```

Methods can access the instance of the class they are called on using the `self` parameter.

```python

class MyClass:
    a = 1
    b = 2

    def my_method(self):
        print(self.a)

    def my_other_method(self):
        print(self.b)


my_class = MyClass()
my_class.my_method()
# > 1

my_class.my_other_method()
# > 2
```

## The `__init__` Method

The `__init__` method is a special method that is called when an instance of a class is created. It is used to set up
the initial state of the instance.

```python

class MyClass:
    def __init__(self):
        print('MyClass.__init__')


my_class = MyClass()
# > MyClass.__init__
```

`__init__.py` is a normal method, meaning it can take parameters.

```python

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


my_class = MyClass(1, 2)

print(my_class.a)
# > 1

print(my_class.b)
# > 2
```

## Instance Attributes

Instance attributes are variables that belong to an instance of a class. They are defined on any instance using the `.`
operator.

```python

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


a = MyClass(1, 2)
b = MyClass(3, 4)

print(a.a)
# > 1

print(a.b)
# > 2

print(b.a)
# > 3

print(b.b)
# > 4

a.a = 5

print(a.a)
# > 5

print(b.a)
# > 3

a.c = 6

print(a.c)
# > 6

print(b.c)
# > AttributeError: 'MyClass' object has no attribute 'c'
```


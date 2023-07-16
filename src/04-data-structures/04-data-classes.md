# Dataclasses

Dataclasses are a way to create classes that are mainly used to store data. They are similar to namedtuples, but they
are mutable and have more features. They are created using the `dataclass` decorator.

```python
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    height: float


p = Person('John', 30, 1.80)

print(p)
# > Person(name='John', age=30, height=1.8)
```

## Default Values

Default values can be set for dataclass fields by using the `default` keyword argument.

```python
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int = 0
    height: float = 0.0


p = Person(name='John')

print(p)
# > Person(name='John', age=0, height=0.0)
```

## Default Factory

Default values can also be set using a factory function. The factory function is called with no arguments when the field
is not set.

```python
from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    age: int = 0
    height: float = 0.0
    friends: list[str] = field(default_factory=list)


p = Person(name='John')

print(p)
# > Person(name='John', age=0, height=0.0, friends=[])
```

> **Note:** For mutable default values, it is recommended to use the `default_factory` argument instead of the `default`
> argument, as otherwise the same mutable object will be used for all instances of the class.

## Type Hints

Type hints can be added to dataclass fields. They are not enforced, but can be used by external tools.

```python
from dataclasses import dataclass


@dataclass
class Person:
    name: str  # The name must be a string
    age: int = 0  # The age must be an integer
    height: float = 0.0  # The height must be a float


p = Person(name='John', age=30, height=1.80)

print(p)
# > Person(name='John', age=30, height=1.8)
```

## Frozen

Dataclasses can be made immutable by setting the `frozen` keyword argument to `True`. This will make the class hashable.

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    name: str
    age: int = 0
    height: float = 0.0


p = Person(name='John', age=30, height=1.80)

print(p)
# > Person(name='John', age=30, height=1.8)

p.age = 31
# > AttributeError: can't set attribute
```

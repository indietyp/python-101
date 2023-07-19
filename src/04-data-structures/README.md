# Data Structures

In the previous chapters we have talked about primitive data types, such as `int`, `float`, `bool`, `str`, and `None`.
These are the basic building blocks of any program, but they are not enough to solve most real-world problems. In this
chapter we will introduce more complex data types, which are called **data structures**.

We will cover the following data structures:

* [Lists](00-lists.md)
* [Tuples](01-tuples.md)
* [Sets](02-sets.md)
* [Dictionaries](03-dictionaries.md)
* [Dataclasses](04-data-classes.md)
* [Enumerations](05-enums.md)

## Guidance

If you don't know which type of collection to use, here is a simple decision diagram:

```mermaid
flowchart TD
    A[I want to save a list of things]

    A --> B{{ Do my values have a unique key<br/> and associated value? }}
    B -->|No| D{{Do I mainly check if a value is the collection?}}

    D -->|Yes| E{{Are all values unique?}}
    D -->|No| I

    E -->|Yes| G{{Do I only insert values once<br/>and then check against those?}}
    G -->|Yes| H[use <code>frozenset</code>]
    G -->|No| F[use <code>set</code>]

    E -->|No| I{{Do I only insert values once?}}
    I -->|No| C[use <code>list</code>]

    I -->|Yes| J[use <code>tuple</code>]
    B -->|Yes| L[use <code>dict</code>]
```

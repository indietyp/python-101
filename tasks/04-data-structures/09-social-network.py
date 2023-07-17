"""
Create a program that will help you manage your social network. The program should be able
to handle the following commands:

- `create` - create a new user in your social network
- `add` - adds a connection between two users in your social network
- `remove` - remove a connection between two users in your social network
- `print` - prints your social network
- `clear` - clears your social network
- `done` - exits the application

The application should also handle invalid commands by printing out an error message.

Extra:
    - Allow the user to directly add a friend via `add <from> <to>`.
    - Allow the user to remove a friend via `remove <from> <to>`.
    - Allow to add and remove via name or index.
    - If a user does not exist when adding a friend, create the user.
    - Add a command `mutual` that will print out all the mutual friends between two people.
    - Add a command `friends` that will print out all the friends of a person.
    - Add a command `has-connection-between <from> <to>` that will print out whether there
        is a connection between two people. Hint: use DFS, BFS or Dijkstra's algorithm.
    - Allow the user to input multiple friends at once, separated by commas.

Example:
    Input: create
    Name: John
    Output: Index: 0
    Input: create
    Name: Jane
    Output: Index: 1
    Input: add
    From: 0
    To: 1
    Output: Connection added
    Input: print
    Output:
        [0] John -> Jane
        [1] Jane -> John
    Input: add
    From: John
    To: Jane
    Output: Connection added
    Input: print
    Output:
        [0] John -> Jane
        [1] Jane -> John
    Input: remove
    From: 0
    To: 1
    Output: Connection removed
    Input: print
    Output:
        [0] John
        [1] Jane
    Input: done
"""

# Write your code below this line 👇

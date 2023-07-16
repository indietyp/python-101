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
"""

# Write your code below this line 👇

users = []
social_network = {}

while True:
    command = input("Input: ")
    args: list[str] = command.split()

    match args:
        case ["done"]:
            break
        case ["create", *names]:
            users.extend(name for name in names if name not in users)
        case ["add", from_, to]:
            if not from_.isdigit():
                if from_ in users:
                    from_ = users.index(from_)
                else:
                    users.append(from_)
                    from_ = len(users) - 1

            if not to.isdigit():
                if to in users:
                    to = users.index(to)
                else:
                    users.append(to)
                    to = len(users) - 1

            social_network.setdefault(from_, set()).add(to)
            social_network.setdefault(to, set()).add(from_)
        case ["remove", from_, to]:
            if not from_.isdigit():
                if from_ not in users:
                    continue

                from_ = users.index(from_)

            if not to.isdigit():
                if to not in users:
                    continue

                to = users.index(to)

            social_network.setdefault(from_, set()).discard(to)
            social_network.setdefault(to, set()).discard(from_)

        case ["print"]:
            for user, friends in social_network.items():
                index = user
                user = users[user]
                print(
                    f"[{index}] {user} -> {', '.join(users[friend] for friend in friends)}")
        case ["clear"]:
            social_network.clear()
            users.clear()
        case ["mutual", from_, to]:
            if not from_.isdigit():
                if from_ not in users:
                    continue

                from_ = users.index(from_)

            if not to.isdigit():
                if to not in users:
                    continue

                to = users.index(to)

            mutual_friends = social_network.setdefault(from_,
                                                       set()) & social_network.setdefault(
                to, set())
            print(
                f"Mutual friends: {', '.join(users[friend] for friend in mutual_friends)}")
        case ["friends", user]:
            if not user.isdigit():
                if user not in users:
                    continue

                user = users.index(user)

            friends = social_network.setdefault(user, set())
            print(f"Friends: {', '.join(users[friend] for friend in friends)}")
        case ["has-connection-between", from_, to]:
            if not from_.isdigit():
                if from_ not in users:
                    continue

                from_ = users.index(from_)

            if not to.isdigit():
                if to not in users:
                    continue

                to = users.index(to)

            visited = set()
            queue = [from_]
            while queue:
                user = queue.pop(0)
                if user == to:
                    print("There is a connection between the two users.")
                    break
                visited.add(user)
                queue.extend(
                    friend for friend in social_network.setdefault(user, set()) if
                    friend not in visited)
            else:
                print("There is no connection between the two users.")
        case _:
            print("Invalid command.")

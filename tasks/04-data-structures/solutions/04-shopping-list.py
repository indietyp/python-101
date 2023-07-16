"""
Create an application that will help you with your shopping.

The application should be able to handle the following commands:
- `add` - adds an item to the shopping list
- `remove` - removes an item from the shopping list by its index
- `print` - prints the shopping list
- `clear` - clears the shopping list
- `done` - exits the application

The application should also handle invalid commands by printing out an error message.

Extra:
    - Allow the user to directly add an item via `add <item>`.
    - Allow the user to input multiple items at once, separated by commas.
    - Allow the user to remove an item by its name.
    - Allow the user to remove directly an item via `remove <item>`.
    - Allow the user to remove by index or name with the same command.
    - Allow the user to remove multiple items at once, separated by commas.
    - Allow the user to either input the command in lowercase or uppercase.

Example:
    Input: add
    Item: Milk
    Input: add
    Item: Eggs
    Input: add
    Item: Bread
    Input: print
    Output:
        [0] Milk
        [1] Eggs
        [2] Bread
    Input: remove
    Index: 1
    Input: print
    Output:
        [0] Milk
        [1] Bread
    Input: clear
    Input: print
    Output:
    Input: done
"""

# Write your code below this line 👇

shopping_list = []
while True:
    command = input("Input: ")
    args = command.split()

    match args:
        case ["done"]:
            break
        case ["add", *items]:
            shopping_list.extend(items)
        case ["remove", *items]:
            for item in items:
                if item.isdigit():
                    shopping_list.pop(int(item))
                else:
                    shopping_list.remove(item)
        case ["print"]:
            print("Output:")
            for index, item in enumerate(shopping_list):
                print(f"    [{index}] {item}")
        case ["clear"]:
            shopping_list.clear()
        case _:
            print("Unknown command")

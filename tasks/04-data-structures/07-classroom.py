"""
Write a program for a classroom. The program should be able to record the students' names
and their grades. Your program should be able to take the following commands:

* `add <name> <grade>` - add a student to the classroom
* `remove <name>` - remove a student from the classroom
* `print` - print the students and their grades
* `exit` - exit the program

Help: You can use `.split()` to split a string into a list of words.

Extra:
    - Add a command `average` which prints the average grade of the students.
    - Add a command `top` which prints the student with the highest grade.
    - Add a command `top <number>` which prints the top `<number>` students.
    - Add a command `bottom` which prints the student with the lowest grade.
    - Add a command `bottom <number>` which prints the bottom `<number>` students.
    - Add a command `save <filename>` which saves the students and their grades
        in a file.
    - Add a command `load <filename>` which loads the students and their grades
        from a file.

Example:
    Input: add John 5
    Input: add Jane 4
    Input: add Bob 3
    Input: print
    Output: John 5, Jane 4, Bob 3
    Input: remove Jane
    Input: print
    Output: John 5, Bob 3
    Input: exit
"""

# Write your code below this line 👇

classroom = {}

while True:
    command = input("Command: ")
    args = command.split()

    match args:
        case ["add", name, grade]:
            classroom[name] = int(grade)
        case ["remove", name]:
            del classroom[name]
        case ["print"]:
            print(classroom)
        case ["exit"]:
            break
        case ["average"]:
            print(sum(classroom.values()) / len(classroom))
        case ["top"]:
            print(max(classroom, key=classroom.get))
        case ["top", number]:
            number = int(number)
            print(sorted(classroom, key=classroom.get, reverse=True)[:number])
        case ["bottom"]:
            print(min(classroom, key=classroom.get))
        case ["bottom", number]:
            number = int(number)
            print(sorted(classroom, key=classroom.get)[:number])
        case ["save", filename]:
            with open(filename, "w") as file:
                for name, grade in classroom.items():
                    file.write(f"{name} {grade}\n")
        case ["load", filename]:
            with open(filename, "r") as file:
                for line in file:
                    name, grade = line.split()
                    classroom[name] = int(grade)
        case _:
            print("Unknown command")

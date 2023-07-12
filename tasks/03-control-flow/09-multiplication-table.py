"""
Take a number from the user and print a multiplication table up to that number.

Hint: You can use `print(a, end='')` to print a without a newline at the end, and `print()` to print a newline.

Extra Task: Print the table in a nice format, like this:

    Enter a number: 5
       1 | 2 | 3 | 4 | 5
    -+---+---+---+---+---
    1| 1 | 2 | 3 | 4 | 5
    2| 2 | 4 | 6 | 8 | 10
    3| 3 | 6 | 9 | 12| 15
    4| 4 | 8 | 12| 16| 20
    5| 5 | 10| 15| 20| 25

Example:
    Enter a number: 5
    1 x 1 = 1
    1 x 2 = 2
    1 x 3 = 3
    1 x 4 = 4
    1 x 5 = 5
    ...
"""

# Write your code below this line 👇

number = input('Enter a number: ')
number = int(number)

for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(f'{i} x {j} = {i * j}')

# Fancy version

number = input('Enter a number: ')
number = int(number)


class Table:
    n: int
    rows: list[list[int]]

    def __init__(self, n: int):
        self.n = n
        self.rows = [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]

    def column_width(self, column: int) -> int:
        return len(str(max(row[column] for row in self.rows)))

    def header_width(self) -> int:
        return len(str(self.n))

    def __str__(self) -> str:
        header_width = self.header_width()

        rows = []
        header_row = []
        # first construct the header
        for row_index in range(self.n + 1):
            if row_index == 0:
                header_row.append(' ' * header_width)
            else:
                header_row.append(str(row_index).rjust(self.column_width(row_index - 1)))

        rows.append(header_row)

        # then construct the rows
        for row_index in range(self.n):
            row = [str(row_index + 1).rjust(header_width)]

            for index, value in enumerate(self.rows[row_index]):
                row.append(str(value).rjust(self.column_width(index)))

            rows.append(row)

        # create the separator row
        separator_row = ['-' * len(column) for column in rows[0]]
        separator_row = '-+-'.join(separator_row)

        # now merge each individual row into a string
        rows = [' | '.join(row) for row in rows]

        # and finally join all the rows together
        return '\n'.join([rows[0], separator_row, *rows[1:]])


table = Table(number)
print(table)

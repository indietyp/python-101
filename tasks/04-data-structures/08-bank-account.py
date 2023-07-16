"""
Create a program to manage bank accounts.
The program should be able to handle the following commands:
* `create` - create a new bank account
* `deposit` - deposit money into a bank account
* `withdraw` - withdraw money from a bank account (There is no overdraft)
* `print` - prints all the bank accounts
* `clear` - clears all the bank accounts
* `done` - exits the application

The application should also handle invalid commands by printing out an error message.

Extra:
    - Allow the user to directly create a bank account via `create <name> <balance>`.
    - Allow the user to deposit money via `deposit <name> <amount>`.
    - Allow the user to withdraw money via `withdraw <name> <amount>`.
    - Allow the user to remove a bank account via `remove <name>`.
    - Allow the user to remove a bank account via `remove <index>`.
    - Allow the user to remove multiple bank accounts at once, separated by commas.
    - Allow the user to either input the command in lowercase or uppercase.
    - Withdrawal should have a fee of 0.5% of the amount withdrawn,
        and should have a confirmation prompt.
    - Write the bank accounts to a file via `save <filename>`.
    - Load the bank accounts from a file via `load <filename>`.
    - Add a command `transfer <from> <to> <amount>` that will transfer money from one
        account to another.
        (There is no overdraft, so the transfer should only happen if the `from`
        account has enough money)
    - Add a fee of 1% of the amount transferred to the `transfer` command.
    - Add a command `print <name>` that will print the bank account with the given name.
    - Add a command `print <index>` that will print the bank account with the given index.
    - Add a list of transactions to each bank account, and print them out when printing
        said account.

Example:
    Input: create
    Name: John
    Balance: 1000
    Input: create
    Name: Jane
    Balance: 2000
    Input: create
    Name: Bob
    Balance: 3000
    Input: print
    Output:
        [0] John (1000)
        [1] Jane (2000)
        [2] Bob (3000)
    Input: deposit
    Index: 0
    Amount: 500
    Input: deposit
    Name: Jane
    Amount: 1000
    Input: deposit
    Index: 2
    Amount: 1500
    Input: print
    Output:
        [0] John (1500)
        [1] Jane (3000)
        [2] Bob (4500)
    Input: withdraw
    Index: 0
    Amount: 3000
    Error: Not enough money
    Input: done
"""
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


# Write your code below this line 👇

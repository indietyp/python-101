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
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


# Write your code below this line 👇

class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TRANSFER = "transfer"


@dataclass(frozen=True)
class Transaction:
    at: datetime
    type_: TransactionType
    before: float
    after: float
    fee: float = 0

    target: int = None


@dataclass
class BankAccount:
    name: str
    balance: float = 0

    transactions: list[Transaction] = None


accounts: list[BankAccount] = []

while True:
    command = input("Input: ")
    args = command.split()

    match args:
        case ["done"]:
            break
        case ["create", name, balance]:
            accounts.append(BankAccount(name, float(balance)))
        case ["deposit", amount]:
            if amount.isdigit():
                account = accounts[int(amount)]
            else:
                account = next(account for account in accounts if account.name == amount)

            transaction = Transaction(at=datetime.now(), type_=TransactionType.DEPOSIT,
                                      before=account.balance,
                                      after=account.balance + amount)
            account.balance += amount
            account.transactions.append(transaction)
        case ["withdraw", amount]:
            if amount.isdigit():
                account = accounts[int(amount)]
            else:
                account = next(account for account in accounts if account.name == amount)

            transaction = Transaction(at=datetime.now(), type_=TransactionType.WITHDRAW,
                                      before=account.balance,
                                      after=account.balance - amount)
            if transaction.after < 0:
                print("Error: Not enough money")
                continue

            account.balance -= amount
            account.transactions.append(transaction)
        case ["print"]:
            for index, account in enumerate(accounts):
                print(f"[{index}] {account.name} ({account.balance})")
        case ["print", name]:
            if name.isdigit():
                account = accounts[int(name)]
            else:
                account = next(account for account in accounts if account.name == name)

            print(f"{account.name} ({account.balance})")
            for transaction in account.transactions:
                print(
                    f"{transaction.at} {transaction.type_.value} {transaction.before} {transaction.after}")
        case ["clear"]:
            accounts.clear()
        case ["save", filename]:
            with open(filename, "w") as file:
                for account in accounts:
                    transactions = [
                        f"{transaction.at.isoformat()} {transaction.type_.value} {transaction.before} {transaction.after}"
                        for transaction in account.transactions]

                    file.write(f"{account.name} {account.balance}\n")
                    file.write("\n    ".join(transactions))

        case ["load", filename]:
            with open(filename, "r") as file:
                account = None

                for line in file.readlines():
                    if line.startswith("    "):
                        transaction = Transaction(*line.split())
                        account.transactions.append(transaction)
                    else:
                        name, balance = line.split()
                        account = BankAccount(name, float(balance))
                        accounts.append(account)
        case ["transfer", from_, to, amount]:
            if from_.isdigit():
                from_account = accounts[int(from_)]
            else:
                from_account = next(
                    account for account in accounts if account.name == from_)

            if to.isdigit():
                to_account = accounts[int(to)]
                to = int(to)
            else:
                to, to_account = next(
                    (index, account) for index, account in enumerate(accounts) if
                    account.name == to)

            transaction = Transaction(at=datetime.now(), type_=TransactionType.TRANSFER,
                                      before=from_account.balance,
                                      after=from_account.balance - amount,
                                      target=to)
            if transaction.after < 0:
                print("Error: Not enough money")
                continue
            from_account.balance -= amount
            from_account.transactions.append(transaction)

            transaction = Transaction(at=datetime.now(), type_=TransactionType.TRANSFER,
                                      before=to_account.balance,
                                      after=to_account.balance + amount,
                                      target=from_)
            to_account.balance += amount
            to_account.transactions.append(transaction)

        case ["remove", *names]:
            indices = []
            for name in names:
                if name.isdigit():
                    indices.append(int(name))
                else:
                    index = next(index for index, account in enumerate(accounts) if
                                 account.name == name)
                    indices.append(index)

            for index in sorted(indices, reverse=True):
                accounts.pop(index)

        case ["help"]:
            print("""Commands:
    create <name> <balance>
    deposit <name> <amount>
    withdraw <name> <amount>
    print
    print <name>
    print <index>
    clear
    save <filename>
    load <filename>
    transfer <from> <to> <amount>
    remove <name>...
    help
    done""")
        case _:
            print("Unknown command")

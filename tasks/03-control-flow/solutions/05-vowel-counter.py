"""
Take a string from the user and print the number of vowels in the string.

Hint: You can iterate over a string using a for loop, and you can use the
      in operator to check if a character is in a string.

Example:
    Enter a string: hello
    There are 2 vowels in the string.
"""

# Write your code below this line 👇

string = input("Enter a string: ")
# string = ""
string = string.lower()
vowels = 0

index = 0
while index < len(string):
    character = string[index]

    if character in "aeiou":
        vowels += 1

    index += 1


for character in string:
    if character in "aeiou":
        vowels += 1

print(f"There are {vowels} vowels in the string.")

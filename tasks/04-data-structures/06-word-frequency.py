"""
Write a program that takes a sentence from the user and prints out the frequency of each word in the sentence.

Extra:
    - Ignore punctuation.
    - Ignore case.
    - Sort the words by frequency.
    - Allow the user to specify in which order the words should be sorted.
        - Most frequent first.
        - Least frequent first.
        - Alphabetical.
        - Reverse alphabetical.
        - By length.
        - Reverse length.
        - By number of vowels.
        - Reverse number of vowels.
        - By number of consonants.
        - Reverse number of consonants.
        - By number of letters.
        - Reverse number of letters.
        - By number of digits.
        - Reverse number of digits.
        - By number of special characters.
        - Reverse number of special characters.
    - Allow the user to load a file instead of inputting a sentence.

Example:
    Input: This is a sentence. This is another sentence.
    Output:
        this: 2
        is: 2
        a: 1
        sentence: 2
        another: 1

Example (extra):
    Input: [load file] example.txt
    Output:
        this: 2
        is: 2
        a: 1
        sentence: 2
        another: 1
"""

# Write your code below this line 👇

input_string = input("Input: ")

if input_string.startswith("[load file]"):
    _, filename = input_string.split()
    with open(filename) as file:
        input_string = file.read()

input_string = input_string.replace(".", "").replace(",", "").replace("!", "").replace(
    "?", "")
input_string = input_string.lower()
words = input_string.split()

word_frequencies = {}
for word in words:
    if word not in word_frequencies:
        word_frequencies[word] = 0
    word_frequencies[word] += 1

print("Output:")
for word, frequency in sorted(word_frequencies.items(), key=lambda item: item[1],
                              reverse=True):
    print(f"{word}: {frequency}")

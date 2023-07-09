value = input('Enter a word: ')
reverse = reversed(value)

if list(value) == list(reverse):
    print(f'{value} is a palindrome')

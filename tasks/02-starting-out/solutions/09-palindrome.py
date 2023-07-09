value = input('Enter a word: ')

reverse = reversed(value)
reverse = ''.join(reverse)

if value == reverse:
    print(f'{value} is a palindrome')

password = "1234"
number = 28


def enable_random():
    global password, number

    import random
    import string

    password_length = random.randint(1, 10)
    password_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(password_characters) for i in range(password_length))

    number = random.randint(1, 100)

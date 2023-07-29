import string
import random

LOWERCASE_ALPHABETS = list(string.ascii_lowercase)

UPPERCASE_ALPHABETS =  list(string.ascii_uppercase)

NUMBERS = list(string.digits)
    
SYMBOLS = list(string.punctuation)


def lower_case(n):
    return random.choices(LOWERCASE_ALPHABETS, k=n)


def upper_case(n):
    return random.choices(UPPERCASE_ALPHABETS, k=n)


def numbers_case(n):
    return random.choices(NUMBERS, k=n)


def symbol_case(n):
    return random.choices(SYMBOLS, k=n)


def length_generator(length):
    while length > 0:
            n = random.randint(1, length)
            yield n
            length -= n

def pass_generator(user_choice ,length):
    password = []
    each_length = list(length_generator(length))
    
    while len(each_length) < len(user_choice):
        each_length = list(length_generator(length))
    
    for i in (user_choice*4):

        if len(each_length) == 0:
            break
        if i == 1:
                password.append(lower_case(each_length[-1]))
        elif i == 2:
                password.append(upper_case(each_length[-1]))
        elif i == 3:
                password.append(numbers_case(each_length[-1]))
        else:
                password.append(symbol_case(each_length[-1]))
        each_length.pop()
    
    alt = ''
    final_password = []
    for i in [x for x in password]:
        alt += (''.join(i))
    for i in alt:
        final_password.append(random.choice(alt))
    return ''.join(final_password)



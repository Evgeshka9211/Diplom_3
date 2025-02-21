import random
import string

def inner_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

class StringHelper:

    @staticmethod
    def random_name():
        return inner_random_string(8)

    @staticmethod
    def random_pass():
        return inner_random_string(6)

    @staticmethod
    def random_email():
        characters = string.digits
        digits = ''.join(random.choice(characters) for _ in range(4))
        return f'user_{digits}@yandex.ru'
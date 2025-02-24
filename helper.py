import random
import string

def inner_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

class StringHelper:
    @staticmethod
    def test_data():
        name = inner_random_string(8)
        password = inner_random_string(6)

        characters = string.digits
        digits = ''.join(random.choice(characters) for _ in range(4))
        email = f'user_{digits}@yandex.ru'
        data = {
            'name': name,
            'password': password,
            'email': email
        }
        return data
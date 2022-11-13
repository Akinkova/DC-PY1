import string
from random import sample


def get_random_password(n: int = 8) -> str:
    letters = string.ascii_uppercase + string.ascii_lowercase + string.digits  # TODO написать функцию генерации случайных паролей
    return ''.join(sample(letters, n))


print(get_random_password())

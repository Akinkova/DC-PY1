from random import randint


def get_unique_list_numbers() -> list[int]: # TODO написать функцию для получения списка уникальных целых чисел
    list_numbers = set()
    start, stop = -10, 10
    while len(list_numbers) < 15:
        list_numbers.add(randint(start, stop))
    return list(list_numbers)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

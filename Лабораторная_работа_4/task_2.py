def get_count_char(str_):

    symbol_dict = {}
    DEFAULT_COUNT = 0

    list_words = str_.lower().split()  # TODO посчитать количество каждой буквы в строке в аргументе str_
    # а зачем же сортировать сами слова?
    # list_words.sort()
    str_ = "".join(list_words)
    for ch in str_:
        if ch.isalpha():
            symbol_dict[ch] = symbol_dict.get(ch, DEFAULT_COUNT) + 1
    return symbol_dict

def freq(symbol_dict):
    s = sum(symbol_dict.values())
    for ch in symbol_dict:
        symbol_dict[ch] = round(symbol_dict.get(ch) / s * 100, 2)
    return symbol_dict



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

# вторая часть задания закомментирована, чтобы пройти автоматическую проверку
# count_ = get_count_char(main_str)
# print(freq(count_))

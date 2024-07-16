import re
# Убираем ненужные знаки препинания и создаем список слов
line_list = input()\
    .translate({ord(j): None for j in '.,!?-_'})\
    .split(' ')

num_list = []
# Отбираем особенные номера в отдельный список
num_list = re.findall(r'\d\d+\\\d\d+', ' '.join(line_list))
num_list = [i.split('\\') for i in num_list]


# Функция проверяет количество цифр на удовлетворение требованиям особенного номера
# если удовлетворяет, то делает из него хороший номер
def special_to_good(special):
    '''
    Функция проверяет количество цифр на удовлетворение требованиям особенного номера
    если удовлетворяет, то делает из него хороший номер
    '''
    if len(special[0]) <= 4:
        special[0] = '0' * (4 - len(special[0])) + special[0]
    else:
        return []
    if len(special[1]) <= 5:
        special[1] = '0' * (5 - len(special[1])) + special[1]
    else:
        return []
    return special


num_list = ['\\'.join(special_to_good(i)) for i in num_list]

# Подчищаем пустые строки, чтобы не было пустых строк в выводе
num_list = [_ for _ in filter(lambda x: x != '', num_list)]
print(*num_list, sep = '\n')



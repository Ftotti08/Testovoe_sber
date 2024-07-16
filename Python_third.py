import random


# Принимает числа построчно и создает список
print('Вводите числа построчно и нажми ctrl+D')
lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)


def compare(x, y):
    '''
    Принимает 2 числа КАК СТРОКИ и выдает:
     -1 если первое больше второго,
     0 если равны
     1 если второе больше
    '''
    sxy = str(x) + str(y)
    syx = str(y) + str(x)
    if sxy < syx:
        return -1
    elif sxy > syx:
        return +1
    return 0


def quicksort(A):
    '''
    Немного модифицированный алгоритм быстрой сортировки
    Вместо классического сравнения чисел, сравнивает их как строки
    с приоритетом для меньшей длины
    '''
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if compare(elem, q) == -1:
                L.append(elem)
            elif compare(elem,q) ==1:
                R.append(elem)
            else:
                M.append(elem)
        return quicksort(L) + M + quicksort(R)


# Разворачиваем список и распечатываем его без пробелов
print(*quicksort(lines)[::-1],sep='')

n, k = [int(i) for i in input().split(' ')]
# Считываем расстояния
start_l = [[int(input())] for i in range(n)]
max_index = 0
# В цикле добавляем по банкомату в самое большое расстояние
# Если в данный отрезок уже добавлялся банкомат, то его нужно переместить чтобы делить на равные отрезки
for i in range(k):
    max_index = start_l.index(max(start_l, key= lambda x: x[0]))
    start_l[max_index] = [sum(start_l[max_index])/(len(start_l[max_index])+1) for i in range(len(start_l[max_index])+1)]

# Распечатываем финальный список построчно
for i in start_l:
    print(*i, sep = '\n')
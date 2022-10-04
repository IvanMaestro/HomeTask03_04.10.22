# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample


def init_list(count):
    ls = sample(range(count*2), count)
    return ls


def mult_couple(new_list):
    res = 0
    size = len(new_list)
    res_list = []
    if size % 2 == 0:
        for i in range(0, size//2):
            res = new_list[i] * new_list[size - 1]
            res_list.append(res)
            size -= 1
    else:
        tmp = size - 1
        for j in range(0, tmp // 2):
            res = new_list[j] * new_list[size - 1]
            res_list.append(res)
            size -= 1
        res_list.append(new_list[(tmp//2)])
    return res_list


n = int(input('Задайте размер списка: '))
while n < 0:
    n = int(input('Размер списка должен быть болбше нуля: '))
input_list = init_list(n)
print(f'{input_list}, \nПроизведение пар чисел списка -> {mult_couple(input_list)}')

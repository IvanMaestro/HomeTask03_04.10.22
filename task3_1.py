# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
# out
# [4, 2, 4, 9]
# 8
from random import sample


def init_list(count):
    ls = sample(range(count*2), count)
    return ls


def elem_sum(new_list):
    res = 0
    for i in range(len(new_list)):
        if i % 2 == 0:
            res += new_list[i]
    return res

# 1 вариант в 2 метода
# n = int(input('Задайте размер списка: '))
# while n < 0:
#     n = int(input('Размер списка должен быть болбше нуля: '))
# input_list = init_list(n)
# print(f'{input_list}, \nСумма элементов на нечетных позициях -> {elem_sum(input_list)}')


# 2 вариант - покороче
n = int(input('Задайте размер списка: '))
input_list = init_list(n)
sum1 = 0
for i in range(0, len(input_list), 2):
    sum1 += input_list[i]
print(f"{input_list} -> сумма элементов на нечётных позициях равна: {sum1}")

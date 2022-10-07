# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

number = int(input('Введите количество элементов списка: '))
random_list = [randint(1, 5) for i in range(number)]
uniq_list = []
for i in random_list:
    if random_list.count(i) == 1:
        uniq_list.append(i)
print(random_list, '=>', uniq_list)
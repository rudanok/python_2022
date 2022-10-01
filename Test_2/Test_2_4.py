# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

number = int(input('Введите число N: '))
positions = int(input('Введите число позиций: '))

# Создаём файл указанным числом позиций
def create_file(number, i):
    data = open(r"Test_2\File_2_4.txt", "w")
    while i > 0:
        data.write(str(random.randint(1, number * 2 + 1) - 1))
        if i > 1:
            data.write('\n')
        i -= 1
    data.close()

# Создаём список элементов от -N до N
list_of_elements = []
for i in range(-number, number + 1):
    list_of_elements.append(i)
print('Список элементов —>', list_of_elements)

create_file(number, positions)

# Создаём список позиций из файла
data = open(r"Test_2\File_2_4.txt", "r")
list_of_positions = data.read().split("\n")
print('Список позиций —>', list_of_positions)


# Произведение элементов на указанных позициях
result = 1
print('Произведение элементов на позициях', end = ' ')
for i in range(len(list_of_positions)):
    print(list_of_positions[i], end = ' ')
    result *= list_of_elements[int(list_of_positions[i])]
print('=', result)
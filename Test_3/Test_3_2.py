# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list, result_list = [2, 3, 4, 5, 6], []
position1 = 0
position2 = len(list) - 1
while position1 <= position2:
    result_list.append(list[position1] * list[position2])
    position1 += 1
    position2 -= 1
print(list, '=>', result_list)
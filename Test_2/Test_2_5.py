# Реализуйте алгоритм перемешивания списка.

import random

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print ('Исходный список: ', list)
for i in range(len(list)):
    j = random.randint(0, i + 1) 
    list[i], list[j] = list[j], list[i] 
print ('Перемешанный: ', list)
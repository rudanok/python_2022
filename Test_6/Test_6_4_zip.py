#  Используем функцию zip

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# Задача решается при условии, что степень многочлена = 2 и в каждом многочлене присутствует по три члена

# Функция получает список членов и возвращает список коэффициентов
def get_item_list(list):

    item_list = []
    for i in list:
        sep = i.find('x^')
        if sep >= 0:
            item_list.append(int(i[:sep]))
        else:
            if 'x' in i:
                item_list.append(int(i[0:-1]))
            else:
                item_list.append(int(i))
    return item_list

# задаём многочлены, отрезаем последнюю часть и удаляем пробелы
polinomial_1 = '3x^2 + 5x + 9 = 0'[:-4].replace(' ', '')
polinomial_2 = '5x^2 + 2x + 1 = 0'[:-4].replace(' ', '')

# получаем списки членов
list_1 = polinomial_1.split('+')
list_2 = polinomial_2.split('+')

# выводим списки членов (для наглядности)
print('Списки членов:')
print(list_1)
print(list_2)

# получаем списки коэффициентов
print('Списки коэффициентов:')
item_list_1 = get_item_list(list_1)
item_list_2 = get_item_list(list_2)

# выводим словари (для наглядности)
print(item_list_1)
print(item_list_2)

# получаем список кортежей элементов
item_zip = zip(item_list_1, item_list_2)
item_list = list(item_zip)

# выводим итоговый многочлен с суммированием элементов
print('Сумма многочленов:')
print(f'{sum(item_list[0])}x^2 + {sum(item_list[1])}x + {sum(item_list[2])} = 0')

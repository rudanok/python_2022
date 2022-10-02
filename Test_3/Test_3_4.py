# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

binary_number = ''
decimal_number = int(input('Введите десятичное число: '))
print(decimal_number, end = ' => ')
while decimal_number != 0:
    binary_number = str(decimal_number % 2) + binary_number
    decimal_number //= 2
print(binary_number)
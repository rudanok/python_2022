# Задание 2a. Создайте программу для игры с конфетами против бота.

# Условие задачи: На столе лежит N конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

from random import randint
import time

def input_number(player_name, player_number, amount):
    if player_number == 1: # бот
        x = randint(1, 28)
        print(f'{player_name} взял {x}.', end = ' ')
    else:
        print(f'{player_name}, сколько конфет вы берёте:', end = ' ')
        x = int(input())
    while x < 1 or x > 28 or x > amount:
        x = int(input(f'{player_name}, введите корректное число: '))
    return x

amount = 100
player_number = randint(1, 2)

print()
print(f'Правила игры: на столе {amount} конфет, вы и бот по очереди берёте от 1 до 28 конфет.')
print('Кто ходит первым, решает жеребьёвка. Выигрывает тот, кто делает последний ход.')

user_name = input('Введите ваше имя: ')

print('Жеребьёвка...')
time.sleep(3)
if player_number == 1:
    print('Первым ходит бот!')
else:
    print('Первым ходит', user_name)

while amount > 28:
    if player_number == 1:
        q = input_number('Бот', player_number)
        player_number = 2
    else:
        q = input_number(user_name, player_number)
        player_number = 1
    amount -= q
    print(f'На столе осталось {amount}.')

if player_number == 1:
    print('Победил бот!')
else:
    print(f'Победил {user_name}!')
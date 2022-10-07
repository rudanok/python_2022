# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number, list = int(input("Введите натуральное число: ")), []

for i in range(2, int(number ** 0.5) + 1): 
    while (number % i == 0): 
        list.append(i)
        number //= i 

if (number != 1): 
    list.append(number)

print(list)
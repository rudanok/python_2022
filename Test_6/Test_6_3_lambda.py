# Используем lambda и List Comprehetion
# 
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Используем List Comprehention

x = int(input('Введите целое число: '))

factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
factorial_list = [factorial(i) for i in range(1, x + 1)]
print(factorial_list)
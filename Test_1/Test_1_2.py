# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

list_of_number = list(map(float, input('Введите три числа через запятую: ').split(',')))    
left = not (list_of_number[0] or list_of_number[1] or list_of_number[2])
right = not list_of_number[0] and not list_of_number[1] and not list_of_number[2]
if left == right:
    print("Истина")
else:
    print("Ложь")    


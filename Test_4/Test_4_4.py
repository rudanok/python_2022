# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = 2 # задача решается только при условии, что k = 2

def get_polinomial(k):

    a = int(randint(0, 100))
    b = int(randint(0, 100))
    c = int(randint(0, 100))

    if a == 0:
        p = '' # polinomial
    elif a == 1:
        p = 'x^{}'.format(k)    
    else:
        p = '{}*x^{}'.format(a, k)

    if b == 0:
        term = ''
    elif b == 1:
        term = 'x'
    else:
        term = '{}*x'.format(b) 

    if not p: # первый член = 0
        if not term: # второй член = 0
            return 'Не удалось сформировать многочлен из заданных значений!'      
        else: # второй член != 0
            p = term
    else: # первый член != 0
        if term: # второй член !=0
            p = '{} + {}'.format(p, term)    

    if c == 0:
        term = ''
    else:
        term = str(c)   

    if not term: # третий член = 0
        p = '{} = 0'.format(p)
    else: # третий член != 0  
        p = '{} + {} = 0'.format(p, term)  

    return p

polinomial = get_polinomial(k)

my_file = open(r"Test_4\File_4_4.txt", "w")
my_file.write(polinomial)
my_file.close()

print(f'Результат «{polinomial}» записан в файл File_4_4.txt')
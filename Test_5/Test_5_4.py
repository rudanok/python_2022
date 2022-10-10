# Задание 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode(text):  
    symbol = ''
    result = ''
    count = 0       
    for i in text:
        if i != symbol:
            if count != 0:
                result += str(count) + symbol               
            symbol = i
            count = 0
        count += 1
    result += str(count) + symbol    
    return result

def decode(text):
    count = ''
    result = ''
    for i in text:
        if i.isdigit():
            count += i
        else:
            result += i * int(count)
            count = ''
    return result

data = open(r'Test_5\Text_5_4a.txt', 'r', 1, 'utf-8')
file_text = data.read()
data.close()
encode_text = encode(file_text)
print(f'Кодированный текст:\n{encode_text}') 

data = open(r'Test_5\Text_5_4b.txt', 'r', 1, 'utf-8')
file_text = data.read()
data.close()
decode_text = decode(file_text)
print(f'Декодированный текст:\n{decode_text}') 
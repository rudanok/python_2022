# Задание 1: Напишите программу, удаляющую из текста все слова, содержащие "абв".

user_text = 'Слово1абв Слово2 Слово3 Словоабв4'
search_text = 'абв'
result = [i for i in user_text.split() if search_text not in i]
print(' '.join(result))
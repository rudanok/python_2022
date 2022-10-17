# Получаем список строк из файла
def get_data():
    with open(r'Test_7\phonebook.csv', 'r', 1, 'utf-8') as file:
        data = file.read().split("\n")
        data.pop(0) # удаляем строку с заголовками
    return data        

# Ищем слово во всех полях справочника, возвращаем список
def find_data(word, data):
    find_list = [item for item in data if word in item]
    return find_list

# Записываем в справочник нового абонента
def save_item(item_list):
    with open(r'Test_7\phonebook.csv', 'a+', 1, 'utf-8') as file:
        file.write('\n')
        file.write(';'.join(item_list))
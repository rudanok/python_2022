# Выводим разделитель строк
def print_sep():
    print('=' * 28)   

# Показываем меню пользователю
def show_menu(user_menu):
    print()
    print('—- ТЕЛЕФОННЫЙ СПРАВОЧНИК -—')
    print_sep()
    print('\n'.join(user_menu))
    print_sep()

# Предлагаем пользователю выбрать действие
def choose_action(size):
    number = int(input('Введите номер пункта меню: '))
    while number < 1 or number > size:
        number = int(input('Введите корректный номер: '))
    print_sep()    
    return number    

# Выводим строку данных телефонного справочника в определённом формате
def output_item(item_list):
    print(item_list[0], f'{item_list[1]}:', item_list[2], f'— {item_list[3]}' if item_list[3] else '')   

# Получаем от пользователя поисковый запрос
def input_word():
    return input('Что ищем: ')   

# Выводим информацию пользоваетлю
def print_info(info):
    print(info)

# Получаем от пользователя данные абонента
def input_item():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    note = input('Введите примечание (если нужно): ')
    return [last_name, first_name, phone_number, note]   

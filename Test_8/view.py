# Выводим разделитель строк
def print_sep():
    print('=' * 30)   

# Показываем меню пользователю
def show_menu(user_menu):
    print()
    print('СПРАВОЧНИК СОТРУДНИКОВ')
    print_sep()
    print('\n'.join(user_menu))
    print_sep()

# Предлагаем пользователю выбрать действие
def choose_action(size):
    number = int(input('Введите номер пункта меню: '))
    while number < 1 or number > size:
        number = int(input('Введите корректный номер: '))
    # print_sep()    
    return number    

# Выводим строку данных телефонного справочника в определённом формате
def output_employees(employees):
    if employees:
        for employee in employees:
            print(f'{employee["id"]}. {employee["last_name"]} {employee["first_name"]}, {employee["position"]} (тел.: {employee["phone_number"]}) — {employee["salary"]} руб.')
    else:
        print('Данные не найдены!')

# Получаем от пользователя поисковый запрос
def input_text(search_text):
    return input(search_text)   

# Выводим информацию пользоваетлю
def print_info(info):
    print(info)

# Получаем от пользователя данные сотрудника
def input_data(id = 0):
    if id == 0:
        id = int(input('Введите id: '))
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    position = input('Введите должность: ')
    phone_number = input('Введите номер телефона: ')
    salary = float(input('Введите зарплату: '))
    return {'id':id, 'last_name': last_name, 'first_name': first_name, 'position': position, 'phone_number': phone_number, 'salary': salary}
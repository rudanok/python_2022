import model
import view

def start():

    data = model.get_data() # получаем список записей телефонного справочника (без строки с заголовками)

    # Считаю, что меню нужно создавать именно здесь, а не в model,
    # поскольку алгоритм выбора находится в этой функции ниже
    menu = ['1. Показать справочник',\
            '2. Найти абонента',\
            '3. Добавить абонента',\
            '4. Завершить работу']
    view.show_menu(menu) # показываем меню пользователю

    action = view.choose_action(len(menu)) # предлагаем выбрать действие

    if action == 1: # показываем справочник 
        for item in data:
            item_list = item.split(';') # получаем строку справочника в виде списка
            view.output_item(item_list) # выводим строку справочника
    elif action == 2: # ищем абонента
        word = view.input_word() # предлагаем ввести слово для поиска
        found_items = model.find_data(word, data) # ищем
        if found_items: # выводим результаты поиска
            view.print_info('Результаты поиска:')
            view.print_sep()
            for item in found_items:
                item_list = item.split(';')
                view.output_item(item_list) # выводим строку данных телефонного справочника
        else:
            view.print_info('Данные не найдены!')  
    elif action == 3: # добавляем абонента
        item_list = view.input_item() # получаем данные от пользователя
        model.save_item(item_list) # записываем данные в файл
        view.print_sep()
        view.print_info('Данные абонента записаны.')
    else:
        view.print_info('Работа завершена.')

    view.print_sep()     
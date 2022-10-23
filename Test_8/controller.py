import model
import view

def start():

    menu = ['1. Найти сотрудника',\
            '2. Сделать выборку сотрудников по должности',\
            '3. Сделать выборку сотрудников по зарплате',\
            '4. Добавить сотрудника',\
            '5. Удалить сотрудника',\
            '6. Изменить данные сотрудника',\
            '7. Экспортировать данные в формате json',\
            '8. Завершить работу']

    answer = '' 
    while answer != '+':      
        answer = view.input_text('Для просмотра меню введите плюс: ')      
    view.show_menu(menu) # показываем меню пользователю
    action = view.choose_action(len(menu)) # предлагаем выбрать действие

    if action == 1: # поиск сотрудников по фамилии
        name = view.input_text('Введите для поиска фамилию или имя: ')
        result = model.find_by_name(name) # ищем
        view.output_employees(result) # выводим
        start()    
    elif action == 2: # выборка сотрудников по должности   
        position = view.input_text('Введите для поиска название должности: ')   
        result = model.find_by_position(position) # ищем
        view.output_employees(result) # выводим
        start()                   
    elif action == 3: # выборка сотрудников по зарплате 
        text = view.input_text('Введите мин. и макс. зарплату через пробел: ')
        result = model.find_by_salary(text) # ищем
        view.output_employees(result) # выводим
        start()                                              
    elif action == 4: # добавление сотрудника
        employee = view.input_data() # получаем данные от пользователя
        model.add_employee(employee)
        view.print_info('Данные нового сотрудника записаны.')
        start()  
    elif action == 5: # удаление сотрудника
        id = int(view.input_text('Введите id сотрудника, которого нужно удалить: '))
        if model.find_by_id(id):
            model.del_employee(id) # удаляем
            view.print_info(f'Данные сотрудника с id={id} удалены.')  
        else:
            view.print_info(f'Сотрудник с id={id} не найден.')                                        
        start() 
    elif action == 6: # изменение данных сотрудника
        id = int(view.input_text('Введите id сотрудника, данные которого нужно изменить: '))
        if model.find_by_id(id):
            new_data = view.input_data(id) # получаем новые данные от пользователя
            model.edit_employee(id, new_data) # изменяем
            view.print_info(f'Данные сотрудника с id={id} изменены.') 
        else:
            view.print_info(f'Сотрудник с id={id} не найден.')                                    
        start() 
    elif action == 7: # экспорт данных в формате json
        model.write_json()
        view.print_info('Данные экспортированы в файл employees.json.')
        start()
    elif action == 8:
        view.print_info('Работа завершена.')
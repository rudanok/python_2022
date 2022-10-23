import csv
import json

# Получение данных из csv-файла
def read_csv():
    employees = []
    with open(r'Test_8\employees.csv', 'r', 1, 'utf-8') as file:
        csv_reader = csv.reader(file)
        first_line = True
        for row in csv_reader:
            if first_line:
                first_line = False
                continue
            item = {}
            item['id'] = int(row[0])
            item['last_name'] = row[1]
            item['first_name'] = row[2]
            item['position'] = row[3]
            item['phone_number'] = row[4]
            item['salary'] = float(row[5])
            employees.append(item)
    return employees    

# Получение данных из json-файла
def read_json() -> list:
    employee = []
    with open(r'Test_8\employees.json', 'r', 1, 'utf-8') as file:
        for line in file:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee    

# Экспорт данных в csv-файл
def write_csv(employees: list):
    with open(r'Test_8\employees.csv', 'w', 1, 'utf-8') as file:
        csv_writer = csv.writer(file)
        for employee in employees:
            csv_writer.writerow(employee.values())  

# Экспорт данных в json-файл
def write_json():
    employees = read_csv()
    with open(r'Test_8\employees.json', 'w', 1, 'utf-8') as file:
        for employee in employees:
            file.write(json.dumps(employee) + '\n')

# Поиск сотрудника по id
def find_by_id(id):
    employees = read_csv()
    for employee in employees:
        if employee['id'] == int(id):
            return True
    return False

# Поиск сотрудников по фамилии или имени
def find_by_name(name):
    employees = read_csv()
    return [x for x in employees if name in x['last_name'] or name in x['first_name']]

# Поиск сотрудников по должности
def find_by_position(position):
    employees = read_csv()
    return [x for x in employees if position in x['position']]   

# Поиск сотрудников по зарплате
def find_by_salary(salary_range):
    salary_list = list(map(float, salary_range.split()))
    employees = read_csv()
    return [x for x in employees if salary_list[0] <= x["salary"] <= salary_list[1]]  

# Добавление нового сотрудника
def add_employee(employee):
    with open(r'Test_8\employees.csv', 'a', 1, 'utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(employee.values())           

# Удаление сотрудника по id
def del_employee(id):
    employees = read_csv()
    employees = list(filter(lambda x: x["id"] != id, employees))
    employees.insert(0, {'id': 'id', 'last_name': 'last_name', 'first_name': 'first_name', 'position': 'position', 'salary': 'salary'})    
    write_csv(employees)      

# Редактирование сотрудника по id
def edit_employee(id, new_data):
    employees = read_csv()
    for employee in employees:
        if employee['id'] == id:
            employee['last_name'] = new_data['last_name']
            employee['first_name'] = new_data['first_name']
            employee['position'] = new_data['position']
            employee['phone_number'] = new_data['phone_number']
            employee['salary'] = new_data['salary']  
    employees.insert(0, {'id': 'id', 'last_name': 'last_name', 'first_name': 'first_name', 'position': 'position', 'salary': 'salary'})
    write_csv(employees)
import os

def add_new_user(name: str, phone: str, filename: str):
    with open(filename, 'a', encoding='utf-8') as wrtbl:
        lines_count = len(wrtbl.read().split('\n'))
        wrtbl.write(f"\n{lines_count + 1};{name};{phone}")
    return "Новый пользователь добавлен"

def read_all(filename) -> str:
    with open(filename, 'r', encoding='utf-8') as data:
        result = data.read()
    return result

def search_user(data: str, search_str: str) -> str:
    lines = data.strip().split('\n')
    result = []
    for line in lines:
        if search_str in line:
            result.append(line)
    return '\n'.join(result)

def check_directory(filename: str):
    if filename not in os.listdir():
        return None

INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - копирование данных в другой файл
"""
DATASOURCE = 'phone.txt'


while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(DATASOURCE))
    elif mode == 2:
        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        print(add_new_user(name, phone, DATASOURCE))
    elif mode == 3:
        search = input('Введите строку для поиска: ')
        data = read_all(DATASOURCE)
        print(search_user(data, search))
    elif mode == 4:
        filename = input("Введите имя файла: ")
        if not check_directory(filename):
            print(f"Файл {filename} не существует")
            continue
        line_number = int(input("Введите номер строки: "))
        with open(DATASOURCE, 'r', encoding='utf-8') as f1, open(filename, 'w', encoding='utf-8') as f2:
            lines = f1.readlines()
            if len(lines) < line_number:
                print("Неверный номер строки")
                continue
            f2.write(lines[line_number-1])
            print(f"Строка {line_number} скопирована в файл {filename}")

# Ввод данных в телефонный справочник

import format

def add():
    number = int(input('Выберите формат данных (1 или 2): '))
    if 1 <= number <= 2:
        lastName = input('Введите Фамилию: ')
        firstName = input('Введите Имя: ')
        tel = input('Введите Телефон: ')
        comm = input('Введите Описание: ')
        if number == 1:
            format.add_1(lastName, firstName, tel, comm)
        elif number == 2:
            format.add_2(lastName, firstName, tel, comm)
    else: print("такого варианта нет")
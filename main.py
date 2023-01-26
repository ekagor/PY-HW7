# главный модуль

import add_contact
import print_contact

number = int(input('Выберите действие:\n\
    1: Вывести телефонные контакты\n\
    2: Добавить телефонный контакт\n\
    '))

if   number == 1:
    print_contact.contact()
elif number == 2:
    add_contact.add()
else: print("такого действия нет")
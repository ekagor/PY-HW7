# модуль печати

def contact():

    number = int(input('Выберите файл данных (1 или 2): '))
    if number == 1: fileName = "telefon_book_1.txt"
    elif number == 2: fileName = "telefon_book_2.txt"
    else: print("такого файла нет")
    with open(fileName, 'r', encoding = 'utf-8') as file:
        for line in file:
            print(line, end = '')
# Запись в файлы

def add_1(lastName, firstName, tel, comm):

    with open('telefon_book_1.txt', 'a', encoding='utf-8') as file:
        file.write('{}\n{}\n{}\n{}\n'
                    .format(lastName, firstName, tel, comm))    

def add_2(lastName, firstName, tel, comm):
    with open('telefon_book_2.txt', 'a', encoding='utf-8') as file:
        file.write('{},{},{},{}\n'
                    .format(lastName, firstName, tel, comm))  
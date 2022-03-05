# Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных свидетельствует
# пустая строка.
file = []
while True:
    stroka = input("Введите текст: ")
    if stroka == '':
        print(file)
        exit()
        else:
        nstroka = stroka + '\n'
        file.append(nstroka)
            with open("#1.txt", "w") as file_obj:
                file_obj.writelines(file)



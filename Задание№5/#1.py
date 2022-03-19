# Создайте модуль (модуль - программа на Python, т.е. файл с расширением
# .py). В нем создайте функцию создающую директории от dir_1 до dir_9 в папке
# из которой запущен данный код. Затем создайте вторую функцию удаляющую
# эти папки. Проверьте работу функций в этом же модуле

import os
dir_1 = 'C:/Users/Иван/Телеметрия/Задание№5'

def dir_2(dir):

    for i in range(dir):
        pr = os.path.join(dir_1, 'dir_' + str(i))

        os.mkdir(pr)
        print("Directory '% s' created" % i)

    for i in range(dir):

        pr = os.path.join(dir_1, 'dir_' + str(i))


        if os.path.exists(pr):
            os.rmdir(pr)
            print("Directory '% s' deleted" % i)

dir_2(10)









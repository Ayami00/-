#  Создать (программно) текстовый файл, записать в него программно набор
# чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в
# файле и выводить ее на экран.

with open("#5.txt", 'w') as file:
    str = ['1 2 3 4']
    file.writelines(str)

with open('#5.txt', 'r') as file:
    numbers_str = file.read()
    numbers_lst = numbers_str.split(' ')
    print(f"Числа:\n{numbers_str}")
    print(f"Сумма чисел:\n{sum([int(i) for i in numbers_lst])}")
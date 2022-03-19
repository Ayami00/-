# Напишите программу, в которой описывается функция с произвольным
# количеством аргументов. В качестве результата функция возвращает сумму
# значений целочисленных аргументов. При вычислении результата
# использовать обработку исключений.


def devizion(number_1, number_2):

    try:
        result = (number_1+number_2)

    except TypeError:
        result = f'{number_1} или {number_2} Переменная должна быть числом'

    return result

print(devizion(3,-5))
print(devizion(4, 3))
print(devizion(2, 0))
print(devizion('aaa', 0))
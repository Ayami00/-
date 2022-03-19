# Напишите программу, в которой пользователю предлагается ввести два
# целочисленных значения. Эти значения определяют границы диапазона, в
# котором отображаются целые числа. Использовать обработку исключений.
import sys
inp1 = input('Введите первое значение: ')
inp2 = input('Введите второе значение: ')
try:
    int(inp1)
    int(inp2)
except ValueError:
    print(f'{inp1} или {inp2} Переменная должна быть числом')
    sys.exit()
except TypeError:
    print(f'{inp1} или {inp2} Переменная должна быть числом')
    sys.exit()

def fun(inp1, inp2):
    x1 = int(inp1)
    x2 = int(inp2)
    try:
        if x1 < x2:
            for x in range(x1, x2+1):
                print(x)
                x = x + 1
        elif x2 < x1:
            for x in reversed(range(x2, x1+1)):
                print(x)
                x = x - 1;
    except ValueError:
        print(f'{x1} или {x2} Неверные значение')
    except FloatingPointError:
        print (f'{x1} или {x2} Число должно быть целым')
fun(inp1, inp2)

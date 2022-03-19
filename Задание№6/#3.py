#  Напишите программу для решения квадратного уравнения вида ax2+bx+c.
# Вывести график квадратного уравнения. Коэффициенты a, b, c запросить у
# пользователя. Использовать обработку исключений.
import math
import matplotlib
import random
import matplotlib.pyplot as plt
import  numpy as np
a = int(input('Введите a:'))
b = int(input('Введите b:'))
c = int(input('Введите c:'))
def devizion(a, b, c):
    try:
        D = (b**2)-4*a*c
        x1 = (-b + math.sqrt(D)) / 2 * a
        x2 = (-b - math.sqrt(D)) / 2 * a
    except TypeError:
        D = f'{a},{b},{c}    Переменная должна быть числом'
    except UnboundLocalError:
        x1 = 'Корня нет'
        x2= 'Корня нет'
    except ValueError:
        x1 = 'Корня нет'
        x2 = 'Корня нет'
    return D, x1, x2
x = np.linspace(-100,100, 100)
y = a*x**2 + b*x + c
fig, ax = plt.subplots()
ax.plot(x, y, color="red", label="y(x)")
ax.set_title("График функции")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.text(-50,17500,r'$x1={x1}$')
plt.text(-50,15000,r'$x2={x2}$')
plt.show()
D, x1, x2 = devizion(a, b, c)
print(f'Итог:{D},{x1},{x2}')




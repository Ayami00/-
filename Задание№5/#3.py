# Создайте файл graphics.py и в нем реализуйте построение графиков (по
# вариантам см. Приложение).
# Вариант_10

import matplotlib
import random
import matplotlib.pyplot as plt
import  numpy as np

plt.figure(figsize=(9,9))
plt.subplot(3, 1, 1)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.grid(True)

x = np.linspace(-5, 5)
y = x**3+x-2
plt.plot(x, y, 'b-')

plt.subplot(3, 1, 2)

z = x**2+2
z1 = x*2+1
y1 = z/z1
plt.xlabel('x', fontsize=14)
plt.xlim((-5,5))
plt.ylabel('y', fontsize=14)
plt.grid(True)
plt.plot(x, y1, 'b-')

plt.subplot(3, 1, 3)
 y3 = x**3+x-2
plt.xlabel('x', fontsize=14)
plt.xlim((-10,0))
plt.ylabel('y', fontsize=14)
plt.grid(True)
plt.plot(x, y2, 'b-')

plt.subplot(3, 1, 3)
 y4=-2*x+1
plt.xlabel('x', fontsize=14)
plt.xlim((0,3))
plt.ylabel('y', fontsize=14)
plt.grid(True)
plt.plot(x, y4, 'b-')

plt.subplot(3, 1, 3)
 y5=z/z1
plt.xlabel('x', fontsize=14)
plt.xlim((3,10))
plt.ylabel('y', fontsize=14)
plt.grid(True)
plt.plot(x, y5, 'b-')
plt.show()



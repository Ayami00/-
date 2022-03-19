# Напишите программу, в которой с использованием потоков, вычисляется
# сумма квадратов натуральных чисел. Сумма вычисляется определенное время,
# по аналогии с примером из листинга
import threading
from time import sleep

def mysum():
  global num
  k=1
  txt=str(num)
  while myevent.is_set():
   num+=k**2
   txt+="^2 + "+str(k)
   print(f'["{k}"], {txt} = {num}')
   k+=1
   sleep(0.3)
print('Сумма целых чисел')
t = threading.Thread(target=mysum)
num=0
myevent = threading.Event()
myevent.set()
t.start()
sleep(3)
myevent.clear()
if t.is_alive():
 t.join()
print(f'Результат: {num}')

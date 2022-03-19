# Напишите программу, в которой создается и построчно заполняется
# двумерный список (список, элементами которого являются списки). Для
# заполнения каждой строки (каждого внутреннего списка) используется
# отдельный дочерний поток.
from threading import Thread, Semaphore
from time import sleep
def sp1(num, time, text):
    semaphor.acquire()
    Asv=[]
    for k in range(num):
        Asv.append([k+4])
        sleep(time)
        print(Asv)
    semaphor.release()

def sp1_1(num, time, text):
    semaphor.acquire()
    B = []
    for n in range(num):
        B.append([n+1])
        sleep(time)
        print(B)
    semaphor.release()
semaphor = Semaphore(5)

potok = Thread(target=sp1, args=(3, 0.04, 'Поток1'))
potok.start()
potok1 = Thread(target=sp1_1, args=(6, 0.15, 'Поток1'))
potok1.start()

if potok.is_alive():
    potok.join()

if potok1.is_alive():
    potok1.join()
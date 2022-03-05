# функцию my_func(), которая принимает три позиционных
#аргумента, и возвращает сумму наибольших двух аргументов.

def fun(x, y, z):
    suma = [x, y, z]
    sp = [ ]

    a = max(suma)
    sp.append(a)
    suma.remove(a)
    b = max(suma)
    sp.append(b)
    print(sum(sp))
print(fun(int(input("Введите первое число:")), int(input("Введите второе число: ")), int(input("Введите третье число:"))))
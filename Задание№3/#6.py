#Реализовать функцию int_func(), принимающую слово из маленьких
#латинских букв и возвращающую его же, но с прописной первой буквой.
#Например, print(int_func(‘text’)) -> Text.
#--------------------------------------------
def fun(a):
    return a.title()
print(fun("AAA sSS mmM"))
#---------------------------------------
def fun1(a):
    x = a.split(' ')
    k = []
    for i in x:
        el = str(i)
        x = el[:1].upper()
        z = x + el[1:]
        k.append(z)
    return k
print(fun1("sss mmmm aaa"))
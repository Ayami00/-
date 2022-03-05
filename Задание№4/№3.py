# Создать текстовый файл (не программно), построчно записать фамилии
# студентов и величину их стипендий. Определить, кто из студентов имеет доход
# менее 5 тыс., вывести фамилии этих студентов. Выполнить подсчет средней
# величины дохода студента

file = {'Student 1': 0, 'Student 2': 10, 'Student 3': 9, 'Student 4': 5, 'Student 5': 0, 'Student 6': 0, 'Student 7': 3}
try:
    file_obj = open("#3.txt", 'w')
    for familia, stipendia in file.items():
        file_obj.write(familia + ':' + str(stipendia) + "\n")
except IOError:
    print("Ошибка")
finally:
    file_obj.close()
summa = 0
stip = 0
fam = []
with open("#3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 5:
            fam.append(tokens[0])
        summa += int(tokens[1])
        stip += 1
srednee = summa / stip
print(f"Фамилии: {fam}")
print(f"Среднее: {srednee}")

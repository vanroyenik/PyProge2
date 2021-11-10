# -*- coding: utf-8 -*-
"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, 
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

import os

ppath = 'C:\\Users\\Admin2018\\py_notepad\\HomeTask_5'
os.chdir(ppath)

f1 = open("l5_task1_out.txt", 'w')

while True:
    word = str(input(">>> "))
    if word != '':
        f1.write(word + "\n")
        continue
    else:
        print("Finished")
        break

f1.close()

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
"""

f2 = open("l5_task2_in.txt", 'r')
text = f2.readlines()#список строк
f2.close()

print("Количество строк = %d" %(len(text)))
for i in range(len(text)):
    print("Строка #%d - %d символов;" %(i+1, len(text[i])))


"""
3. Создать текстовый файл (не программно), построчно записать фамилии 
сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад 
менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""    

from functools import reduce

f3 = open("l5_task3_in.txt", 'r', encoding='utf-8')
text = f3.readlines()
f3.close()

pars_text = dict([line.split() for line in text])#вложенный список в словарь

def salary_chk(emp_dict):
    min_sal = [emp for emp in emp_dict if int(emp_dict[emp]) < 20000]
    return min_sal

lst_avg = reduce(lambda x, y: int(x) + int(y), pars_text.values()) / len(pars_text)
   
        
print("Сотрудники с З/П меньше 20т.: ", salary_chk(pars_text))
print("Средняя зарплата: ", lst_avg)


"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую 
построчно данные. При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""

nwords = ('Один', 'Два', 'Три', 'Четыре')


def translator(book):
    for i in range(len(book)):
        sub = book[i].split()
        sub[0] = nwords[i]
        book[i] = " ".join(sub)
        

with open("l5_task4_in.txt", "r", encoding=("utf-8")) as f4:
    try:   
        strs = f4.readlines()
    except IOError:
        print("Произошла ошибка чтения")

translator(strs)

with open("l5_task4_out.txt", "w", encoding=("utf-8")) as f4:
    try:
        for line in strs:
            f4.write(line+"\n")
    except IOError:
        print("Произошла ошибка записи")

            
"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, 
разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
"""

from random import randint
from functools import reduce

fl_len = randint(0, 1000)

with open("l5_task5_out.txt", "w", encoding=("utf-8")) as f5:
    try:
        for i in range(fl_len):
            f5.write(str(randint(0, 1000))+" ")
    except IOError:
        print("Произошла ошибка записи")
        
with open("l5_task5_out.txt", "r", encoding=("utf-8")) as f5:
    try:
        mass = f5.readline().split()
    except IOError:
        print("Произошла ошибка записи")
        
def summator(a, b):
    return int(a) + int(b)

print("В массиве длиной %d - Сумма чисел = %d" %(len(mass), reduce(summator, mass)))


"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка 
описывает учебный предмет и наличие лекционных, практических и лабораторных занятий 
по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
 Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
 Вывести словарь на экран.
"""
from functools import reduce

f = open("l5_task6_in.txt", "r", encoding='utf-8') #прочитали текст
mass = f.readlines()
f.close()

sp_mass = [line.split() for line in mass] #парсим по пробелу - вложенный список


for i in range(len(sp_mass)): #убираем лишние символы
    for pos in range(len(sp_mass[i])):
        if sp_mass[i][pos].find(":") != -1:
            sp_mass[i][pos] = sp_mass[i][pos].replace(":", "")
        if sp_mass[i][pos] == "-":
            sp_mass[i][pos] = sp_mass[i][pos].replace("-", "0")
        if sp_mass[i][pos].find("(л)") != -1:
            sp_mass[i][pos] = sp_mass[i][pos].replace("(л)", "")
        if sp_mass[i][pos].find("(пр)") != -1:
            sp_mass[i][pos] = sp_mass[i][pos].replace("(пр)", "")
        if sp_mass[i][pos].find("(лаб)") != -1:
            sp_mass[i][pos] = sp_mass[i][pos].replace("(лаб)", "")

subjects = [item[0] for item in sp_mass] #список ключей-предметов
times = [[int(item) for item in sp_mass[i][1:]] for i in range(len(sp_mass))] #список значений по предмету и привели к типу int

lesson = dict(zip(subjects, times))#сформировали словарь "предмет - количество часов"

def summr(a, b): # сумматор учебных часов
    return a+b

for subj in lesson.keys(): #проводим вычисления по каждому предмету
    lesson[subj] = reduce(summr,lesson.get(subj))



print(lesson) #готово


'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать 
данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: 
    [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
    
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''

import json
import statistics

firms = []
with open("l5_task7_in.txt") as textf:
    for linef in textf:
        firms.append(linef.split())
        
f_keys = [item[0] for item in firms]        
f_profits = [int(item[2])-int(item[3]) for item in firms]
firms_profit = dict(zip(f_keys, f_profits))

avg_profit = dict(average_profit = statistics.mean([x for x in f_profits]))

firms_report = [firms_profit, avg_profit]

with open("l5_task7_out.json", "w") as out_file:
    json.dump(firms_report, out_file)
        
        
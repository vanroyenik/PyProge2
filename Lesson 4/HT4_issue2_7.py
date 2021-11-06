
"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, 
значения которых больше предыдущего элемента.
"""

#inlist = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

lenlist = int(input("Введите длину массива: "))
inlist = [int(input("Элемент %d: " %(i))) for i in range(lenlist) ]
outlist = [inlist[i] for i in range(1,len(inlist)) if inlist[i] > inlist[i-1]]
#[12, 44, 4, 10, 78, 123]

print("Входной массив: ", inlist)
print("Выходной массив:", outlist)


"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. 
Необходимо решить задание в одну строку
"""

res = [i for i in range(20, 240+1) if ((i % 20) == 0 or (i % 12) == 0)]
print(res)


"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать итоговый массив чисел, соответствующих требованию. 
Элементы вывести в порядке их следования в исходном списке. 
Для выполнения задания обязательно использовать генератор.
"""

#inlist = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#2 2 2 7 23 1 44 44 3 2 10 7 4 11
inlist = str(input("Введите список: ")).split()
inlist = [int(i) for i in inlist]
outlist = [i for i in inlist if inlist.count(i) == 1]

print("Результат: ", outlist)
#Результат:  [23, 1, 3, 10, 4, 11]

#__________________________________________

def gener(input_list):
    for el in input_list:
        if input_list.count(el) == 1:
            yield el
            

outlist = []
generated_output = gener(inlist)
for i in generated_output:
    outlist.append(i)
print("Результат: ", outlist)

#print(next(generated_output))

"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce 

inlist = [x for x in range(100,1000+1)]

#1
la_multiple = reduce(lambda a, b: a*b, inlist)
print(la_multiple)
#2
def multiple (a, b):
    return a * b

mult = reduce(multiple, inlist)
print(mult)

"""
#test
if mult == la_multiple:
    print("ok")
"""   
    
"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""

import time
from itertools import count
from itertools import cycle
#A
for num in count(int(input("Укажите число: "))):
    if num % 100 == 0:
        time.sleep(3)
        check = str(input("Продолжить? Y/N - "))
        if check.lower() == 'y':
            pass
        else:
            print("Завершено")
            break
    else:
        print(num)
        
#B
с = 0
word = str(input("Введите строку: "))
for char in cycle(word):
    if с >= 3*len(word):
        break
    else:
        print(char)
        с += 1
    

"""
7. Реализовать генератор с помощью функции с ключевым словом yield, 
создающим очередное значение. При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n). 
Функция отвечает за получение факториала числа, 
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
"""
from functools import reduce

def fact(num):
    for el in range(1, num+1):
        yield el
        
def multiplier(curr, prev):
    return curr * prev
    

in_num = int(input("Введите число: "))

factorial = reduce(multiplier, fact(in_num))
print("Факториал числа %d равен %d " %(in_num, factorial))
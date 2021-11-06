# -*- coding: utf-8 -*-
"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета 
заработной платы сотрудника. В расчете необходимо использовать формулу: 
(выработка в часах * ставка в час) + премия. 
Для выполнения расчета для конкретных значений необходимо запускать скрипт с 
параметрами.
"""

from sys import argv

script_name, prod_hrs, rate, bonus = argv

def salary_calc(v_pr_hr, v_rt, v_bon):
    return (int(v_pr_hr) * int(v_rt)) + int(v_bon)

print("Выработка: ", prod_hrs)
print("Ставка: ", rate)
print("Премия: ", bonus)

print("Зарплата: ", salary_calc(prod_hrs, rate, bonus))


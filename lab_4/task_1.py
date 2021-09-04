# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script, hours, salary, bonus = argv  

def wage(hours, salary, bonus):
    return int(salary) * int(hours) + int(bonus)

print(wage(hours, salary, bonus))
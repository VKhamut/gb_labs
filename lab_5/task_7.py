# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

with open("./gb_labs/lab_5/task_7_file", "r") as f:
    content = f.readlines()
#print(content)

average_profit = 0
average_count = 0
list_of_firms = []
list_of_profits = []

for firm in content:
    list_of_firms.append(firm.split()[0])
    list_of_profits.append(int(firm.split()[2]) - int(firm.split()[3]))
    if int(firm.split()[2]) > int(firm.split()[3]): 
        average_profit = average_profit + int(firm.split()[2]) - int(firm.split()[3])
        average_count += 1
average_profit = round(average_profit / average_count,2)

final_list = [dict(zip(list_of_firms, list_of_profits)), {"average_profit": average_profit}]
print(final_list)

with open("./gb_labs/lab_5/task_7.json", "w") as f:
    json.dump(final_list, f)
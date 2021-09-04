# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open("./gb_labs/lab_5/task_6_file", "r") as f:
    content = f.readlines()
print(content)

list_of_keys = []
list_of_values = []
parsed_list_of_values = []

for i in range(len(content)):
    list_of_keys.append(content[i].split(": ")[0])
    list_of_values.append(content[i].split(": ")[1])
#print(list_of_keys)
#print(list_of_values)

for el in list_of_values:
    for str in el.split():
        parsed_list_of_values.append(str.split("(",1)[0])
#print(parsed_list_of_values)

for i in range(len(parsed_list_of_values)):
    if parsed_list_of_values[i] == "-": parsed_list_of_values[i] = 0
    parsed_list_of_values[i] = int(parsed_list_of_values[i])
list_of_values.clear()
#print(parsed_list_of_values)

for i in range(0, len(parsed_list_of_values), 3):
#    list_of_values.append([parsed_list_of_values[i], parsed_list_of_values[i + 1], parsed_list_of_values[i + 2]])
     list_of_values.append(parsed_list_of_values[i] + parsed_list_of_values[i + 1] + parsed_list_of_values[i + 2])
parsed_list_of_values.clear()
#print(list_of_values)

lessons_dict = dict(zip(list_of_keys, list_of_values))
print(lessons_dict)

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open("./gb_labs/lab_5/task_3_file", "r") as f:
    content = f.readlines()
print(content)

workers_dict = {}
low_salary_list = []

for el in content:
    workers_dict.update({el.split()[0]: float(el.split()[1])})
    if float(el.split()[1]) < 20: low_salary_list.append(el.split()[0])
#print(workers_dict)
print(f"Low salary workers: {low_salary_list}")
print(f"Avarage workers salary is {round(sum(workers_dict.values()) / len(workers_dict.items()),2)}")

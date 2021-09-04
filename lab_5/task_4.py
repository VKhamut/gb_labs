# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

with open("./gb_labs/lab_5/task_4_file", "r") as f:
    content = f.readlines()
print(content)

with open("./gb_labs/lab_5/task_4_file_w", "w") as f:
    for el in content:
        print(el)
        elements = el.split(" - ")
        if elements[0] == "One": elements[0] = "Один"
        if elements[0] == "Two": elements[0] = "Два"
        if elements[0] == "Three": elements[0] = "Три"
        if elements[0] == "Four": elements[0] = "Четыре"
#       print(elements)
        f.writelines(f"{elements[0]} - {elements[1]}")

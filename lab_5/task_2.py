# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open("./gb_labs/lab_5/task_2_file", "r") as f:
    content = f.readlines()

print(content)
print("Lines in file:", len(content))

for el in content:
    print(f"{content.index(el) + 1} line conains {len(el.split())} words")
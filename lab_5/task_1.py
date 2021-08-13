# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open("./task_1_file.txt", "w") as f:
    while True:
        new_line = input("Enter new line or press Enter to finish: ")
        if new_line == "": break
        print(new_line, file=f)

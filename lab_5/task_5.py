# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

with open("./gb_labs/lab_5/task_5_file_w", "w") as f:
        for i in range(20):
            f.write(f"{int(random.random() * 100)} ")

with open("./gb_labs/lab_5/task_5_file_w", "r") as f:
        numbers = f.read().split()
for el in range(len(numbers)): 
    numbers[el] = int(numbers[el])
print(sum(numbers))
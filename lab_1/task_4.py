#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
print("\ntask_4\n")
num = int(input("Enter integer number: "))
big_num = 0
while num:
    if num % 10 > big_num: big_num = num % 10
    num = num // 10
print("The biggest digit is %d" % big_num)
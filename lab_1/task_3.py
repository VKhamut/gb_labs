#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
print("\ntask_3\n")
n = str(input("Enter number: "))
print(int(n) + int(n + n) + int(n + n + n))
# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

sum = 0
flag = True
while flag:
    numbers = input("Enter your number/numbers and separate it with spaces: ").split()
    for el in numbers:
        try:
          el = int(el)
          sum = sum + el
        except ValueError:
            print("Non number symbol detected. Program is terminated")
            flag = False
            break
    print(sum)

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
list_2 = []
list_2_len = int(input("Enter list lenght: "))
i = 0
while i < list_2_len:
    list_2.append(input("Enter %d element of list: " % (i + 1)))
    i += 1 
print(list_2)

i = 0
while i < (list_2_len - 1):
    tmp = list_2[i]
    list_2[i] = list_2[i + 1]
    list_2[i + 1] = tmp
    i = i + 2
print(list_2)
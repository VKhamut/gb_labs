# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
new_list = [45, 'new', 2, 2.34, 'last', False, 6]
print(new_list)
for el in new_list: print(new_list.index(el) + 1, "element:", type(el))

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

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
month = int(input("Enter number of month (1-12): "))
month_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autmun', 'autmun', 'autmun', 'winter']
print("This is ", month_list[month - 1])

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
str = input("Enter your sentence: ").split()
print(str)
i = 1
for el in str:
   if len(el) > 10: el = el[0:9] 
   print(i, "-", el, "\n")
   i += 1

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
rating_list = [20, 14, 7, 3, 3, 2]
print(rating_list)
#last occurance of element in list e.g. last index:
len(rating_list) - rating_list[::-1].index(3) - 1
new_num = 1
while (new_num):
   new_num = int(input("Enter new natural number or 0 for exit: "))
   if new_num == 0: break
   if new_num >= rating_list[0]:
       rating_list.insert(0, new_num)
       print(rating_list)
       continue
   for el in reversed(rating_list):
       if new_num <= el: 
           rating_list.insert(len(rating_list) - rating_list[::-1].index(el), new_num)
           break
   print(rating_list)


# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
goods = []
tmp_dic = {}
i = 1

while input("\nWanna add new item?\nYes - Enter 1\nNo - Press Enter\n"):
    while input("\nWanna add new feature of item?\nYes - Enter 1\nNo - Press Enter\n"):
        k = input("Please input a key: ") 
        v = input("Plesse input a value: ") 
        tmp_dic.update({k:v}) #making temporary dic with Nth item features
    goods.append((i, tmp_dic.copy())) # IMPORTANT: use .copy() method for append tuple with dict
    tmp_dic.clear()
    i += 1
print(goods, "\n")

#use predefined dict for part two of the task
#goods_test = [(1, {'view': 'printer', 'price': '200', 'count': '2', 'color' : 'RGB'}), (2, {'view': 'computer', 'type': 'PC', 'count': '3', 'price': '500', 'color' : 'red'}), (3, {'view': 'monitor', 'type': 'LCD', 'count': '0', 'price': '900', 'size' : '26inch'})]
#print(goods_test, "\n")

analitics_dic = {}
temp_list_val = []

for el in goods:
    for key in el[1].keys():
        for el_1 in goods: # making one more pass of all tuples in 'goods' list to find all values with specified key and add them to temp list
            if el_1[1].get(key) != None: temp_list_val.append(el_1[1].get(key))
        analitics_dic.update({key:temp_list_val.copy()}) # add iterated key and list of valus to dict
        temp_list_val.clear()
print(analitics_dic.items())
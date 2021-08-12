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
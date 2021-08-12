# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
   tmp_list = sorted([num_1, num_2, num_3])
   return(tmp_list[-1] + tmp_list[-2])
    
print(my_func(8, 3, 6))
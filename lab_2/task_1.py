# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
new_list = [45, 'new', 2, 2.34, 'last', False, 6]
print(new_list)
for el in new_list: print(new_list.index(el) + 1, "element:", type(el))
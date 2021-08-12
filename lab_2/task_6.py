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

#use predefined dict for testing second part of the task
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
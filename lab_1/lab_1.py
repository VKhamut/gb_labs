#1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
print("\ntask_1\n")
var1 = int(input("Enter digit: "))
print(var1)

var2 = str(input("Enter string: "))
print(var2)

my_list = list(['1', '2', '4', '5'])
print(my_list)
my_list.append(input("Enter something for adding to list "))
print(my_list)

#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
print("\ntask_2\n")
time = int(input("Enter time in seconds: "))
time_h = time//3600
time_m = (time - time_h * 3600)//60
time_s = time - time_h * 3600 - time_m * 60 
print("Time is: %.2d:%.2d:%.2d" % (time_h, time_m, time_s))

#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
print("\ntask_3\n")
n = str(input("Enter number: "))
print(int(n) + int(n + n) + int(n + n + n))

#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
print("\ntask_4\n")
num = int(input("Enter integer number: "))
big_num = 0
while num:
    if num % 10 > big_num: big_num = num % 10
    num = num // 10
print("The biggest digit is %d" % big_num)

#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
print("\ntask_5\n")
revenue, costs = input("Enter company revenue and costs  with space separation\n").split()
revenue, costs = [int(revenue), int(costs)]
if revenue > costs: 
    print("Company have profit")
    print("Profitable is ", round((revenue - costs) / revenue * 100), " %")
else:
    print("Company have NO profit")
employee = int(input("Enter employee count: "))
print("Profit per employee is: ", round((revenue - costs) / employee, 2))

#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
print("\ntask_6\n")
a, b = input("Enter a and b with space separation\n").split()
a, b = [int(a), int(b)]
i = 1
while a < b:
    a = a * 1.1
    i += 1
print("Number of day: ", i)  

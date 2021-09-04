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
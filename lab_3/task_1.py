# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def devide_of_two(numerator, denominator):
   try: 
       #numerator = float(input("Enter numerator: "))
       #denominator = float(input("Enter denominator: "))
       return numerator / denominator
   except ZeroDivisionError: 
       return "Zero denominator is prohibited\n"
           
print(round(devide_of_two(float(input("Enter numerator: ")),float(input("Enter denominator: "))),2))
print(devide_of_two(8,2))
#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
print("\ntask_2\n")
time = int(input("Enter time in seconds: "))
time_h = time//3600
time_m = (time - time_h * 3600)//60
time_s = time - time_h * 3600 - time_m * 60 
print("Time is: %.2d:%.2d:%.2d" % (time_h, time_m, time_s))
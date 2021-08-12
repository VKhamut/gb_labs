# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def personal_data(f_name, s_name, b_year, city, e_mail, phone):
   res = str(f_name) + " " + str(s_name) + " " + str(b_year) + " " + str(city) + " " + str(e_mail) + " " + str(phone)
   return res
    
print(personal_data(
   phone = 321, 
   city = 'krsk', 
   e_mail = 'me@mail.ru', 
   s_name = 'Petrov', 
   f_name = 'Peter', 
   b_year = 2000))
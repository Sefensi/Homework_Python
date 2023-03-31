# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def to_degree(a,b):
    if b == 0:
        return 1
    else:
        return a * to_degree(a, b - 1)
    
number = int(input("Введите число: "))
degree_of_number = int(input("Введите степень, в которую возведется число: "))
print(to_degree(number, degree_of_number))
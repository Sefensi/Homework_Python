# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
n = int(input("Введите число N: "))
i = 0
while 2 ** i <= n:
    print(f"степень 2 от {i} = {2 ** i}")
    i += 1
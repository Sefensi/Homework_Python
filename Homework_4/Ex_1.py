# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
import random


range_of_numbers = int(input("Введите интервал списков: "))
len_of_list = int(input("Введите длину первого набора: "))
len_of_list2 = int(input("Введите длину второго набора: "))


list_1 = [random.randint(-range_of_numbers, range_of_numbers) for x in range(len_of_list)]
set_1 = set(list_1)
print(set_1)
list_2 = [random.randint(-range_of_numbers, range_of_numbers) for x in range(len_of_list2)]
set_2 = set(list_2)
print(set_2)
new_k = set_1 & set_2
kool = list(new_k)
kool.sort()
for i in kool:
    print(i, end=' ')
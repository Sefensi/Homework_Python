# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random


count_of_numbers = int(input("Введите длину массива: "))
list_of_numbers = []

for i in range(count_of_numbers):
    list_of_numbers.append(random.randint(-count_of_numbers, count_of_numbers))
    #массив создаю через рандом чисел, 
    #потому что в случае массива из i++, смысла никакого не будет, число X всегда будет равно 1
print(list_of_numbers)

finding_number = int(input("Введите число для поиска ближайшего к X: "))
final_number = 0
count_of_final = 0
list_of_finals = []
max_diff = count_of_numbers 
for i in range(len(list_of_numbers)):
    difference = abs(list_of_numbers[i] - finding_number)
    if not difference > max_diff:
        if max_diff == difference:
            list_of_finals.append(list_of_numbers[i])
        else:
            list_of_finals = []
            list_of_finals.append(list_of_numbers[i])
        max_diff = difference
        final_number = list_of_numbers[i]
print(final_number)  

if len(list_of_finals) > 1:
    print(f"Ближайшие к X числа из строки: {list_of_finals} ")
else:
    print(f"Ближайшее число к X = {final_number} ")
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random


count_of_numbers = int(input("Введите длину строки: "))
list_of_numbers = []
count_of_OREL = 0  # OREL=0
count_of_RESHKA = 0  # RESHKA=1
for i in range(count_of_numbers):
    list_of_numbers.append(random.randint(0, count_of_numbers))
    # массив создаю через рандом чисел,
    # потому что в случае массива из i++, смысла никакого не будет, число X всегда будет равно 1
print(list_of_numbers)

find_the_number = int(input("Введите число для поиска в строке: "))
count_of_numbers = 0

for number in list_of_numbers:
    if int(number) == find_the_number:
        count_of_numbers += 1

print(f"Цифра {find_the_number} встречается в строке = {count_of_numbers} раз(а)")


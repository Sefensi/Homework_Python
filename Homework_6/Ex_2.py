# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

list_of_numbers = [int(num) for num in input("Введите элементы массива: ").split(", ")]
lower_limit = int(input("Нижняя граница диапазона для поиска: "))
upper_limit = int(input("Верзхняя граница диапазона для поиска: "))
resulting_list = []

for index in range(len(list_of_numbers)):
    if lower_limit <= list_of_numbers[index] <= upper_limit:
        resulting_list.append(index)
        
print(resulting_list)
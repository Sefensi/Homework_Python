# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_element_of_list = int(input("Введите первый элемент: "))
diff_of_elements = int(input("Введите шаг прогрессии: "))
count_of_elements = int(input("Введите количество элементов прогрессии: "))

last_element_of_list = first_element_of_list + (count_of_elements - 1)  * diff_of_elements
final_list = [num for num in range(first_element_of_list, last_element_of_list + 1, diff_of_elements)]

print(*final_list)
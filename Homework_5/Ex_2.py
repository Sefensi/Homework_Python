# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

def make_a_summ(a, b):
    if a == 0:
        return b
    return make_a_summ(a-1, b+1)

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
print(make_a_summ(first_number, second_number))

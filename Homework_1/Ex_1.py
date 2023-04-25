# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

numbers = input("Введите число: ")
print(numbers)
second_summary = numbers[0] + numbers[1] + numbers[2]
print(second_summary)
summary = (int(numbers[0]) + int(numbers[1]) + int(numbers[2]))
print(summary)

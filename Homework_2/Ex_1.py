# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random


count_of_coins = int(input("Введите количество монет: "))
list_of_coins = []
count_of_OREL = 0 #OREL=0
count_of_RESHKA = 0 #RESHKA=1
for i in range(count_of_coins):
    list_of_coins.append(random.randint(0,1))
print(list_of_coins)
for number in list_of_coins:
    if number == 0:
        count_of_OREL +=1
    else:
        count_of_RESHKA +=1
if count_of_OREL >= count_of_RESHKA:
    print(f"Перевернем монеты с решкой наверху {count_of_RESHKA} раз")
else:
    print(f"Перевернем монеты с орлом наверху {count_of_OREL} раз")
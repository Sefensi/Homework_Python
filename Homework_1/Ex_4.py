# Задача 8: Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

number1 = int(input("Введите длину шоколадки: "))
number2 = int(input("Введите ширину шоколадки: "))
number3 = int(input("Введите желаемое количество долек: "))
if (number3%number1 == 0 or number3%number2 == 0) \
    and (number1*number2) >= number3:
    print("Yes")
else:
    print("No")

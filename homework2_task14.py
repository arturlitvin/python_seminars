# Задача 14: Требуется вывести все целые степени двойки  (т.е. числа вида 2^k), не превосходящие числа N.

# 10 -> 1 2 4 8




m = 2 # int(input('Введите число, которое хотите возвести в степень: '))
n = int(input('Введите число - ограничитель: '))
x = None
for i in range(0, n):
   x = m ** i
   if x <= n:
       print(f'{i}-я степень числа {m}: {x}')
   else:
       break

    
   

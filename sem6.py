# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

# Вывод:
# 3 3 2 12


# n = int(input('Введите кол-во элементов первого массива: '))
# m = int(input('Введите кол-во элементов второго массива: '))
# my_list_n = []
# my_list_m = []
# for i in range(n):
#     x = int(input(f'Введите элемент № {i+1} первого массива: '))
#     my_list_n.append(x)
# for i in range(m):
#     x = int(input(f'Введите элемент № {i+1} второго: '))
#     my_list_m.append(x)

# for number in my_list_n[:]:
#     if number in my_list_m:
#         my_list_n.remove(number)

# print(my_list_n)

# n = int(input('Введите кол-во элементов первого массива: '))
# my_list_n = list(map(int, input().split()))
# m = int(input('Введите кол-во элементов второго массива: '))
# my_list_m = list(map(int, input().split()))
# # for i in range(n):
# #     flag = False
# #     for j in range(m):
# #         if my_list_n[i] == my_list_m[j]:
# #             flag = True
# #             break
# #         if not flag:
# #             print(my_list_m[i], end=' ')
# my_list_m = set(my_list_m)
# for i in range(n):
#     if my_list_n[i] not in my_list_m:
#         print(my_list_n[i], end=' ')

# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: 
# 5 
# 1 2 3 4 5
# Вывод: 
# 0 
# Ввод:
# 5
# 1 5 1 5 1
# Вывод:
# 2
# (каждое число вводится с новой строки)

# Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a= int(input("Введите значение 1-го элемента прогрессии: "))
d=int(input("Введите шаг (разность элементов): "))
n=int(input("Введите количество элементов: "))
array = []
# [a + (i - 1) * d for i in range(a, n * 2 + 1, d)]
# print(array)



for i in range(a, (a+(n-1)*d)+1, d):
    array.append(i)
print(array)

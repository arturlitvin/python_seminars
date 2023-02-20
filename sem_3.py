# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# Эффективное решение
# list_1 = [1, 1, 2, 7,7,2,3,4,5,6,7,8,898,54,34,56,23213,55]
# print(len(set(list_1)))

# менее Эффективное решение
# list_1 = set(list_1)
# # list_1 = list(list_1)
# # x = 0
# # for i in list_1:
# #     x+=1
# # print(x)
# print(len(list_1))

# Теперь "неэффективное" решение с урока

# list_1 = [1, 1, 2, 0, -1 , 3, 4, 4]
# uniq = []
# for element in list_1:
#     if element not in uniq:
#         uniq.append(element)
# print(uniq)
# print(len(uniq))

# list_1 = list(map(int, input("введите числа через пробел: ").split(" ")))
# print(list_1)

# # Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# array = [1, 2, 3, 4, 5]
# k = int(input('Введите число от 1 до 5 на которое хотите сдвинуть список: '))
# print(array[(-k+1):]+array[:k]) # - не универсальное решение, работает только с 3-кой

# new_array = []

# for i in range(k, len(array)):
#     new_array.append(array[i])
# for i in range(0, k):
#     new_array.append(array[i])
# print(new_array)

# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# my_dict = {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VII": "S005", "V":"S009 ","VIII":" S007 "}
# print((my_dict))
# my_dict_1 = []
# for v in my_dict.values():
#     my_dict_1.append(v)
# print(set(my_dict_1))

# my_dict=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": "S005"}, {"V":" S009 "}, {"VIII":"S007"}]
# print(my_dict)
# my_dict_1 = set()
# for element in my_dict:
#     for value in element.values():
#         my_dict_1.add(value)
# print(my_dict_1)

# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# arr = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1, len(arr)):
#     if arr[i-1] < arr[i]:
#         count += 1
# print(count)
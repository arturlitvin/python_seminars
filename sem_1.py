# Задача 1 За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# import math

# n = int(input('Введите расстояние за день: '))
# m = int(input('Введите общее расстояние: '))
# d = (m / n)
# # print(d)
# print(math.ceil(d))

# n = int(input('Введите расстояние за день: '))
# m = int(input('Введите общее расстояние: '))
# d = (m//n+(n % m != 0))
# print(d)

# n = int(input('Введите расстояние за день: '))
# m = int(input('Введите общее расстояние: '))
# d = (-(-m//n))
# print(d)

# n = int(input('Введите расстояние за день: '))
# m = int(input('Введите общее расстояние: '))
# d = (m+n-1)//n
# print(d)

# Задача 3
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a = int(input('Введите колличество учеников в первом классе: '))
# b = int(input('Введите колличество учеников во втором классе: '))
# c = int(input('Введите колличество учеников в третьем классе: '))
# d = a+b+c
# if d % 2 == 0:
#     d = d/2
# else: d = d/2 + 0.5

# print(int(d))

# a = int(input('Введите колличество учеников в первом классе: '))
# b = int(input('Введите колличество учеников во втором классе: '))
# c = int(input('Введите колличество учеников в третьем классе: '))
# d = a+b+c
# if d % 2 == 0:
#     d = d/2
# else: d = (d+1) / 2

# print(int(d))

# import math
# a = int(input('Введите колличество учеников в первом классе: '))
# b = int(input('Введите колличество учеников во втором классе: '))
# c = int(input('Введите колличество учеников в третьем классе: '))
# d = a+b+c
# if d % 2 == 0:
#     d = d/2
# else: d = math.ceil(d/2)


# a = int(input('Введите колличество учеников в первом классе: '))
# if a % 2 != 0:
#     a = a+1
# b = int(input('Введите колличество учеников во втором классе: '))
# if b % 2 != 0:
#     b = b+1
# c = int(input('Введите колличество учеников в третьем классе: '))
# if c % 2 != 0:
#     c = c+1
# d = (a+b+c)/2
# print(d)

# a = int(input('Введите колличество учеников в первом классе: '))
# b = int(input('Введите колличество учеников во втором классе: '))
# c = int(input('Введите колличество учеников в третьем классе: '))
# d = (a+(a%2!=0) +b+(b%2!=0)+c+(c%2!=0))//3
# print(d)

# a = int(input('Введите колличество учеников в первом классе: '))
# b = int(input('Введите колличество учеников во втором классе: '))
# c = int(input('Введите колличество учеников в третьем классе: '))
# d = (a+(a%2!=0) +b+(b%2!=0)+c+(c%2!=0))//3
# d = (a+1)//2+(b+1)//2+(c+1)//2
# print(d)

# Задача 5:Вагоны в электричке пронумерованы натуральными числами,
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
# а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# i = int(input('Введите номер вагона с головы состава: '))
# j = int(input('Введите номер вагона с хвоста: '))
# if i == j:
#     x = 'Недостаточно информации'
# else:
#     x = i+j-1
# print(f'Кол-во вагонов в составе: {x}')

# Дано натуральное число. 
# Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. 
# Напомним, что в соответствии с григорианским календарем, год является високосным, 
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.


# year = int(input('Введите год, который хотите проверить на високосность: '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('YES')
# else: print('No')
# # Input: 2016
# # Output: YES
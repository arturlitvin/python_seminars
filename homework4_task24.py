# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9


n = int(input('Введите кол-во кустов: '))
berr = []

for i in range(n):
    x = int(input(f'Введите кол-во ягод на кусте № {i + 1}: '))
    berr.append(x)

print(berr)
m = int(input('Введите номер "некоторого" куста, к которому направился комбайн: '))
if m == 1 or n == 3:
    max_berr = berr[0] + berr[1] + berr[2]
elif m == n:
    max_berr = berr[-1] + berr[-2] + berr[-3]
elif m == n - 1:
    if berr[m] > berr[m - 3]:
        max_berr = berr[m] + berr[m - 2] + berr[m - 1]
    else:
        max_berr = berr[m - 3] + berr[m - 2] + berr[m - 1]
elif m == 2:
    if berr[0] > berr[3]:
        max_berr = berr[0] + berr[1] + berr[2]
    else:
        max_berr = berr[3] + berr[1] + berr[2]
else:
    if (berr[m - 1] + berr[m - 2] + berr[m - 3]) >= (berr[m - 1] + berr[m - 2] + berr[m]) and (
            berr[m - 1] + berr[m - 2] + berr[m - 3]) >= (berr[m - 1] + berr[m] + berr[m + 1]):
        max_berr = berr[m - 1] + berr[m - 2] + berr[m - 3]
    elif (berr[m - 1] + berr[m - 2] + berr[m]) >= (berr[m - 1] + berr[m - 2] + berr[m - 3]) and (
            berr[m - 1] + berr[m - 2] + berr[m]) >= (berr[m - 1] + berr[m] + berr[m + 1]):
        max_berr = berr[m - 1] + berr[m - 2] + berr[m]
    else:
        max_berr = berr[m - 1] + berr[m] + berr[m + 1]
        
print('Максимальное кол-во ягод, которые может собрать комбайн: ', max_berr)

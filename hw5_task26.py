# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 ()


def degree(a, b):
    if b == 0:
        return 1
    return a*(degree(a, b-1))


a = int(input('Введите целое число: '))
b = int(input('Введите интересующую Вас степень, ранее введённого числа: '))
print(f"Число {a} в {b}-й степени  равно {degree(a,b)}")
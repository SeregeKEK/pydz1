#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
#является ли этот день выходным.
import math


def Zadacha1():
    a = int(input('введите число от 1 до 7: '))
    if a < 1 or a > 7:
        print('Введено неверное число')
    elif a > 5 and a < 8:
        print('Выходной')
    else:
        print('Рабочий')

# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def Zadacha2():
    x = int(input('введите число x: '))
    y = int(input('введите число y: '))
    z = int(input('введите число z: '))
    if not(x or y or z) == (not x and not y and not z):
        print('True')
    else:
        print('False')


# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
def Zadacha3():
    x = int(input('введите число x: '))
    y = int(input('введите число y: '))
    if x > 0 and y > 0:
        print('1-я четверть')
    elif x < 0 and y > 0:
        print('2-я четверть')
    elif x > 0 and y < 0:
        print('3-я четверть')
    elif x < 0 and y < 0:
        print('4-я четверть')
    elif x == 0 or y == 0:
        print('Введено неверное число') 

# Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).
def Zadacha4():
    num = int(input('введите число от 1 до 4: '))
    if num == 1:
        print('Диапозон x > 0 and y > 0')
    elif num == 2:
        print('Диапозон x < 0 and y > 0')
    elif num == 3:
        print('Диапозон x > 0 and y < 0')
    elif num == 4:
        print('Диапозон x < 0 and y < 0')
    elif num < 1 or num > 4:
        print('Введено неверное число')

# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
def Zadacha5():
    ax = float(input('Введите A(x): '))
    ay = float(input('Введите A(y): '))
    bx = float(input('Введите B(x): '))
    by = float(input('Введите B(y): '))
    print(f'Расстояние между точками = {round(((bx - ax) ** 2 + (by - ay) ** 2), 5)**0.5}')


#Zadacha1()
#Zadacha2()
#Zadacha3()
#Zadacha4()
Zadacha5()
# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
def Zadacha1():
    num = float(input("Введите число: "))
    num_string = str(num)
    num_string = num_string.replace('.', '')
    list_string = list(num_string)
    list_num = map(int, list_string)
    my_sum = sum(list_num)
    print(f'Сумма цифр равна: {my_sum}')

# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.
def Zadacha2():
    n = int(input('Введите число: '))
    mult = 1
    for i in range(1, n+1):
        mult *= i
        print(mult, end=' ')


# Задайте список из n чисел последовательности 
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.
def Zadacha3():
    n = int(input('Введите число: '))
    sum = 0
    for i in range(1, n+1):
        res = (1+1/i)**i
        res = round(res)
        print(f'{i}: {res} ')
        sum += res
    print(f'Сумма: {sum}')


# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
def Zadacha4():
    number = int(input('Введите число: '))
    list1 = list()
    for i in range(-number, number + 1):
        list1.append(i)
    numberOne = int(input('Введите 1-ю позицию: '))
    numberTwo = int(input('Введите 2-ю позицию: '))
    res = list1[numberOne - 1] * list1[numberTwo - 1]
    print(list1)
    print(res)


# Реализуйте алгоритм перемешивания списка. 
# Без ф-и shaffle из модуля random
def Zadacha5():
    import random
    list1 = list()
    rangeList = int(input('Введите число: '))
    for i in range(rangeList + 1):
        list1.append(i)
    print(*list1)
    print(*random.sample(list1, rangeList + 1))



#Zadacha1()
#Zadacha2()
#Zadacha3()
#Zadacha4()
Zadacha5()

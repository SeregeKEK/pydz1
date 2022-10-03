# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
def Zadacha1():
    my_list = [2, 3, 5, 9, 3]
    my_sum = 0
    for i in range(1, len(my_list), 2):
        my_sum += my_list[i]
    print(my_sum)

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def Zadacha2():  
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    revList = myList[::-1]
    list1 = myList[:int(len(myList) / 2)]
    list2 = revList[:int(len(myList) / 2)]
    
    mult = list()
    for index in range(len(list1)):
        mult.append(int(list1[index] * list2[index]))
    print('Произведение пар чисел', mult)


# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
def Zadacha3():  
    from random import uniform
    ListRange = int(input("Введите длину списка: "))
    myList = [round(uniform(0, value), 2) for value in range(1, ListRange + 1)]
    print(myList)

    maxVal = 0
    minVal = 1
    for value in myList:
        value = round(value % 1, 2)
        if value < minVal:
            minVal = value
        if value > maxVal:
            maxVal = value
    print( 
        'Разница между максимальным и минимальным элементами: ', 
        round(maxVal - minVal, 2)
    )


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
def Zadacha4():
    number = int(input("Введите число: "))
    print(bin(number)[2:])


# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
def Zadacha5():
    num = int(input('введите число - '))
    numOne = 1
    numTwo = 1
    fiboNum = []
    for _ in range(num):
        fiboNum.append(numOne)
        numOne, numTwo = numTwo, numOne + numTwo
    numOne = 0
    numTwo = 1
    for _ in range(num+1):
        fiboNum.insert(0, numOne)
        numOne, numTwo = numTwo, numOne - numTwo
    print(fiboNum)



# Zadacha1()
# Zadacha2()
# Zadacha3()
# Zadacha4()
Zadacha5()

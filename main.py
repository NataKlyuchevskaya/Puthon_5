'''
def stepen (x, y):
    if y == 0:
        return 1
    else:
        return x * stepen (x, y - 1)

    a = int(input("Введите число А"))
    b = int(input("Введите число В"))
    print(stepen(a, b))

def summa_recursion(a, b):
    if a == 0:
        return b
    else:
        return summa_recursion(a - 1, b + 1)
'''


'''Задача 30: Заполните массив элементами арифметической прогрессии.
    Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
    Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
    Каждое число вводится с новой строки 
    Ввод: 7 2 5
    Вывод: 7 9 11 13 15'''
'''
a1 = 7
d = 2
n = 5
for i in range(a1, n):
    a[n]= a1(n-1) + d
    print(a[n], end = ' ') 
'''

'''Задача 32: Определить индексы элементов массива (списка),
 значения которых принадлежат заданному диапазону 
 (т.е. не меньше заданного минимума и не больше заданного максимума)'''

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_2 = []
max = 10
min = 6
for i in range(len(lst_1)):
    if list_1[i] >= min and list_1[i] <= max:
         list_2.append(i)
print(list_2)









    




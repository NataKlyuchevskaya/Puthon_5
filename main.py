def stepen (x, y):
    if y == 0:
        return 1
    return x * stepen (x, y - 1)

    a = int(input("Введите число А"))
    b = int(input("Введите число В"))
    print(stepen(a, b))

def summa_recursion(a, b):
    if a == 0:
        return b
    else:
        return summa_recursion(a - 1, b + 1)




    




#Дан список A размера N и целые числа K и L (1 < K < L < N). Переставить в обратном
#порядке элементы списка, расположенные между элементами AK и AL, включая эти
#элементы.
access = 1
try:
    n = int(input("длина списка "))
    список = []
    if n <= 1:
        print("не верное значение")
        access = 0
    if access == 1:
        while n != 0:
            n -= 1
            chislo = int(input("число "))
            список.append(chislo)
        список.insert(0,"k")
        список.append("x")
        print(список)
        список.reverse()
        print(список)
    else:
        print("не верное значение")
except ValueError:
    print("не верное значение")
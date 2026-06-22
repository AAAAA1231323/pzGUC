#Вариант 5.

#1.Из последовательности на n целых чисел создать новую последовательность, в
#которой каждый последующий элемент равен квадрату суммы двух соседних элементов.

try:
    kollvo = int(input("kollvo "))
    if kollvo >= 3:
        a = [int(input()) for _ in range(kollvo)]
        b = [(a[i-1]**2 + a[i+1]**2) for i in range(1,kollvo-1)]
        pervoe = a[1]**2
        vtoroe = a[kollvo-1]**2
        b.append(vtoroe)
        b.insert(0,pervoe)
        print(b)
    else:
        print("не может быть меньше 3 ")
except ValueError:
    print("ошибка")

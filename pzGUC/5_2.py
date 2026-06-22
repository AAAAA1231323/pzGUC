#2  Описать функцию DigitCountSum(K, C, S), находящую количество C цифр целого
#положительного числа K, а также их сумму S (K — входной, C и S — выходные
#параметры целого типа). С помощью этой функции найти количество и сумму цифр
#для каждого из пяти данных целых чисел.
t = 5
def funk(chislo):
    try:
        c_chislo = len(chislo)
        print("количество: ", c_chislo)
        chislo_int = int(chislo)
        summa_cifr = 0
        while c_chislo != 0:
            цифра = chislo_int % 10
            print(цифра)
            summa_cifr += цифра
            chislo_int //= 10
            c_chislo -= 1
        print("Сумма цифр:", summa_cifr)
    except ValueError:
        print("Ошибка")

while t != 0:
    chislo = input("Введите число: ")
    funk(chislo)
    t -= 1
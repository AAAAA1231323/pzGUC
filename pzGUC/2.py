import sys

v1 = int(input())

try:
    v2 = int(input("скорость 2 машины: "))
except ValueError:
    print("Ошибка: введены не числа")
    sys.exit()

if v1 <= 0:
    print("скорость 1 машины:", v1)

try:
    S = int(input("Расстояние между 2 машинами: "))
except ValueError:
    print("Ошибка: введены не числа")
    sys.exit()

try:
    T = int(input("Время: "))
except ValueError:
    print("Ошибка: введены не числа")
    sys.exit()

while T > 0:
    T = T - 1
    S = S - (v1 + v2)
    if T == 0:
        break

print("итоговое расстояние: ", S)

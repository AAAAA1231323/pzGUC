#1. Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1, 0.2, ..., 1 кг
#конфет.

count = 5
co = 1
d1 = 1
try:
    cena = float(input("введите цену 1 кг: "))
except ValueError:
    print("введите число, а не букву")
    d1 = 0
if d1 == 1 and cena >= 0:
    while count != 0:
        count -= 1
        co += 0.2
        print("стоиммость   ", round(co, 1), " кг конфет:  ", round((cena * (co)),1),"  руб")
elif d1 == 1 and cena <= 1:
    print("цена не может быть отрицательной ")
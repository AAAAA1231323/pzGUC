# Дан список размера N. Обнулить все его локальные максимумы (то есть числа,
# большие своих соседей).
coord = 1
try:
    n = int(input("длина "))
    r = n
    spisok = []
    if n >= 0:
        while n != 0:
            n -= 1
            chislo = int(input("\n число "))
            spisok.append(chislo)
        print("\n", spisok)
        while r >= 2:
            if spisok[coord - 1] <= spisok[coord] and spisok[coord + 1] <= spisok[coord] and r >= 3 and spisok[
                coord - 1] != spisok[coord] and spisok[coord + 1] != spisok[coord] and r >= 3:
                spisok[coord] = 0
            r -= 3
            coord += 3

        print("\n", spisok)
    else:
        print("не верное значение ")
except ValueError:
    print("не верное значение ")
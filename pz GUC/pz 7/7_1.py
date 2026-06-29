#Дано целое число N (1 < N < 26). Вывести N последних строчных (то есть маленьких)
#букв латинского алфавита в обратном порядке (начиная с буквы «z»).
try:
    alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","y","z"]
    chislo = int(input("chislo "))
    coord = 24
    coord2 = 0
    if chislo <= 25 and chislo >= 0:
        while coord2 != chislo:
            print(alp[coord-coord2])
            coord2 += 1
    else:
        print("значение введено неверно")
except ValueError:
    print("значение введено неверно")
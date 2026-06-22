#2. Дано целое число N (>0). Используя операции деления нацело и взятия остатка от
#деления, найти количество и сумму его цифр.
N = 12345
count = 0
total_sum = 0

while N > 0:
    digit = N % 10
    total_sum += digit
    count += 1
    N //= 10

print(count, total_sum)

magnit = {'хлеб', 'молоко'}
troyka = {'хлеб', 'сыр', 'масло'}
karusel = {'хлеб', 'сыр'}

print(magnit & troyka & karusel)
print(magnit | troyka | karusel)

colors = {"red", "green", "blue"}
if "yellow" not in colors:
    colors.add("yellow")
print(colors)

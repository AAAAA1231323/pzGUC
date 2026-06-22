# 2. Из предложенного текстового файла (text18-27.txt) вывести на экран его содержимое,
# количество пробельных символов. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив последнюю строку фразой введенной
# пользователем.

with open('text18-27.txt', 'r', encoding='utf-8') as file:
    content = file.read()

print(content)

probeli = 0
for s in content:
    if s == ' ':
        probeli += 1
print('Количество пробельных символов:', probeli)

with open('text18-27.txt', 'r', encoding='utf-8') as file:
    stroki = file.readlines()

fraza = input('Введите свою фразу: ')
stroki[-1] = fraza + '\n'

with open('text18-27_new.txt', 'w', encoding='utf-8') as new_file:
    new_file.writelines(stroki)

with open('text18-27_UPPER.txt', 'w', encoding='utf-8') as upper_file:
    upper_file.write(content.upper())

print('Готово')

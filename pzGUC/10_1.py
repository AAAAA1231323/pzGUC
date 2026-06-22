# 1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Элементы первого и второго файлов:
# Элементы первого файла, присутствующие во втором:
# Элементы второго файла, присутствующие в первом:
# Количество элементов:
# Количество отрицательных элементов:
# Количество положительных элементов:





f1 = open('file1.txt', 'w')
f1.write('-10 15 3 -8 20 5 -1')
f1.close()
f2 = open('file2.txt', 'w')
f2.write('5 -8 100 3 -50')
f2.close()




f1 = open('file1.txt')
k1 = f1.read().split()
for i in range(len(k1)):
    k1[i] = int(k1[i])
f1.close()
f2 = open('file2.txt')
k2 = f2.read().split()
for i in range(len(k2)):
    k2[i] = int(k2[i])
f2.close()





v_pervom = []
for x in k1:
    if x in k2:
        v_pervom.append(x)

vo_vtorom = []
for x in k2:
    if x in k1:
        vo_vtorom.append(x)

vse = k1 + k2
otr, pol = 0, 0
for x in vse:
    if x < 0:
        otr += 1
    if x > 0:
        pol += 1





res = open('result.txt', 'w', encoding='utf-8')
res.write('Элементы первого и второго файлов: ' + str(k1) + ' ' + str(k2) + '\n')
res.write('Элементы первого файла, присутствующие во втором: ' + str(v_pervom) + '\n')
res.write('Элементы второго файла, присутствующие в первом: ' + str(vo_vtorom) + '\n')
res.write('Количество элементов: ' + str(len(vse)) + '\n')
res.write('Количество отрицательных элементов: ' + str(otr) + '\n')
res.write('Количество положительных элементов: ' + str(pol) + '\n')
res.close()
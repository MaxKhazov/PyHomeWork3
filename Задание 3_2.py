# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random


n = int(input('Введите количество элементов в списке: '))
mult = 0
list = []
for i in range(1, n+1):
    list.append(random.randint(1, 10))

for x in list:
    i = 0
    while i < n/2:
        mult = list[i]*list[n-1-i]
        i += 1
        print(mult)
        # print(i)
print(list)

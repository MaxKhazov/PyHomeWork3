# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random


n = int(input('Введите количество элементов в списке больше двух: '))
sum = 0
list = []
for i in range(1, n+1):
    list.append(random.randint(1, 100))

i = 0
for x in list:
    if i % 2 == 1:
        sum += x
    i = i + 1
print(list)
print(sum)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def fibpos(n):
    if n in [1,2]:
        return 1
    else:
        return fibpos(n-1) + fibpos(n-2)

def fibneg(n):
    if n in [1,2]:
        return -1
    else:
        return -fibneg(n-1) - fibneg(n-2)

list = []
for e in range (1, 10):
    list.append(fibneg(e))
for e in range (1,10):
    list.append(fibpos(e))
print(list)

# Здесь я уже не разобрался, как это можно сделать...
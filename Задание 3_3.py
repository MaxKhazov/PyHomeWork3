# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части

a = [1.1, 1.9, 1.4, 1.5]
max = 0
min = 1
for i in a:
    if i%1 > max:
        max = i%1
    if i%1 < min:
        min = i%1
diff = max-min
print(max,'-', min,'=',diff)

#1.	Считать из параметров командной строки одномерный массив, состоящий из N целочисленных элементов.
#2.	Вывести в консоль сумму элементов с четными номерами
#3.	Вывести в консоль произведение элементов с нечетными номерами.
#4.	Поменять местами минимальный и максимальный элементы. Вывести результат в консоль.
from math import prod

A=[]
A = [ int(input('Введите число для массива:')) for i in range(5) # C помощью range можно задать макс количество введенных чисел в нашем случае 5
print('Одномерный массив:', A)
even_nums = []
i: int # # int- позволяет ввести только цельные числа
for i in A: # оператор for используется для перебора элементов последовательности, Оператор "in". Возвращает. True, если значение присутствует в последовательности, иначе возвращает False.
    if i % 2 == 0: #проверяем число на остаток если после деления на 2 по итогу будет равно нулю и не будет остатка то число четное
        even_nums.append(i) #С помощью функции append() мы добавили значение к первому списку even_nums и в следующей строке вывели получившийся список на экран.
summ = sum(even_nums) #c помощью функции sum считаем сумму с четными номерами
even_nums_1 = []
i: int
for i in A:
    if i % 2 != 0: # проверяем число на остаток если после деления на 2 по итогу будет не равно нулю и будет остаток то число нечетное
        even_nums_1.append(i)
proizv = prod(even_nums_1) # с помощью функции prod считаем произведение элементов с нечетными номерами
print('Сумма элементов с четными номерами:', summ)
print('Произведение элементов с нечетными номерами:', proizv)
Smena = A
tMax = Smena.index(max(Smena)) # находим максимальный элемент в массиве
tMin = Smena.index(min(Smena)) # находим минимальный элемент в массиве
Smena[tMax], Smena[tMin] = Smena[tMin], Smena[tMax] # меняем местами минимальный и маскимильный элемент
print('Поменять местами минимальный и максимальный элементы:', Smena)



#4. Считать с клавиатуры непустую произвольную последовательность целых чисел. Найти:
#i. Сумму всех чисел последовательности (решить задачу используя циклическую конструкцию while)
print('Введите числа и дважды нажмите ENTER') # с помощью функции print() выводим на экран значение, переданное внутрь функции.
a = int(input('а-->> '))# с помощью функции input() мы просим пользователя ввести любое целое(int) число которое он захочет
list = []
b = 10
while True: #whileОператор используется для повторного выполнения до тех пор, пока выражение имеет значение true:
    try:#Блок try содержит код, в котором нужно обработать исключения, если они возникнут.
        list.append(a) #С помощью функции append() мы добавили значение к первому списку list и в следующей строке вывели получившийся список на экран.
        b = b + a
        a = int(input('-->> '))
    except: #При возникновении исключения интерпретатор последовательно проверяет в каком из блоков except обрабатывается это исключение.
        break; #Оператор break досрочно прерывает цикл.
print(b)

#ii. Количество всех чисел последовательности (решить задачу используя циклическую конструкцию while)
print('Введите числа и дважды нажмите ENTER')
n = int(input())
count = 0
counter = 0
while n > 0:
    count += n
    n = int(input())
    if n == 0: #c помощью оператора if мы выбираем точно один из наборов, вычисляя выражения одно за другим, пока не будет установлено, что одно из них истинно
        print('Сумма чисел:', count) #Метод count () используется для подсчета того, сколько раз символ или подстрока встречаются в строке
    counter = counter + 1 #подсчитываем элементы, а значениями — их количества, например буква а в тексте была 4 раза
print('Количество чисел:', counter)


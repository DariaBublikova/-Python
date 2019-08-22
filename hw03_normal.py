# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fibonacci_lst = [1, 1]
    fibonacci = ''
    i = 2
    while i < int(m):
        num = fibonacci_lst[i - 2] + fibonacci_lst[i - 1]
        fibonacci_lst.append(num)
        if i in range(n - 1, m):
            fibonacci += str(num) + ' '
        i += 1
    return fibonacci

fibonacci(3, 6)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return origin_list

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_func(function, iterable):
    return (item for item in iterable if function(item) is True)

print(list(filter_func(lambda x: True if x % 3 == 0 else False, [1, 3, 7, 8, 9, 13, 27])))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

x = [int(input('x{} = '.format(x))) for x in range(0,4)]
y = [int(input('y{} = '.format(y))) for y in range(0,4)]

mid_diagonal_1 = [(x[2] + x[0]) / 2, (y[2] + y[0]) / 2]
mid_diagonal_2 = [(x[3] + x[1]) / 2, (y[3] + y[1]) / 2]

if mid_diagonal_1 == mid_diagonal_2:
    print('Точки являются вершинами параллелограмма')
else:
    print('Точки не являются вершинами параллелограмма')
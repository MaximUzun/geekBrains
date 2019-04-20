# Автор Узун М.В.
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    pass
    fibonacci_row = [1, 1]
    for i in range(1, m+1):
        next_element = fibonacci_row[-1] + fibonacci_row[-2]
        fibonacci_row.append(next_element)
    return fibonacci_row[n: m+1]

input("Press Enter")

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    pass
    while True:
        count = 0
        for i in range(len(origin_list)-1):
            if i < len(origin_list):
                if origin_list[i] > origin_list[i+1]:
                    origin_list[i], origin_list[i+1] = origin_list[i+1], origin_list[i]
                    count += 1
        if count == 0:
            break
    return origin_list

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

input("Press Enter")

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_own_filter(func, iter):
    new_iter = []
    for i in iter:
        if func(i) == True:
            new_iter.append(i)
    return new_iter

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
# Признаю - тут гуглил очень сильно

def distance(iter):
    a = iter[0]
    b = iter[1]
    AB = ((a['x'] - b['x']) ** 2 + (a['y'] - b['y']) ** 2) ** 0.5
    return AB

def parallelogram(*iter):
    sides = [[iter[0], iter[1]], [iter[2], iter[3]], [iter[1], iter[2]], [iter[0], iter[3]]]
    sides = list(map(distance, sides))
    print(sides)
    if sides[0] == sides[1] and sides[2] == sides[3]:
        return True
    else:
        return False

A1 = {'x': 5, 'y': 7}
A2 = {'x': 9, 'y': 7}
A3 = {'x': 7, 'y': 12}
A4 = {'x': 13, 'y': 12}

parallelogram(A1, A2, A3, A4)

input("Press Enter")
# Автор - Узун Максим Владимирович
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
print('Задача 1')
fruit_list = ["яблоко", "банан", "киви", "арбуз"]
for index, value in enumerate(fruit_list, 1):
    print("{}.{:>10}".format(index, value))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print('   ')
print('Задача 2')
numbers_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_list2 = [1, 3, 5, 7, 9]

print(numbers_list1)
print(numbers_list2)

for elements in numbers_list2:
    if elements in numbers_list1:
            numbers_list1.remove(elements)
print(numbers_list1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print('   ')
print('Задача 3')
number_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
number_list2 = []
print(number_list1)

for digit in number_list1:
    if digit % 2 == 0:
        number_list2.append(digit / 4)
    else:
        number_list2.append(digit * 2)
print(number_list2)
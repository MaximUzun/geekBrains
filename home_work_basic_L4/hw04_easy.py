# Автор Узун М.В.
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

origin_list = [random.randint(1, 10) for i in range(7)]

edit_list = [i ** 2 for i in origin_list]

input("Press Enter")

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list1 = ['apple', 'banana', 'cherry', 'fig', 'grape', 'honeydrew', 'lime']
list2 = ['mango', 'peach', 'quince', 'cherry', 'lemon', 'apple', 'fig', 'tomato']

new_list = [i for i in list1 if i in list2]

input("Press Enter")

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

origin_list = [random.randint(-10, 30) for i in range(15)]

edit_list = [i for i in origin_list if i % 3 == 0 and i > 0 and i % 4 != 0]

input("Press Enter")
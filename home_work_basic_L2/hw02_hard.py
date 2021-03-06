# Автор - Узун Максим Владимирович
# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
print('Задача 1')
eq = equation.split()
print(eq)
x = float(x)
y = 0
tmp_var = float(eq[2][:-1])
if eq[3] == '+':
    y = tmp_var*x + float(eq[4])
else:
    y = tmp_var*x - float(eq[4])

print(y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

print('   ')
print('Задача 2')

date_format = date.split('.')
day = date_format[0]
month = date_format[1]
year = date_format[2]
month_31 = ['01', '03', '05', '07', '08', '10', '12']
month_30 = ['02', '04', '06', '09', '11']

if len(day) == 2 and len(month) == 2 and len(year) == 4:
    if month in month_31 and 1 <= int(day) <= 31 and 1 <= int(year) <= 9999:
        print('Дата введена корректно')
    elif month in month_30 and 1 <= int(day) <= 30 and 1 <= int(year) <= 9999:
        print('Дата введена корректно')
    else:
        print('Дата некорректна')
else:
    print('Дата некорректна')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
print('   ')
print('Задача 3')

N = 10

cell_list = [ i*i for i in range(1, N)]
lvl_list = [i for i in range(1, N)]
print(cell_list)
print(lvl_list)

room = 13
number = 0

count = 0
for cell in cell_list:
    number += cell
    count += 1
    if number >= room:
        break

print('Номер блока, где нужная комната, количество этажей в блоке и количество комнат на этаже: ' + str(count))

slice_cell_list = cell_list[:count]
print(slice_cell_list)

last_room = sum(slice_cell_list)
print('Последняя комната в нужном нам блоке имеет номер: ' + str(last_room))

first_room = last_room - slice_cell_list[-1] + 1
print('Первая комната в  блоке имеет номер: ' + str(first_room))

before_lvl_number = sum(lvl_list[:(count - 1)])
print('Этажей до блока: ' + str(before_lvl_number))

inner_lvl = 1
end = first_room + count

for j in range(count):
    just_list = range(first_room, end)
    if room in just_list:
        inner_room_place = just_list.index(room) +1
        print('Положение комнаты на этаже: ' + str(inner_room_place))
        break
    first_room += count
    end += count
    inner_lvl += 1
final_lvl = inner_lvl + before_lvl_number
print('Комната находится на этаже: ' + str(final_lvl))

print('Вход: ', room)
print('Выход: ', str(final_lvl), str(inner_room_place))
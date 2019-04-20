# Автор Узун М.В.
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

try:
    user_input = int(input("Выберите действие:\n"
                       "1. Перейти в папку\n"
                       "2. Просмотреть содержимое  каталога\n"
                       "3. Удалить папку\n"
                       "4. Создать папку\n"
                       "Ваше действие: "))
    if user_input == 1:
        path = input("Введите имя папки: ")
        buffer = change_folder(path)
        if buffer == 1:
            print(f"Не могу перейти в папку {path}, она не существует")
        else:
            print(f"Успешно перешли в папку {path}")
    elif user_input == 2:
        look_in_folder(1, ".")
    elif user_input == 3:
        path = input("Введите имя директории: ")
        buffer = delete_folder(path)
        if buffer == 1:
            print(f"Директории {path} не существует")
        elif buffer == 2:
            print(f"Диретория {path} не пуста, не могу удалить")
        else:
            print(f"Директория {path} успешно удалена")
    elif user_input == 4:
        path = input("Введите имя директории: ")
        buffer = create_folder(path)
        if buffer == 1:
            print(f"Директория {path} уже существует")
        else:
            print(f"Директория {path} успешно создана")
    else:
        print("Не верный ввод")
except ValueError:
    print("Необходимо вводить цифры")
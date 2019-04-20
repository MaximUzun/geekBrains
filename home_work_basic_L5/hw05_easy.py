# Автор Узун М.В.
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def first_task():
    while True:
        try:
            user_input = int(input("1 - создать папки\n2 - удалить папки\nВведите номер задачи: "))
            if user_input == 1:
                for index in range(1, 10):
                    path = f"dir_{index}"
                    buffer = create_folder(path)
                    if buffer == 1:
                        print(f"Директория {path} существует")
                break
            elif user_input == 2:
                for index in range(1, 10):
                    path = f"dir_{index}"
                    buffer = delete_folder(path)
                    if buffer == 1:
                        print(f"Директория {path} не существует")
                    elif buffer == 2:
                        print(f"Директория {path} не пуста")
                break
            else:
                print("Не верный ввод")
        except ValueError:
            print("Необходимо вводить цифры, соответс")
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def second_task():
    print("Список каталогов текущей директории: ")
    look_in_folder(0, ".")

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def third_task():
    try:
        user_input = int(input("1 - скопировать файл\n2 - удалить файл\nВведите цифру: "))
        if user_input == 1:
            copyfile("hw05_easy.py", "hw05_easy.py_backup")
        elif user_input == 2:
            try:
                remove("hw05_easy.py_backup")
            except FileNotFoundError:
                print("Копии файла нет")
        else:
            print("Не верный ввод")
    except ValueError:
        print("Не верный ввод. Необходимо вводить цыфры")

# Автор Узун М.В.
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class student:
    def __init__(self, surname_name, clas, mother, father, subjects):
        self.surname_name = surname_name
        self.clas = clas
        self.mother = mother
        self.futher = father
        self.subjects = subjects

class teacher:
    def __init__(self, surname, subject, classes):
        self.surname = surname
        self.subject = subject
        self.classes = classes

stud_1 = student("Иванов И.И.", "5А", "Валентина", "Остап", ["математика", "русский", "английский"])
stud_2 = student("Сидоров С.С.", "5А", "Ольга", "Алексей", ["математика", "русский", "английский"])
stud_3 = student("Петров П.П.", "5А", "Альбина", "Руслан", ["математика", "русский", "английский"])
stud_4 = student("Лосев П.Л.", "5А", "Евгения", "Александр", ["математика", "русский", "английский"])
stud_5 = student("Михайлов П.К.", "5А", "Светлана", "Сергей", ["математика", "русский", "английский"])
stud_6 = student("Грач В.П.", "7А", "Светлана", "Рамиль", ["математика", "русский", "английский", "физика"])
stud_7 = student("Соловьев В.В.", "7А", "Александра", "Сергей", ["математика", "русский", "английский", "физика"])
stud_8 = student("Лучев А.А.", "7Б", "Виолета", "Петр", ["математика", "русский", "английский", "химия"])
stud_9 = student("Зверев А.С.", "7Б", "Галина", "Константин", ["математика", "русский", "английский", "химия"])
teach_1 = teacher("Иванов", "математика", ["5А","7А","7Б"])
teach_2 = teacher("Петров", "русский", ["5А","7А","7Б"])
teach_3 = teacher("Глушаков", "английский", ["5А","7А","7Б"])
teach_4 = teacher("Верещагин", "физика", ["7А"])
teach_5 = teacher("Руцкой", "химия", ["7Б"])
students = [stud_1, stud_2, stud_3, stud_4, stud_5, stud_6, stud_7, stud_8, stud_9]
teachers = [teach_1, teach_2, teach_3, teach_4, teach_5]
# 1. Получить полный список всех классов школы
full_clas_list = []
for i in students:
    if i.clas not in full_clas_list:
        full_clas_list.append(i.clas)
print(full_clas_list)
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
class_ = input("Введите номер класса: ")
class_list = []
for i in students:
    if i.clas == class_:
        class_list.append(i.surname_name)
print(class_list)
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
stud = input("Введите Фамилию И.О. ученика: ")
for i in students:
    if stud == i.surname_name:
        stud = i
teachers_for_stud = []
for j in teachers:
    if stud.clas in j.classes:
        teachers_for_stud.append(j.surname)
print(stud.surname_name + "-->" + stud.clas + "-->", teachers_for_stud, "-->", stud.subjects)
# 4. Узнать ФИО родителей указанного ученика
stud = input("Введите Фамилию И.О. ученика: ")
for i in students:
    if stud == i.surname_name:
        stud = i
print(stud.mother, stud.father)
# 5. Получить список всех Учителей, преподающих в указанном классе
class_ = input("Введите номер класса: ")
clas_teachers = []
for j in teachers:
    if class_ in j.classes:
        clas_teachers.append(j.surname)
print(clas_teachers)

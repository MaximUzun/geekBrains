# Автор Узун М.В.
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    pass

    number = str(number)
    if int(number[ndigits+1]) >= ndigits:
        check_number = int(number[ndigits])
        if int(number[ndigits]) == 9:
            round_number = number[:ndigits-1] + str(check_number+1)[0]
        else:
            round_number = number[:ndigits] + str(check_number+1)
        return round_number
    else:
        round_number = number[:ndigits+1]
        return round_number

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(2.9999967, 5))

input("Press Enter")


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    pass
    ticket_number = str(ticket_number)

    part1 = 0
    part2 = 0
    for i in range(len(ticket_number)):
        if i <= 2:
            part1 += int(ticket_number[i])
        else:
            part2 += int(ticket_number[i])

    if part1 == part2:
        return True
    else:
        return False

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

input("Press Enter")
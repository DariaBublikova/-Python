# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = number * (10 ** ndigits) + 0.41
    number = number // 1
    return number / (10 ** ndigits)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    num = str(ticket_number)
    lst_1 = int(num[0]) + int(num[1]) + int(num[2])
    lst_2 = int(num[3]) + int(num[4]) + int(num[5])
    if lst_1 == lst_2:
        return True
    else:
        return False

print(lucky_ticket(123006))
print(lucky_ticket(436751))
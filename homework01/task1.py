# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

number = int(input('введите номер дня недели: '))
if number > 5:
    print('да')
else:
    print('нет')
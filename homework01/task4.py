# задача 4 HARD необязательная Напишите простой калькулятор, который считывает 
# с пользовательского ввода три строки: первое число, второе число и операцию, 
# после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") 
# и выводит результат на экран

a=float(input('введите первое число: '))
operation=input('введите операцию: ')
b=float(input('введите первое число: '))
if operation == '+':
    print(a+b)
if operation == '-':
    print(a-b)
if operation == '/':
    if b!=0:
        print(a/b)
    else:
        print('Деление на 0!')
if operation == '*':
    print(a*b)
if operation == 'mod':
    if b!=0:
        print(a%b)
    else:
        print('Деление на 0!')
if operation == 'pov':
    print(a**b)
if operation == 'div':
    print(a//b)
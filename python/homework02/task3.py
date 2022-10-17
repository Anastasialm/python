# Задача 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой

list_1 = input('введите строку 1: ')
list_2 = input('введите строку 2: ')
count = 0
if len(list_1) > len(list_2):
    for list_2 in list_1:
        a = len(list_2)
        for i in a:
            if list_1[i] == list_2[i]:
                i +=1
            count +=1
print(count)
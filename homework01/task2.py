# задача 2. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = input('введите х:')
y = input('введите y:')
z = input('введите z:')
if not(x or y or z) == (not x and not y and not z):
    print('true')
else:
    print('false')
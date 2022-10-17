# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, 
# и координаты двух точек и находит расстояние между ними в N-мерном пространстве.
dim = int(input('введите количество координат: '))
try:
    coord_A = []
    for i in range(dim):
        coord_A.append(int(input(f'введите {i+1} координату точки А: ')))
    coord_B = []
    for i in range(dim):
        coord_B.append(int(input(f'введите {i+1} координату точки B: ')))
    print(coord_A, coord_B)

    sum = 0
    i = 0
    while i < dim:
        sum = sum + (coord_B[i]-coord_A[i])**2
        i +=1
    print(round((sum**0.5),2))
except:
    print('error')
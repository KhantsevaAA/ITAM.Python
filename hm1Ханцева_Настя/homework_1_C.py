print("HM1C\n Введите кол-во элементов в массиве: ", end='')

str=input()
mas=str.split()
k=1
for i in range(len(mas)-1):
    if mas[i+1]!=mas[i]:
        k=k+1
print(f'Кол-во неповторяющихся элементов массива: {k}')



print("HM1B\n Введите все элементы массива через пробел: ", end='')
k=0
str=input()
mas=str.split()
for i in range(len(mas)):
    if (int(f'{mas[i]}')>0):
        k=k+1
print(f'Кол-во положительных элементов: {k}')

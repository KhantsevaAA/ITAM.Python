print("HM1A\n Введите все элементы массива через пробел: ", end='')
str=input()
mas=str.split()
print('Все элементы с четными номерами', end='')
for i in range(len(mas)):
    if (i%2==0):
        print(f' {mas[i]}', end='')



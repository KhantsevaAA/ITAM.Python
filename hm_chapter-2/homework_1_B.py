def summation(start, end):
    s = 0
    end = end + 1
    if start + end != 0:
        if start < end:
            for i in range(start, end, 1):
                s = s + i
        else:
            for i in range(end, start):
                s = s + i
    return (f'Сумма чисел на отрезке {s}')


print('Введите границы отрезка числа, которого будут суммироваться, через пробел: ', end='')
str = input().split()
print(summation(int(str[0]), int(str[1])))

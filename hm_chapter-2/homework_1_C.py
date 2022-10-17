def summation(str):
    m = 0
    for i in range(len(str)):
        str[i]=int(str[i])
        if str[i] < 0:
            str[i] *= 2
        if m >= str[i]:
            m = str[i]
    f = lambda x: x / m
    str = map(f, str)
    return list(str)


print('Введите некоторое кол-во чисел, которые будут суммироваться по данному условию: ', end='')
n = input().split()
print(summation(n))

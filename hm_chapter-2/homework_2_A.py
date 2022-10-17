def rec(n):
    i: int = 1
    while n > i:
        n -= i
        i += 1
    if n != i:
        i -= 1
    return i


print('Введите кол-во блоков в лестнице: ', end='')
k = int(input())
print(rec(k))

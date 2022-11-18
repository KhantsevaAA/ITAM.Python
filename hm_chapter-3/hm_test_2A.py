class NumerialSystem:
    def __init__(self, n):
        mas = [0] * n
        ss = [0] * n
        self.str = ''
        print("Введите систему численя «BINARY» и «TERNARY», а дальше само число в заданной системе счисления.")
        for i in range(n):
            c = input().split(' ')
            # print(f"{c[0]} {c[1]}")
            mas[i] = int(c[1])
            if c[0] == "BINARY":
                ss[i] = binary(mas[i])
            elif c[0] == "TERNARY":
                ss[i] = termary(mas[i])
            print(ss[i])


def binary(num):
    out = 0
    n = 0
    while num != 0:
        out += ((num % 10) * (2 ** n))
        num = num // 10
        n += 1
    return out


def termary(num):
    out = 0
    n = 0
    while num != 0:
        out += ((num % 10) * (3 ** n))
        num = num // 10
        n += 1
    return out


n = int(input("Введите кол-во чисел: "))
str = NumerialSystem(n)

class NumerialSystem:
    def __init__(self, n):
        self.mas = [0] * n
        self.ss = [0] * n

        print("Введите систему численя «BINARY» и «TERNARY», а дальше само число в заданной системе счисления.")
        for i in range(n):
            c = input().split(' ')
            # print(f"{c[0]} {c[1]}")
            self.mas[i] = int(c[1])
            if c[0] == "BINARY":
                self.ss[i] = binary(self.mas[i])
            elif c[0] == "TERNARY":
                self.ss[i] = termary(self.mas[i])
            # self.strm += f"{mas[i]}  "
            # self.strs += f"{ss[i]}  "

    def num_sort(self):
        for i in range(len(self.ss) - 1):
            for j in range(len(self.ss) - i - 1):
                if self.ss[j] > self.ss[j + 1]:
                    c = self.ss[j]
                    self.ss[j] = self.ss[j + 1]
                    self.ss[j + 1] = c
                    c = self.mas[j]
                    self.mas[j] = self.mas[j + 1]
                    self.mas[j + 1] = c
        print(self.mas)

    def __str__(self):  # конвертирование объекта Binary в строку
        return str(self)


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
str.num_sort()

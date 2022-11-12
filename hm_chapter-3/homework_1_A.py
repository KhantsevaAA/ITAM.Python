class Binary:
    # def __init__(self, num):  # инициализация объекта Binary (num - число в 10 сс)
    #     first = 0
    #     num1 = int(num[0])
    #     second = 0
    #     num2 = int(num[1])
    #     n = 0
    #     while num1 != 0:
    #         first += ((num1 % 10) * (2 ** n))
    #         num1 = num1 // 10
    #         n += 1
    #     n = 0
    #     while num2 != 0:
    #         second += ((num2 % 10) * (2 ** n))
    #         num2 = num2 // 10
    #         n += 1
    #     Binary.num = first
    #     Binary.other = second

    def __init__(self, num):  # инициализация объекта Binary (num - число в 10 сс)
        self.num = 0
        n = 0
        while num != 0:
            self.num += ((num % 10) * (2 ** n))
            num = num // 10
            n += 1

    def __add__(self, other):  # сложение объекта Binary и other
        number = self.num + other.num
        output = 0
        n = 0
        while number != 0:
            output += (number % 10) * (2 ** n)
            number = number // 2
            n *= 10
        return output

    def __sub__(self, other):  # вычитание other из объекта Binary
        ...

    def __mul__(self, other):  # умножение объекта Binary на other
        ...

    def __floordiv__(self, other):  # целочисленное деление объекта Binary на other
        ...

    def __str__(self):  # конвертирование объекта Binary в строку
        ...


x = 101
y = 10
a = Binary(x)
b = Binary(y)
print(a + b)

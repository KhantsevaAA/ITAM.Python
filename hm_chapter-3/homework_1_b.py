class Ternary:
    def __init__(self, num):  # инициализация объекта Binary (num - число в 10 сс)
        self.num = 0
        n = 0
        while num != 0:
            self.num += ((num % 10) * (3 ** n))
            num = num // 10
            n += 1

    def __add__(self, other):  # сложение объекта Binary и other
        return translation(self.num + other.num)

    def __sub__(self, other):  # вычитание other из объекта Binary
        return translation(self.num - other.num)

    def __mul__(self, other):  # умножение объекта Binary на other
        return translation(self.num * other.num)

    def __floordiv__(self, other):  # целочисленное деление объекта Binary на other
        return translation(self.num // other.num)

    def __str__(self):  # конвертирование объекта Binary в строку
        return '{} '.format(self)


def translation(number):
    n = 0
    output = 0
    while number != 0:
        output = (number % 3) * (10 ** n) + output
        number = number // 3
        n += 1
    return output


x = int(input("Введите первое число в троичной системемe счисления: "))
y = int(input("Введите второе число в троичной системемe счисления: "))
a = Ternary(x)
b = Ternary(y)
print(a + b)
print(a - b)
print(a * b)
print(a // b)

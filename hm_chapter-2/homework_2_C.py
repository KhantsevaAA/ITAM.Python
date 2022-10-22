def conver(value, base):
    result = ""
    while value > 0:
        residue = value % base
        print("{}".format(residue))
        if (base >= 10) and (residue >= 10):
            result = "{}".format(chr(residue + 55)) + result
        else:
            result = "{}".format(residue) + result
        value = value // base
    return result


print('Введите число в 10-й системе счисления и через пробел сс, в кот-ю надо превести:', end=' ')
str = input().split()
print(conver(int(str[0]), int(str[1])))

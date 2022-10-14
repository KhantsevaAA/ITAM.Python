print("Введите зашифрованную строку: ", end=' ')
str = list(input())

n = 0
while str[n].isupper() == False:
    n = n + 1
answer = str[n]
s = n
while str[s].isdigit() == False:
    s = s + 1
s = s + 1
step = s - n
for i in range(s, len(str), step):
    answer = answer + str[i]
print(f'Дешифрованная строка {answer}')

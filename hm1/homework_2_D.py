print("Введите элементы массива: ", end='')
str = input().split()
k=str[len(str)-1]
for i in range(len(str) - 1, 0, -1):
    str[i] = str[i - 1]
str[0]=k
print(f'Mассив, полученный после сдвига элементов: {str}')

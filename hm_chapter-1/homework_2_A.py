print("Ведите кол-во участников: ", end='')
n = int(input())
och = 0
neoch = 0
print(f"Введите {n} строки формата Фамилия Имя Возраст Формат_участия")
for i in range(n):
    str = input().split()
    if str[3] == 'True':
        och = och + 1
    else:
        neoch = neoch + 1
print(f'Сколько человек записалось на очный формат и на заочный: {och} {neoch}')

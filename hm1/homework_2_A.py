print("Ведите кол-во участников: ", end='')
n = int(input())
och = 0
neoch = 0
for i in range(n):
    str = input().split()
    if str[3] == 'True':
        och = och + 1
    else:
        neoch = neoch + 1
print(f'{och} {neoch}')

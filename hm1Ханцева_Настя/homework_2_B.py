print("Ведите кол-во участников: ", end='')
n = int(input())
och = 0
neoch = 0
nt = 0
for i in range(n):
    f = 0
    str = input().split()
    for j in range(len(str)):
        if str[j] == 'True' or str[j] == 'False':
            f = f + 1
            k = j
    print(f)
    if f == 1:
        if str[k] == 'True':
            och = och + 1
        else:
            neoch = neoch + 1
    else:
        if str[3] == 'True':
            och = och + 1
        elif str[3] == 'False':
            neoch = neoch + 1
        else:
            nt = nt + 1
print(f'{och} {neoch} {nt}')

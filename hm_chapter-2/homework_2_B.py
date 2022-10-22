def key_difference(dict1, dict2):
    dict3 = dict()
    f = False
    for key1, value1 in dict1.items():
        if key1 in dict2.keys():
            if value1 == dict2[key1]:
                dict3[key1] = 'equal'
            else:
                dict3[key1] = 'changed'
        else:
            dict3[key1] = 'deleted'
    for key2, value2 in dict2.items():
        if key2 not in dict1.keys():
            dict3[key2] = 'added'
    return dict3


d1 = dict()
d2 = dict()
print('Введите первый словарь в формате "ключ:статус" через Enter (для окончания введите пустую строку):')
f = True
while f:
    str = input()
    if not str:
        f = False
    else:
        str = str.split(":")
        d1[str[0]] = str[1]
print(d1)
print('Введите второй словарь в формате "ключ:статус" через Enter (для окончания введите пустую строку):')
f = True
while f:
    str = input()
    if not str:
        f = False
    else:
        str = str.split(":")
        d2[str[0]] = str[1]
print(d2)
print(key_difference(d1, d2))

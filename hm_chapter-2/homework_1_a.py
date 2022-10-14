def greetings(str):
    str=str.split()
    return f'Доброго времени суток, {str[1]} "Человек" {str[0]}!'

    str=input().split()
    return f'Доброго времени суток, {str[0]} "Человек" {str[1]}!'
print('Введите фамилию и имя пользователя:', end='')
print(greetings(input()))
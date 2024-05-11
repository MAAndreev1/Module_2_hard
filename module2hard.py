# Словарь для проверки результатов

check = dict({})
check[3] = 12
check[4] = 13
check[5] = 1423
check[6] = 121524
check[7] = 162534
check[8] = 13172635
check[9] = 1218273645
check[10] = 141923283746
check[11] = 11029384756
check[12] = 12131511124210394857
check[13] = 112211310495867
check[14] = 1611325212343114105968
check[15] = 1214114232133124115106978
check[16] = 1317115262143531341251161079
check[17] = 11621531441351261171089
check[18] = 12151811724272163631545414513612711810
check[19] = 118217316415514613712811910
check[20] = 13141911923282183731746416515614713812911

# Домашнее задание

while True:
    n = input('Какое число сейчас на левой табличке? >>> ')

    numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    numbers_first = list(numbers_tuple)
    numbers_second = list(numbers_tuple)
    result = ''

    if (n.isdigit() == False) or ((int(n) in check) == False):  # Проверка корректности вводимой информации
        print('Такого не может быть на табличке! Введите другое значение.')
        continue

    n = int(n)

    for i in numbers_tuple:
        numbers_second.remove(i)
        for j in numbers_second:
            if n % (i + j) == 0:
                result += (str(i) + str(j))
    print(f'{n} - {result}',)

    if result == str(check[n]):  # Проверка результата
        print('Верно')
    else:
        print('Ошибочный результат!')

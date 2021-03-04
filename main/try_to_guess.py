import random
from time import sleep


n = random.randint(0, 10)  # Choose a number in range of 1, 11
x = 'Bem vindo ao '
new = ''
for y in x:
    new = y  # 'New' start being the letters of x
    if y == ' ':  # if y is a space, the timer is 0, so skip to the next letter
        sleep(0)
    else:
        sleep(0.22)  # wait 0.22 sec to star printing the letters
    print('\033[35m{}\033[m'.format(new,), end='')
a = ''
inicio = 0
add = 1
for c in range(0, 3):  # 'a' will be printed 3 times
    if inicio == 0:  # in the first time, print 'TRY'
        a = 'TRY'
    if inicio == 1:
        a = 'TO'
    if inicio == 2:
        a = 'GUESS!!'
    sleep(0.5)
    print('\033[36m{}\033[m'.format(a), end=' ')
    inicio += add
sleep(1)
print('\nO computador pensou em um número de 0 a 10. Tente adivinhar')
num = int(input('Digite aqui: '))
print('\033[31mPROCESSANDO\033[m', end='')
a = '.'
inicio = 0
limite = 0
cont1 = 0  # variable created to count how many times number chosen by pc was > then entered number
cont2 = 0  # variable created to count how many times number chosen by pc was < then entered number
for c in range(0, 9):
    if inicio == 0:
        a = '\033[31m.\033[m'
        limite = 1
    if inicio == 3:
        a = '\b'
        limite = - 1
    sleep(0.22)
    print(a, end='')
    inicio += limite
if num == n:
    print('\n\033[32mPARABÉNS!!!\033[m\033[36m Você acertou de primeira.\033[m')
else:
    while num != n:  # While entered number is different from number chosen by pc, keep looping
        if num > n:  # if entered number ir > then chosen number
            num = int(input('\n\033[4mMenor... Tente novamente:\033[m '))
            print('\033[31mPROCESSANDO\033[m', end='')
            a = '.'
            inicio = 0
            limite = 0
            for c in range(0, 9):
                if inicio == 0:
                    a = '\033[31m.\033[m'
                    limite = 1
                if inicio == 3:
                    a = '\b'
                    limite = - 1
                sleep(0.22)
                print(a, end='')
                inicio += limite
            cont1 += 1
        elif num < n:  # if entered number is < then chosen number
            num = int(input('\n\033[4mMaior... Tente novamente:\033[m '))
            print('\033[31mPROCESSANDO\033[m', end='')
            a = '.'
            inicio = 0
            limite = 0
            for c in range(0, 9):
                if inicio == 0:
                    a = '\033[31m.\033[m'
                    limite = 1
                if inicio == 3:
                    a = '\b'
                    limite = - 1
                sleep(0.22)
                print(a, end='')
                inicio += limite
            cont2 += 1
        if num == n:
            print('\nVocê precisou de \033[7;40m {} \033[m tentativas para vencer!!.'.format(cont1 + cont2 + 1))

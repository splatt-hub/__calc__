from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.WHITE)
print('Добро Пожаловать в __CALC__', '\n',
      'Инструкция:', '\n',
      '+ сложение', '\n',
      '- вычетание', '\n',
      '/ деление', '\n',
      '* умножение', '\n',
      '% остаток деления', '\n',
      '! деление нацело')

while True:
    print(Fore.GREEN)
    s = input('Введите выражение:')
    if s[s.find('+')] == '+':
        a = s.split('+')
        print(Fore.CYAN)
        print(f'Ответ: {float(a[0]) + float(a[1])}')
    elif s[s.find('-')] == '-':
        a = s.split('-')
        print(Fore.CYAN)
        print(f'Ответ: {float(a[0]) - float(a[1])}')
    elif s[s.find('*')] == '*':
        a = s.split('*')
        print(Fore.CYAN)
        print(f'Ответ: {float(a[0]) * float(a[1])}')
    elif s[s.find('%')] == '%':
        a = s.split('%')
        print(Fore.CYAN)
        print(f'Ответ: остаток {round(float(a[0]) % float(a[1]), 3)}')
    elif s[s.find('!')] == '!':
        a = s.split('!')
        if float(a[0]) // float(a[1]) == 1:
            print(Fore.CYAN)
            print(f'Ответ: {round(float(a[0]) // float(a[1]), 3)} целое')
        else:
            print(Fore.CYAN)
            print(f'Ответ: {round(float(a[0]) // float(a[1]), 3)} целых')
    elif s[s.find('/')] == '/':
        a = s.split('/')
        if float(a[1]) == 0:
            print(Fore.RED)
            print ('Ну ты что, на ноль делить нельзя')
        else:
            print(Fore.CYAN)
            print(f'Ответ: {round(float(a[0]) / float(a[1]), 3)}')
    elif s[s.find('^')] == '^':
        a = s.split('^')
        print(Fore.CYAN)
        print(f'Ответ: {float(a[0]) ** float(a[1])}')
    else:
        print(Fore.RED)
        print('Введено несуществующее действие')
        continue
'''
Par ou Ímpar - URI Online Judge - 1074.py

Emanuel Araújo de Moura
'''

quantidadeValores = int(input())

for i in range(quantidadeValores):
    numero = int(input())
    if numero > 0 and numero % 2 == 0:
        print("EVEN POSITIVE")
    elif numero < 0 and numero % 2 == 0:
        print("EVEN NEGATIVE")
    elif numero > 0:
        print("ODD POSITIVE")
    elif numero < 0:
        print("ODD NEGATIVE")
    else:
        print("NULL")
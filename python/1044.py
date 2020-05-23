'''
Múltiplos - URI Online Judge - 1044.py

Emanuel Araújo de Moura
'''

valores = list(map(int, input().split()))

if valores[1] % valores[0] == 0 or valores[0] % valores[1] == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
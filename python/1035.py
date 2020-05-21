'''
Teste de Seleção 1 - URI Online Judge - 1035.py

Emanuel Araújo de Moura
'''

valores = list(map(int, input().split()))
#  a = 0    b = 1    c = 2   d = 3
if valores[1] > valores[2] and valores[3] > valores[0]:
    if valores[2] + valores[3] > valores[0] + valores[1]:
        if (valores[2] > 0 and valores[3] > 0) and (valores[0] % 2 == 0):
            print("Valores aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")
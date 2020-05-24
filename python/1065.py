'''
Pares entre cinco números -URI Online Judge - 1065.py

Emanuel Araújo de Moura
'''

pares = 0
for i in range(5):
    numero = int(input())
    if numero % 2 == 0:
        pares += 1

print("{} valores pares".format(pares))
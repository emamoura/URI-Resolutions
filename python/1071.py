'''
Soma de Impares Consecutivos I - URI Online Judge - 1071.py

Emanuel Araújo de Moura
'''

x = int(input())
y = int(input())

valores = [x,y]
valores = sorted(valores)
soma = 0

for i in range(valores[0] + 1, valores[1]):
    if i % 2 != 0:
        soma += i
print(soma) 
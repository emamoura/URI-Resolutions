'''
Intervalo 2 - URI Online Judge - 1072.py

Emanuel Araújo de Moura
'''

quantidadeValores = int(input())

dentroIntervalo = 0

for i in range(quantidadeValores):
    numero = int(input())
    if 10 <= numero and numero <= 20:
        dentroIntervalo += 1

print("{} in".format(dentroIntervalo))
print("{} out".format(quantidadeValores - dentroIntervalo)) 
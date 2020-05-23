'''
Pares, ímpares, Positivos e Negativos - URI Online Judge - 1066.py

Emanuel Araújo de Moura
'''

negativo = 0
positivo = 0
par = 0
impar = 0
for i in range(5):
    numero = int(input())
    if numero == 0:
        par += 1
    elif numero < 0 and numero % 2 == 0:
        par += 1
        negativo +=1
    elif numero > 0 and numero % 2 == 0:
        par += 1
        positivo +=1
    elif numero < 0:
        negativo += 1
        impar += 1
    elif numero > 1:
        positivo +=1
        impar += 1

print("{} valor(es) par(es)".format(par))
print("{} valor(es) impar(es)".format(impar))
print("{} valor(es) positivo(s)".format(positivo))
print("{} valor(es) negativo(s)".format(negativo))
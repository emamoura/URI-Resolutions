'''
Notas e Moedas - URI Online Judge - Questão 1021

Emanuel Araújo de Moura
'''

nota = float(input())
nota_copia = (nota % 1) 
nota_copia = round(nota_copia, 2) * 100
listaNotas = [100,50,20,10,5,2]
respostaNotas = []
listaMoedas = [100,50, 25, 10, 5, 1]
respostaMoeda = []

for numero in listaNotas:
    respostaNotas.append(int(nota // numero))
    nota = nota % numero
for numero in listaMoedas:
        respostaMoeda.append(int(nota_copia // numero))
        nota_copia = nota_copia % numero
if nota > 1:
    respostaMoeda[0] = 1

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(respostaNotas[0]))
print("{} nota(s) de R$ 50.00".format(respostaNotas[1]))
print("{} nota(s) de R$ 20.00".format(respostaNotas[2]))
print("{} nota(s) de R$ 10.00".format(respostaNotas[3]))
print("{} nota(s) de R$ 5.00".format(respostaNotas[4]))
print("{} nota(s) de R$ 2.00".format(respostaNotas[5]))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(respostaMoeda[0]))
print("{} moeda(s) de R$ 0.50".format(respostaMoeda[1]))
print("{} moeda(s) de R$ 0.25".format(respostaMoeda[2]))
print("{} moeda(s) de R$ 0.10".format(respostaMoeda[3]))
print("{} moeda(s) de R$ 0.05".format(respostaMoeda[4]))
print("{} moeda(s) de R$ 0.01".format(respostaMoeda[5]))
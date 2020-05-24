'''
Aumento de Salário - URI Online Judge - 1048.py

Emanuel Araújo de Moura
'''

salario = float(input())

if salario <= 400:
    reajuste = (salario * 0.15)
    percentual = 15
    novoSalario = reajuste + salario
elif salario <= 800:
    reajuste = (salario * 0.12)
    percentual = 12
    novoSalario = reajuste + salario
elif salario <= 1200:
    reajuste = (salario * 0.10)
    percentual = 10
    novoSalario = reajuste + salario
elif salario <= 2000:
    reajuste = (salario * 0.07)
    percentual = 7
    novoSalario = reajuste + salario
else:
    reajuste = (salario * 0.04)
    percentual = 4
    novoSalario = reajuste + salario

print("Novo salario: {:.2f}".format(novoSalario))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {} %".format(percentual))
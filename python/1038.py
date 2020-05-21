'''
Lanches - URI Online Judge - 1038.py

Emanuel Araújo de Moura
'''

entrada = list(map(int,input().split()))

preco = [4.00, 4.50, 5.00, 2.00, 1.50]

saida = preco[entrada[0] - 1] * entrada[1]

print("Total: R$ {:.2f}".format(saida))
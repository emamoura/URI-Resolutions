valores = list(map(float, input().split()))
pesos = [2,3,4,1]
soma = 0
notaFinal = 0

for i in range(len(valores)):
    soma += (valores[i] * pesos[i])
mediaPonderada = soma/10
if mediaPonderada >= 7:
    print("Media: {:.1f}".format(mediaPonderada))
    print("Aluno aprovado.")
elif mediaPonderada < 5:
    print("Media: {:.1f}".format(mediaPonderada))
    print("Aluno reprovado.")
else:
    print("Media: {:.1f}".format(mediaPonderada))
    print("Aluno em exame.")
    notaExame = float(input())
    print("Nota do exame: {:.1f}".format(notaExame))
    notaFinal = (mediaPonderada + notaExame) / 2
    if notaFinal >= 5:
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(notaFinal))
    else:
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(notaFinal))
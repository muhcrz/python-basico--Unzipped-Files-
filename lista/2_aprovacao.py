media = float(input("Digite a média do aluno: "))
faltas = int(input("Digite o número de faltas do aluno: "))

if media >= 6.0 and faltas <= 15:
    print("Aprovado")
else:
    print("Reprovado")
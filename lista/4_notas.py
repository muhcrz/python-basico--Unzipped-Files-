notas = [3.0, 5.0, 7.0, 9.0, 8.0]

nomes = ["João", "Maria", "Pedro", "Ana", "Lucas"]

for i in range(len(nomes)):
    print(f"{nomes[i]}: {notas[i]}")

print(f"Média: {sum(notas) / len(notas)}")

print(f"Maior nota: {max(notas)}")

print(f"Menor nota: {min(notas)}")

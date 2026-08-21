def Calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

print("Calculadora de IMC")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = Calcular_imc(peso, altura)
print(f"Seu IMC é: {imc:.2f}")

Abaixo_do_peso = "Abaixo do peso"
Peso_normal = "Peso normal"
Sobrepeso = "Sobrepeso"
Obesidade = "Obesidade"

abaixo_do_peso = imc < 18.5
peso_normal = 18.5 <= imc < 25
sobrepeso = 25 <= imc < 30
obesidade = imc >= 30

print("Classificação do IMC:")
if abaixo_do_peso:
    print(Abaixo_do_peso)
elif peso_normal:
    print(Peso_normal)
elif sobrepeso:
    print(Sobrepeso)
elif obesidade:
    print(Obesidade)
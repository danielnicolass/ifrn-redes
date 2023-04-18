peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2)
print("Seu IMC é:", imc)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Acima do peso")
elif imc < 35:
    print("Sobrepeso")
elif imc < 40:
    print("Obesidade")
else:
    print("Obesidade grave")

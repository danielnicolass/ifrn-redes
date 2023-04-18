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

    //
    
    print("qual o seu peso?")
peso = float(input())
print("qual sua altura?")
altura = float(input())
imc = peso/altura**2
print("esse é seu imc:", imc)

if imc< 18.5:
	print("abaixo do peso")

else:
    if imc>= 18.5 and imc <= 24.9:
        print("peso normal")
    else:
        if imc>=25 and imc<=  29.9:
            print("acima do peso")
        else:
            if imc>=30 and imc<= 34.9:
                print("sobrepeso")
            else:
                if imc>=35 and imc<= 39.9:
                    print("obesidade")
                else:
                    if imc>40:
                        print("obesidade grave")

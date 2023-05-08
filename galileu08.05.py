#soma de todos os números primos abaixo de 1000

soma = 0

x = 1

while x < 1000:
    if x%1 == 0 and x%x == 0:
        soma = soma + x
        x = x + 1
    else: x = x + 1

print(soma)
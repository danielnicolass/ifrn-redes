conta = int(input("Digite o valor da sua conta "))
pagamento = int(input("Digite o quanto deseja pagar "))
troco = pagamento - conta
print ("O seu troco é:", troco)


# Define os valores das notas e moedas disponíveis
notas = [200, 100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05]

# Solicita o valor total da compra e o valor pago
print("Digite o valor total da compra:")
total = float(input())
print("Digite o valor pago:")
pago = float(input())

# Calcula o troco
troco = pago - total

# Exibe o troco em notas
print("Troco em notas:")
nota_atual = 0
if troco >= 200:
    nota_atual = 0
if troco >= 100:
    nota_atual = 1
if troco >= 50:
    nota_atual = 2
if troco >= 20:
    nota_atual = 3
if troco >= 10:
    nota_atual = 4
if troco >= 5:
    nota_atual = 5
if troco >= 2:
    nota_atual = 6
nota = notas[nota_atual]
qtd = int(troco / nota)
print(f"{qtd} notas de R${nota:.2f}")
troco -= qtd * nota

# Exibe o troco em moedas
print("Troco em moedas:")
moeda_atual = 0
if troco >= 1:
    moeda_atual = 0
if troco >= 0.5:
    moeda_atual = 1
if troco >= 0.25:
    moeda_atual = 2
if troco >= 0.1:
    moeda_atual = 3
if troco >= 0.05:
    moeda_atual = 4
moeda = moedas[moeda_atual]
qtd = int(troco / moeda)
print(f"{qtd} moedas de R${moeda:.2f}")
troco -= qtd * moeda

def calcular_troco(valor_total, valor_pago):
    # Calcula o valor do troco
    troco = valor_pago - valor_total

    # Define o valor das notas e moedas em Real
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01]

    # Inicializa o dicionário de troco
    troco_dict = {}

    # Loop pelas notas
    for nota in notas:
        if troco >= nota:
            qtd_notas = troco // nota
            troco_dict[f'{nota} reais'] = int(qtd_notas)
            troco -= qtd_notas * nota

    # Loop pelas moedas
    for moeda in moedas:
        moeda_em_centavos = int(moeda * 100)
        if troco >= moeda:
            qtd_moedas = int(troco // moeda)
            troco_dict[f'{moeda_em_centavos} centavos'] = qtd_moedas
            troco -= qtd_moedas * moeda

    return troco_dict



# Recebe o valor total da conta e o valor pago pelo cliente
valor_total = float(input("Digite o valor total da conta: "))
valor_pago = float(input("Digite o valor pago pelo cliente: "))

# Calcula o valor do troco
troco = valor_pago - valor_total

# Define o valor das notas e moedas em Real
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01]

# Inicializa o dicionário de troco
troco_dict = {}

# Loop pelas notas
for nota in notas:
    if troco >= nota:
        qtd_notas = troco // nota
        troco_dict[f'{nota} reais'] = int(qtd_notas)
        troco -= qtd_notas * nota

# Loop pelas moedas
for moeda in moedas:
    moeda_em_centavos = int(moeda * 100)
    if troco >= moeda:
        qtd_moedas = int(troco // moeda)
        troco_dict[f'{moeda_em_centavos} centavos'] = qtd_moedas
        troco -= qtd_moedas * moeda

# Imprime o resultado
print("O troco é:")
for chave, valor in troco_dict.items():
    print(f"{valor} {chave}")

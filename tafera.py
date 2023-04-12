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
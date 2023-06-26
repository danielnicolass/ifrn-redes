# Leitura das notas a partir do arquivo
notas = []
arquivo = open('notas.txt', 'r')
for linha in arquivo:
    notas.append(float(linha))
arquivo.close()

# Cálculo da média ponderada
pesos = [2, 2, 3, 3]
soma_pesos = 0
soma_notas = 0
for i in range(len(notas)):
    soma_pesos += pesos[i]
    soma_notas += notas[i] * pesos[i]
media_turma = soma_notas / soma_pesos

# Contagem de alunos acima da média desejada
media_desejada = 60
alunos_acima_media = 0
for nota in notas:
    if nota >= media_desejada:
        alunos_acima_media += 1

# Exibição dos resultados
print("Média da turma:", media_turma)
print("Alunos acima da média desejada (60):", alunos_acima_media)

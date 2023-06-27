#Qual o menor valor de ação no último ano?


fd = open("C:\\Users\\20231014050044\\Desktop\\petro.txt", "r")
fd.readline()

linhas = fd.readlines()
menores = []

for linha in linhas:
    colunas = linha.split(",")
    menores.append(float(colunas[3]))

menor = min (menores)


print(menor)


#Qual o preço médio de fechamento?

#Qual o volume médio negociado?

#Qual dia teve o maior valor?
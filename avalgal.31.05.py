#Questão 1 da avaliação
dia = int (input("Dia? "))
mes = int (input("Mês? "))
ano = int (input("Ano? "))

numDias = 0
for a in range(2000, ano):
    numDias += 365
    if a%400 == 0 or a%4 == 0 and a%100 != 0:
        numDias += 1

for m in range(1, mes):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10:
        numDias += 31
    elif (m == 4) or (m == 6) or (m == 9) or (m == 11):
        numDias += 30
    else:
        if (ano%400 == 0) or (ano%4==0 and ano%100 != 0):
            numDias += 29
        else:
            numDias +=28

numDias += dia

numSextas = numDias // 7
print ("Já se passaram", numSextas, "sextas-feiras")


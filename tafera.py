tempo, distancia = int

print("digite o tempo")
tempo = int(input())
print("digite a distancia percorrida")
distancia = int(input())
print("digite a quantidade de litros")
litros = float (input())
print("digite a quantidade de reais do combustivel")
reais = float (input())


tempo = (tempo/3600)
velocidadeMedia = distancia/tempo
custo = litros*reais
desempenhoL = distancia/litros
desempenhoR = custo/distancia
print("velocidade media.", velocidadeMedia)
print("custo da viagem:", custo)
print("desempenho do carro em litros:", desempenhoL)
print("desempenho do carro em reais.", desempenhoR)
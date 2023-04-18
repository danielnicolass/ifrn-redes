carros_vendidos = int(input("Digite o número de carros vendidos: "))
valor_vendas = float(input("Digite o valor total das vendas: R$"))
salario_fixo = float(input("Digite o salário fixo do vendedor: R$"))
comissao_carro = float(input("Digite o valor da comissão por carro vendido: R$"))

salario_comissao = comissao_carro * carros_vendidos
salario_percentual = 0.06 * valor_vendas
salario_final = salario_fixo + salario_comissao + salario_percentual

print("O salário final do vendedor é: R${:.2f}".format(salario_final))

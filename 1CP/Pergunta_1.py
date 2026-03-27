produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço unitário do produto: R$"))
quantidade = int(input("Digite a quantidade do produto desejado: "))
porcentagemDesconto = float(input("Digite o percentual de desconto: "))

valorProdutos = preco * quantidade
valorDesc = valorProdutos * porcentagemDesconto/100
valorFinal = valorProdutos - valorDesc

print("Produto:", produto)
print("Valor bruto:R$", valorProdutos)
print("Desconto: R$", valorDesc)
print("Valor final: R$",valorFinal)

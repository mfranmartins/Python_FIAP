nome = input("Digite o nome do colaborador: ")
valorHora = float(input("Digite o valor da hora trabalhada:R$"))
quantHora = float(input("Digite a quantidade de horas trabalhadas: "))
valorBonus = float(input("Digite o valor do bônus fixo mensal: R$"))
valorDesc = float(input("Digite o valor do desconto total mensal: R$"))

salarioBruto = valorHora * quantHora + valorBonus
salarioLiquido = salarioBruto - valorDesc

print("Colaborador(a):",nome)
print("Salário bruto:R$",salarioBruto)
print("Salário líquido:R$",salarioLiquido)


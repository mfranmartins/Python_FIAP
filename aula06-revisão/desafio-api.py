endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

# FUNÇÃO que verifica se UM código HTTP de uma requisições é sucesso ou não
def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# FUNÇÃO que verifica se tem 2 erros seguidos na lista de requisições de UM endpoint
def verifica_erros(codigos_endpoint):
    for i in range(len(codigos_endpoint) - 1):
        codigo_atual = codigos_endpoint[i]
        prox_codigo = codigos_endpoint[i+1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False
#Calculo da porcentagem de requisições bem sucedidas de cada endpoint
mais_erros = 0
for i in range(len(status)):
    cont = 0
    valor_endpoint = status[i]

    for j in range(len(valor_endpoint)):
        if eh_sucesso(valor_endpoint[j]):
            cont += 1
    erros = len(valor_endpoint) - cont
    porcentagem = cont/len(valor_endpoint) * 100
    tem_erros_seguidos = verifica_erros(status[i])

    if mais_erros < erros:
        mais_erros = erros
        end_mais_erros = endpoints[i]

    if tem_erros_seguidos:
        estado = "CRÍTICO"
    elif porcentagem >= 80:
        estado = "ESTÁVEL"
    else:
        estado = "INSTÁVEL"

    print(f"{endpoints[i]} → {int(porcentagem)}% de requisições bem-sucedidas → {estado}")
print()
print("Endpoint com mais erros:", end_mais_erros)

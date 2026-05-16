temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]
tamanho = len(temperaturas)
max_c = 0
sala_c = 0

for sala in range(tamanho):
    print("Sala", sala + 1)
    temps_sala = temperaturas[sala]

    media = 0
    contador = 0
    for x in range(len(temps_sala)):
        if temperaturas[sala][x] >= 33:
            contador += 1
        media += temperaturas[sala][x]
    print("Média:", media/len(temps_sala))
    print("Registros críticos:",contador)
    if contador > max_c:
        max_c = contador
        sala_c = sala + 1

    print()

print("Sala com maior risco: Sala",sala_c)


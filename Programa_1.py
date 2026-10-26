def calcular_media(notas):
    return sum(notas) / len(notas)
def situacao(media, minimo=7.0):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
nome = input("Nome do estudante: ")
notas = []
for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)
    media = calcular_media(notas)
resultado = situacao(media)
print("\\nNome:", nome)
print(f"Média: {media:.2f}")
print("Situação:", resultado)






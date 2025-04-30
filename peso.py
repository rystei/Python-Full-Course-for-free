#Python convertedor de peso

peso = float(input("Insira seu peso: "))
unidade = input("Quilogramas ou libras (Q ou L): ").upper()

if unidade == "Q":
    peso = peso * 2.205
    unidade = "Lbs"
    print(f"Seu peso é: {round(peso, 1)} {unidade}")
elif unidade == "L":
    peso = peso / 2.205
    unidade = "Kgs"
    print(f"Seu peso é: {round(peso, 1)} {unidade}")
else:
    print(f"{unidade} não é valido")


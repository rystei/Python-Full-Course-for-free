#if = Serve para executar uma condição apenas se ela for verdadeira

print("Bem vindo a auto escola")
print("Descubra se você pode diridir")

while True:
    sair = input("deseja sair do programa? (digite 'sim' para sair): ")

    if sair == "sim":
        print("tchau!")
        break

    idade = int(input("Informe sua idade: "))
    quanto_tempo_falta = 18 - idade

    if idade >= 80:
        print("Você não pode mais dirigir senhor")
    elif idade >= 18:
        print("Você pode dirigir!")
    elif idade <= 12:
        print("Você é muito novo para estar aqui, cade seus pais?")
    else:
        print(f"Você não pode dirigir pois é menor de idade, ainda falta {quanto_tempo_falta} anos para você poder dirigir.")

    print("deseja sair ou ficar ?")

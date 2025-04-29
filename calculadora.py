#Calculadora em python
#Usando um loop para repetir o código até digitar "sim"
#Resultados arrendondados para até 5 casas decimais

print("Bem vindo a sua calculadora basica em python")

while True:
    operacao = input("Selecione o tipo de operação que você gostaria de fazer(+ - * /): ")

    if operacao not in ["+", "-", "*", "/"]:
        print("Por favor escolha entre (+ - * /)")
        continue

    num1 = float(input("Insira o primeiro numero: "))
    num2 = float(input("Insira o segundo numero: "))

    if operacao == "+":
        resultado = num1 +num2
        print(round(resultado, 5))
    elif operacao == "-":
        resultado = num1 - num2
        print(round(resultado, 5))
    elif operacao == "*":
        resultado = num1 * num2
        print(round(resultado, 5))
    elif operacao == "/":
        resultado = num1 / num2
        print(round(resultado, 5))

    sair = input("deseja sair do programa? (digite 'sim' para sair) ou (digite qualquer outra tecla para continuar): ")
    if sair == "sim":
        print("Tchau")
        break


unidade = input("Insira se você quer uma temperatura em Celsius ou Fahrenheit (C/F): ").upper()
temp = float(input("Insira a temperatura: "))

if unidade == "F":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"A Temperatura em Fahrenheit é: {temp}°F ")
elif unidade == "C":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"A Temperatura em Celsius é: {temp}°C ")
else:
    print(f"{unidade} não é uma unidade valida :(")
# operadores lógicos = avaliam múltiplas condições (or, and, not)
#    or = pelo menos uma condição deve ser True (verdadeira)
#    and = ambas as condições devem ser True (verdadeiras)
#    not = inverte a condição (not False se torna True, not True se torna False)

#exemplo or!
# temp = 20
# esta_chovendo = True
# if temp > 40 or temp < 10 or esta_chovendo:
#     print("O evento está cancelado")
# else:
#     print("O evento vai acontecer")

#exemplo and e not!

temp = 28
esta_ensolarado = False

if temp >= 24 and esta_ensolarado:
    print("Está quente")
    print("Está ensolarado")
elif temp < 0 and esta_ensolarado:
    print("Esta frio lá fora")
    print("Está ensolarado")
elif 28 > temp > 0 and esta_ensolarado:
    print("Esta Calor lá fora")
    print("Está ensolarado")
elif temp < 0 and not esta_ensolarado:
    print("Esta frio lá fora")
    print("Está nublado")
elif 28 >= temp > 0 and not esta_ensolarado:
    print("Esta Calor lá fora")
    print("Está nublado")
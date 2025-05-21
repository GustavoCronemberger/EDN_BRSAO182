#Lambda
calcular_gorjeta = lambda valor_conta, porcentagem_gorjeta: float(valor_conta) * float((porcentagem_gorjeta / 100))

valor_da_conta = 350.00
porcentagem = 10

print(f"A gorjeta será de R$ {calcular_gorjeta(valor_da_conta, porcentagem):.2f}")

#Função def

# def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
#     gorjeta = valor_conta * (porcentagem_gorjeta / 100)
#     return gorjeta

# valor_da_conta = 350.00
# porcentagem = 1

# valor_gorjeta = calcular_gorjeta(valor_da_conta, porcentagem)
# print(f"A gorjeta será de R$ {valor_gorjeta:.2f}")
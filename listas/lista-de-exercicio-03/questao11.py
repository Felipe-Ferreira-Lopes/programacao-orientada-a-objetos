salario = float (input("Digite o salario: "))
if salario <=280:
    novo_salario = salario * 1.20
    valor_aumento = novo_salario - salario
    print("Salario atual: ",salario)
    print("Percentual de ajuste salarial 20%")
    print("valor do aumento igual a: ",valor_aumento)
    print("Salario ajustado: ",novo_salario)
elif salario >281 and salario <= 700:
    novo_salario = salario * 1.15
    valor_aumento = novo_salario - salario
    print("Salario atual: ",salario)
    print("Percentual de ajuste salarial 15%")
    print("valor do aumento igual a: ",valor_aumento)
    print("Salario ajustado: ",novo_salario)
elif salario >701 and salario <=1500:
    novo_salario = salario * 1.10
    valor_aumento = novo_salario - salario
    print("Salario atual: ",salario)
    print("Percentual de ajuste salarial 10%")
    print("valor do aumento igual a: ",valor_aumento)
    print("Salario ajustado: ",novo_salario)
else:
    novo_salario = salario * 1.05
    valor_aumento = novo_salario - salario
    print("Salario atual: ",salario)
    print("Percentual de ajuste salarial 5%")
    print("valor do aumento igual a: ",valor_aumento)
    print("Salario ajustado: ",novo_salario)
    
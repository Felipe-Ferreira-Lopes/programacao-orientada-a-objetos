horas_trabalhadas = float (input("Digite a quantidade de horas trabalhadas: "))
dinheiro_hora = float (input("Digite a quantidade recebida por hora de trabalho: "))
salario_bruto = horas_trabalhadas * dinheiro_hora
'''No exemplo disposto pelo senhor você colocou parenteses como (5 * 220), que acredito eu sejam apenas para exemplificação
por conta disso eu apresentei os resultados e os descontos assim como você pediu so que sem colocar o valor das variaveis
dentro dos prints....'''
if salario_bruto <= 900:
    print("salario bruto: R$ ",salario_bruto)
    '''esse valor abaixo de 900 reais esta insento de IR então nao coloquei nenhum print dedicado a ele :)'''
    INSS = salario_bruto * 0.10
    print("(-) INSS: R$",INSS)
    FGTS = salario_bruto * 0.11
    print("FGTS: R$",FGTS)
    print("Total de descontos: R$",INSS)
    salario_liquido = salario_bruto - INSS
    print("Salario liquido: R$",salario_liquido)
elif salario_bruto > 901 and salario_bruto <=1500:
    print("salario bruto: R$",salario_bruto)
    IR = salario_bruto *0.05
    print("(-) IR: R$",IR)
    INSS = salario_bruto * 0.10
    print("(-) INSS: R$",INSS)
    FGTS = salario_bruto * 0.11
    print("FGTS: R$",FGTS)
    print("Total de descontos: R$",INSS + IR)
    salario_liquido = salario_bruto - (INSS + IR)
    print("Salario liquido: R$",salario_liquido)
elif salario_bruto > 1501 and salario_bruto <=2500:
    print("salario bruto: R$",salario_bruto)
    IR = salario_bruto *0.10
    print("(-) IR: R$",IR)
    INSS = salario_bruto * 0.10
    print("(-) INSS: R$",INSS)
    FGTS = salario_bruto * 0.11
    print("FGTS: R$",FGTS)
    print("Total de descontos: R$",INSS + IR)
    salario_liquido = salario_bruto - (INSS + IR)
    print("Salario liquido: R$",salario_liquido)
else:
    print("salario bruto: R$",salario_bruto)
    IR = salario_bruto *0.20
    print("(-) IR: R$",IR)
    INSS = salario_bruto * 0.10
    print("(-) INSS: R$",INSS)
    FGTS = salario_bruto * 0.11
    print("FGTS: R$ ",FGTS)
    print("Total de descontos: R$",INSS + IR)
    salario_liquido = salario_bruto - (INSS + IR)
    print("Salario liquido: R$",salario_liquido)

    
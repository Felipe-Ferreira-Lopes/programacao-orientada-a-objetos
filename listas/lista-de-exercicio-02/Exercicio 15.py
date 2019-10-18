dinheiro_hora = float(input("Digite quanto ganha por hora de trabalho: "))
horas_trabalho_mes = int(input("Digite quantas horas de trabalho por mes: "))
salario_bruto = dinheiro_hora*horas_trabalho_mes
imposto_de_renda = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = (((salario_bruto - imposto_de_renda)-inss)-sindicato)
print("Salario bruto: ",salario_bruto)
print("imposto de renda: ",imposto_de_renda)
print("inss: ",inss)
print("sindicato: ",sindicato)
print("salario liquido: ",salario_liquido)

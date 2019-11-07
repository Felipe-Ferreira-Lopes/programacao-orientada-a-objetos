arquivo_amazon = open('amazon.csv')
print("Informe os anos para calcular a quantidade de queimadas que ocorreram no brasil")
ano_inicio = str(input('Informe ano inicial: '))
ano_fim = str(input('Informe ano de termino: '))

queimadas_acre = 0	
queimadas_ceara = 0
queimadas_amazonas = 0
queimadas_mato_grosso = 0
queimadas_brasil = 0
for linha in arquivo_amazon:
	linha = linha.strip('\n')
	ano, estado, mes, numero, data = linha.split(',')
	numero = numero.replace(".", "")
	estado= estado.replace('"','')
	#print("ano {}, mes {}, numero {}, data {}".format(ano, mes, numero, data))
	if estado == 'Acre' and ano == '2015':
		queimadas_acre = queimadas_acre + int(numero)

	elif estado == 'Ceara' and ano == '2014':
		queimadas_ceara = queimadas_ceara + int(numero)

	elif estado == 'Amazonas':
		queimadas_amazonas = queimadas_amazonas + int(numero)

	elif estado == 'Mato Grosso':
		if int(ano) >= 2010: 
			queimadas_mato_grosso = queimadas_mato_grosso + int(numero)


	elif ano >= ano_inicio and ano <= ano_fim:
		queimadas_brasil = queimadas_brasil + int(numero)
		
	

print("queimadas: {}".format(queimadas_acre))		
print("queimadas: {}".format(queimadas_ceara))
print("queimadas: {}".format(queimadas_amazonas))
print("queimadas: {}".format(queimadas_mato_grosso))
print('No Brasil, ocorreram {} queimadas entre os anos {} e {}'.format(queimadas_brasil, ano_inicio, ano_fim))
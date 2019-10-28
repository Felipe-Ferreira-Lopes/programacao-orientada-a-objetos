'''Pesquisei um pouco sobre maneiras melhores de fazer esse programa e achei o "listOfstrings"
para nao ter que ficar repetindo varios espaços de ("") para cada letra do alfabeto, se não for permitido usar
conteudos nao dados em aula me desculpa :)'''
listOfstrings = ['A','E','I','O','U']
'''mesmo esquema pra evitar falha por letras minusculas ^^ '''
listOfstrings2 = ['a','e','i','o','u']
letra = str (input("Digite uma letra: "))
if letra in listOfstrings:
    print("Vogal")
elif letra in listOfstrings2:
    print("Vogal")
elif letra not in listOfstrings:
    print("consoante")
elif letra not in listOfstrings2:
    print("consoante")

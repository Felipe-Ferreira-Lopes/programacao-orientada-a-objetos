nota = float (input("Digite a primeira nota: "))
nota2 = float (input("Digite a segunda nota: "))
media = (nota + nota2)/2
if media >=9 and media <=10:
    print("Nota 1: ",nota)
    print("Nota 2: ",nota2)
    print("Media: ",media)
    print("Conceito A")
    print("Aprovado")
elif media >=7.5 and media <=8.9:
    print("Nota 1: ",nota)
    print("Nota 2: ",nota2)
    print("Media: ",media)
    print("Conceito B")
    print("Aprovado")
elif media >=6 and media <=7.4:
    print("Nota 1: ",nota)
    print("Nota 2: ",nota2)
    print("Media: ",media)
    print("Conceito C")
    print("Aprovado")
elif media >=4 and media <=5.9:
    print("Nota 1: ",nota)
    print("Nota 2: ",nota2)
    print("Media: ",media)
    print("Conceito D")
    print("Reprovado")
elif media >=0 and media <=3.9:
    print("Nota 1: ",nota)
    print("Nota 2: ",nota2)
    print("Media: ",media)
    print("Conceito E")
    print("Reprovado")
    '''para o caso de alguem digitar notas que nao estejam entre 0-10'''
else:
    print("Notas invalidas")




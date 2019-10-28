nota = float (input("Primeira nota: "))
nota2 = float (input("Segunda nota: "))
media = (nota+nota2)/2
if media >=7 and media <10:
    print("Aprovado")
elif media <=6.9:
    print("Reprovado")
elif media == 10:
    print("Aprovado com Distinção")
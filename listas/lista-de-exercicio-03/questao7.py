numero = float (input("Digite o primeiro numero: "))
numero2 = float (input("Digite o segundo numero: "))
numero3 = float (input("Digite o terceiro numero: "))
if numero > numero2 and numero > numero3:
    print("Maior: ",numero)
elif numero2 > numero and numero2 > numero3:
    print("Maior: ",numero2)
elif numero3 > numero2 and numero3 > numero:
    print("Maior: ",numero3)
if numero < numero2 and numero < numero3:
    print("Menor: ",numero)
elif numero2 < numero and numero2 < numero3:
    print("Menor: ",numero2)
elif numero3 < numero2 and numero3 < numero:
    print("Menor: ",numero3)
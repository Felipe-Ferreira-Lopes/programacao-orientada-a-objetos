numero = float (input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

if numero > numero2 and numero > numero3:
    if numero2 > numero3:
        print("",numero)
        print("",numero2)
        print("",numero3)
    if numero3 > numero2:
        print("",numero)
        print("",numero3)
        print("",numero2)
elif numero2 > numero and numero2 > numero3:
    if numero > numero3:
        print("",numero2)
        print("",numero)
        print("",numero3)
    if numero3 > numero:
        print("",numero2)
        print("",numero3)
        print("",numero)
elif numero3 > numero2 and numero3 > numero:
    if numero2 > numero:
        print("",numero3)
        print("",numero2)
        print("",numero)
    if numero > numero2:
        print("",numero3)
        print("",numero)
        print("",numero2)

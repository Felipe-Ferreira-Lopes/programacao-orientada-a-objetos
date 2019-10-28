turno = str (input("Digite o turno de estudo por favor leve em consideração a seguinte ordem, M (Matutino), V (Vespertino) ou N (Noturno): "))
if turno == ("M") or turno == ("m"):
    print("Bom Dia!")
elif turno == ("V") or turno == ("v"):
    print("Boa Tarde!")
elif turno == ("N") or turno == ("n"):
    print("Boa Noite!")
else:
    print("Valor invalido!")
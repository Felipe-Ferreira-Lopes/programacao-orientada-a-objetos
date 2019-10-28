primeiro_lado = float (input("Digite o primeiro lado: "))
segundo_lado = float (input("Digite o segundo lado: "))
terceiro_lado = float (input("Digite o terceiro lado: "))
'''Sei que nao e o recomendado por conta de estetica deixar linhas assim tão grandes, no entanto nao estava dando
certo quebrar a linha e continuar em baixo por algum motivo que nao entendi, o programa esta funcionando
e pretendo perguntar em sala sobre esse erro (se me lembrar).'''
if (primeiro_lado + segundo_lado) > terceiro_lado or (primeiro_lado + terceiro_lado) > segundo_lado or (segundo_lado + primeiro_lado) > terceiro_lado or (segundo_lado + terceiro_lado) > primeiro_lado or (terceiro_lado + primeiro_lado) > segundo_lado or (terceiro_lado + segundo_lado) > primeiro_lado:
 
     if primeiro_lado == segundo_lado and primeiro_lado == terceiro_lado:
         print("Triangulo equilatero")
     elif primeiro_lado == segundo_lado or primeiro_lado == terceiro_lado or segundo_lado == terceiro_lado:
         print("Triangulo isosceles")
     elif primeiro_lado != segundo_lado and primeiro_lado != terceiro_lado and segundo_lado != terceiro_lado:
         print("Triangulo Escaleno")
else:
    ("Não pode ser triangulo")
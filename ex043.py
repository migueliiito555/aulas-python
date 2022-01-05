from time import sleep
from cores import Cor


cor = Cor()


print(f"{cor.ar}>" * 162)
print(f"{cor.b + cor.n}{'IMC' :^150}")
print(f"{cor.ar}<" * 162, cor.a)



print()
imc = float(input("Digite seu peso: ")) / float(input("Agora sua altura: ")) ** 2



print()
print(f"{cor.azc}*" * 59, cor.a)
print()



print("Seu IMC é", end = "")
sleep(1)
print(".", end = "")
sleep(1)
print(".", end = "")
sleep(1)
print(". ", cor.n, end = "")
if imc < 18.5:
    print(f"{cor.c}ABAIXO DO PESO{cor.a}!")

elif imc < 25:
    print(f"{cor.vd}PESO IDEAL{cor.a}!")

elif imc < 30:
    print(f"{cor.vd}SOBREPESO{cor.a}!")

elif imc < 40:
    print(f"{cor.mc}OBESIDADE{cor.a}!")

else:
    print(f"{cor.m}OBESIDADE MÓRBIDA{cor.a}!")

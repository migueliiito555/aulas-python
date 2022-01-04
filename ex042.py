from cores import Cor


cor = Cor()


print(f"{cor.vr}*" * 59)
print(f"{cor.b + cor.n}{'ANALISADOR DE TRIÂNGULOS' :^59}{cor.a}")
print(f"{cor.vr}*" * 59, cor.a)


print()
l1 = float(input("Insira o comprimento do primeiro lado do triângulo: "))
l2 = float(input("Agora o comprimento do segundo: "))
l3 = float(input("Só falta o terceiro: "))



print()
print(f"{cor.vd}=" * 59, cor.a)



print()
if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
    print(f"Este triângulo {cor.n + cor.vr}NÃO PODE{cor.a} existir!")
    exit()

else:
    print(f"Este triângulo {cor.n + cor.vd}PODE{cor.a} existir!")



    print()
    print(f"{cor.vd}=" * 59, cor.a)
    print()



    if l1 == l2 == l3:
        print(f"Ele forma um triângulo {cor.ar}equilátero{cor.a}!")

    elif l1 == l2 or l1 == l3 or l2 == l3:
        print(f"Ele forma um triângulo {cor.m}isósceles{cor.a}!")

    else:
        print(f"Ele forma um triângulo {cor.c}escaleno{cor.a}!")

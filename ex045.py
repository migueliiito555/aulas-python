from random import randint
from time import sleep
from cores import Cor


cor = Cor()


print(f"{cor.az}*" * 162)
print(f"{cor.colorir('JOKENPÔ') :^200}")
print(f"{cor.az}*" * 162, cor.a, "\n")


jokenpo = [f"{cor.az + cor.n}PEDRA{cor.a}", f"{cor.n}PAPEL{cor.a}", f"{cor.vr + cor.n}TESOURA{cor.a}"]
opcPc = randint(1, 3)
opc = int(input(f"""ESCOLHA:

[ {cor.az}1{cor.a} ] - {cor.az + cor.n}Pedra{cor.a}
[ 2 ] - {cor.n}Papel{cor.a}
[ {cor.vr}3{cor.a} ] - {cor.vr + cor.n}Tesoura{cor.a}

{cor.n}-->{cor.a + cor.vd} """))


print(cor.a)
print(f"{cor.arc}=" * 162, cor.a)


print(f"{cor.n}COMPUTANDO", end = "")
sleep(1)
print(".", end = "")
sleep(1)
print(".", end = "")
sleep(1)
print(".")
sleep(1)


print()
print(f"{cor.arc}=" * 162, cor.a)
print("\n\n")


if opc == opcPc:
    print(f"{cor.ar}=" * 77, end = "")
    print(f" {cor.n}EMPATE!{cor.a} ", end = "")
    print(f"{cor.ar}=" * 76)

elif opc == 1 and opcPc == 3 or opc == 2 and opcPc == 1 or opc == 3 and opcPc == 2:
    print(cor.colorir(">" * 74), end = "")
    print(f" {cor.vd + cor.n}VOCÊ VENCEU!{cor.a} ", end = "")
    print(cor.colorir("<" * 74))

elif opc == 1 and opcPc == 2 or opc == 2 and opcPc == 3 or opc == 3 and opcPc == 1:
    print(f"{cor.n}<" * 74, end = "")
    print(f" {cor.vr + cor.n}VOCÊ PERDEU!{cor.a} ", end = "")
    print(f"{cor.n}>" * 74)

else:
    print(f"{cor.vr + cor.n}[ERRO]{cor.b} Opção Inválida!{cor.a}")
    exit()


print(f"""{cor.a}
{cor.n}VOCÊ: {jokenpo[opc - 1]}
{cor.n}PC: {jokenpo[opcPc - 1]}""", cor.a)

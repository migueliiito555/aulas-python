from cores import cor
from time import sleep


print(f"{cor['vr']}=" * 21, end =  " ")
print(f"{cor['br'] + cor['neg']} CONVERSOR DE BASES {cor['reset']}", end = "")
print(f"{cor['vr']}=" * 21, cor['reset'])


print()
num = int(input("Insira um número inteiro: "))


print()
print(f"{cor['vd']}=" * 62, cor["reset"])


base = int(input("""
Escolha:

[ 1 ] - Hexadecimal;
[ 2 ] - Binário;
[ 3 ] - Octal.

--> """))


print()
print(f"{cor['vd']}=" * 62, cor["reset"], "\n")


print("Convertendo", end = "")
sleep(1)
print(".", end = "")
sleep(1)
print(".", end = "")
sleep(1)
print(".\n")
sleep(1)


print(f"{cor['vd']}=" * 62, cor["reset"], "\n")


if base == 1:
    print(f"{num} em {cor['am']}hexadecimal{cor['reset']} é {cor['neg'] + hex(num)[2:].upper() + cor['reset']}")

elif base == 2:
    print(f"{num} em {cor['vd']}binário{cor['reset']} é {cor['neg'] + bin(num)[2:] + cor['reset']}")

elif base == 3:
    print(f"{num} em {cor['ma']}octal{cor['reset']} é {cor['neg'] + oct(num)[2:] + cor['reset']}")

else:
    print(f"{cor['vr'] + cor['neg']}[ERRO]{cor['reset'] + cor['neg']} Opção inválida!{cor['reset']}")

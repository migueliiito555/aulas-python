from time import sleep
from random import choice

a1 = str(input("Insira o nome do 1º aluno: "))
a2 = str(input("Do 2º aluno: "))
a3 = str(input("Do 3º aluno: "))
a4 = str(input("Do 4º aluno: "))


print()
print("=" * 20, "\n")


print("O aluno escolhido foi", end="")
sleep(0.5)

print(".", end="")
sleep(0.5)

print(".", end="")
sleep(0.5)

print(".")
sleep(0.5)

print()

print(f"{choice([a1, a2, a3, a4])}!!!")

from time import sleep
from cores import cor


print(f"{cor['vr']}=" * 19, end = "")
print(f"{cor['br'] + cor['neg']} CLASSIFICANDO ALUNOS {cor['reset']}", end = "")
print(f"{cor['vr']}=" * 19, cor['reset'], "\n")


n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Agora a segunda nota: "))
m = (n1 + n2) / 2


print()
print(f"{cor['vd']}=" * 60, cor['reset'], "\n")


print("O estado deste aluno é", end = "")
sleep(1)
print(".", end = "")
sleep(1)
print(".", end = "")
sleep(1)
print(".", end = "")
sleep(1)


print(cor['neg'], end = " ")
if m < 5:
    print(f"{cor['vr']}REPROVADO{cor['reset']}!")

elif m < 6.9:
    print(f"{cor['am']}RECUPERAÇÃO{cor['reset']}!")

elif m < 10:
    print(f"{cor['vd']}APROVADO{cor['reset']}!")

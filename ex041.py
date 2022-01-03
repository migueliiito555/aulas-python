from time import localtime
from cores import cor


print(f"{cor['ci']}=" * 21, end = "")
print(f"{cor['br'] + cor['neg']} CONF. NACIONAL DE NATAÇÃO {cor['reset']}", end = "")
print(f"{cor['ci']}=" * 21, cor['reset'], "\n")


idade = localtime().tm_year - int(input("Insira seu ano de nascimento: "))


print()
print(f"Você se enquadra no {cor['neg']}", end = "")
if idade <= 9:
    print(f"{cor['ci']}MIRIM", end = "")

elif idade <= 14:
    print(f"{cor['az']}INFANTIL", end = "")

elif idade <= 19:
    print(f"{cor['am']}JÚNIOR", end = "")

elif idade == 20:
    print(f"{cor['ma']}SÊNIOR", end = "")

else:
    print(f"{cor['inv']}-MASTER-", end = "")

print(f"{cor['reset']}!")

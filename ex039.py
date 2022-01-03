from time import localtime
from cores import cor


print(f"{cor['vd']}=" * 59)
print(f"{cor['br'] + cor['neg']}{'ALISTAMENTO MILITAR':^59}{cor['reset']}")
print(f"{cor['vd']}=" * 59, cor['reset'])
print()


idade = localtime().tm_year - int(input("Insira o seu ano de nascimento: "))


print()
if idade < 0:
    print(f"{cor['vr'] + cor['neg']}[ERRO]{cor['br']} Ano inserido é maior que o atual!{cor['reset']}")

elif idade < 18:
    print(f"Você possui {cor['ci'] + cor['neg']}{idade} anos{cor['reset']}, espere por {18 - idade} ano(s)!")

elif idade == 18:
    print(f"Você possui {cor['vd'] + cor['neg']}18 anos{cor['reset']}, você {cor['neg']}já pode{cor['reset']} se alistar!")

else:
    print(f"Você possui {cor['ma'] + cor['neg']}{idade} anos{cor['reset']}, {cor['neg']}já passou {cor['reset'] + cor['vr']}{idade - 18}{cor['reset']} ano(s)!")

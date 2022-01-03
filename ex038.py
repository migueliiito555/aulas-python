from cores import cor


print(f"{cor['vd']}=" * 25, end = "")
print(f"{cor['br'] + cor['neg']} COMPARADOR ", end = "")
print(f"{cor['vd']}=" * 25, cor['reset'], "\n")


n1 = float(input("Digite um número: "))
n2 = float(input("Mais um: "))



print()
print(f"{cor['vd']}=" * 62, cor['reset'])
print()



if n1 > n2:
    print(f"O {cor['vr'] + cor['neg']}primeiro{cor['reset']} valor é maior!")

elif n2 > n1:
    print(f"O {cor['am'] + cor['neg']}segundo{cor['reset']} valor é maior!")

else:
    print(f"{cor['vr'] + cor['neg']}Não existe{cor['reset']} valor maior, os dois são {cor['vd'] + cor['neg']}iguais{cor['reset']}.")

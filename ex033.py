maior = menor = n1 = float(input("Digite um número: "))
n2 = float(input("Outro número: "))
n3 = float(input("Mais um número: "))


print()


if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3

if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3


print(f"O maior número é {maior} e o menor é {menor}!")
#print(f"O maior número é {max(n1, n2, n3)} e o menor é {min(n1, n2, n3)}")

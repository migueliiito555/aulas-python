soma = 0


for i in range(0, 6):
    num = int(input("Insira um número: "))
    if (num % 2 == 0):
        soma += num

print(f"\nA soma dos números pares é igual à {soma}!")

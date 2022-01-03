from math import trunc

num = int(input("Digite um número de 0 - 9999: "))

print()
print("=" * 20)

print(f"""
Milhar: {num // 1000 % 10}
Centena: {num // 100 % 10}
Dezena: {num // 10 % 10}
Unidade: {num // 1 % 10}
""")

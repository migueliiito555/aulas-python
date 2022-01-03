from cores import cor


print(f"{cor['vd']}=" * 20, end="")
print(f"{cor['neg']}{cor['br']} EMPRÉSTIMO BANCÁRIO {cor['reset']}", end="")
print(f"{cor['vd']}=" * 20, cor["reset"])


print()
prestacaoMensal = float(input("Digite o valor da casa: R$")) / (int(input("Em quantos anos irá pagar? ")) * 12)
salario = float(input("Qual o seu salário? R$"))


print()
print(f"{cor['vr']}=" * 61, cor["reset"])


print()
if prestacaoMensal > salario * 1.3:
    print(f"Prestação mensal {cor['vr'] + cor['neg']}excede{cor['reset']} 30% do salário! Empréstimo negado!!!")

else:
    print(f"Empréstimo {cor['vd'] + cor['neg']}aceito{cor['reset']}!!!")

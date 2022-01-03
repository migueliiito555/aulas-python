salario = float(input("Digite seu salário: "))


print()


if salario <= 1250:
    print(f"Você recebeu um aumento de 10%, então o seu salário agora é de R${salario + (salario * 0.1) :.2f}!")

else:
    print(f"Você recebeu um aumento de 15%, então o seu salário agora é de R${salario + (salario * 0.15)}!")

vel = int(input("Digite a velocidade do seu carro em km: "))


print()


if vel > 80:
    print(f"Seu carro foi multado! Por R${(vel - 80) * 7}!")

else:
    print("Dirija com cuidado!")

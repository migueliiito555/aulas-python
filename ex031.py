distancia = float(input("Digite a distância da viagem em km: "))

print()

if distancia <= 200:
    print(f"O preço da viagem será de R${distancia * 0.5 :.2f}!")

else:
    print(f"O preço da viagem será de R${distancia * 0.45 :.2f}!")

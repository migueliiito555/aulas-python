dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos quilômetros rodados? "))

print(f"\nVocê deve pagar R${60 * dias + km * 0.15 :.2f}!")

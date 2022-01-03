cidade = str(input("Digite o nome da sua cidade: ").strip())

print()
print("=" * 40)

print(f"\nSua cidade começa com SANTO? {'santo' in cidade.split()[0].lower()}")

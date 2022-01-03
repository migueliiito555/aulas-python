nome = str(input("Digite seu nome completo: ").strip())

print()
print("=" * 20)

print(f"""
{nome.upper()}
{nome.lower()}
{len(nome.replace(' ', ''))} letras
{len(nome.split()[0])} letras no 1º nome
""")

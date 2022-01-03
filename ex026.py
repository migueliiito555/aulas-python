frase = str(input("Digite uma frase: ").strip().lower())

print()
print("=" * 40)

print(f"""
Quantas vezes aparece \"A\"? {frase.count('a')}
1ª vez: {frase.find('a')}
Última vez: {frase.find('a', -1)}
""")

from math import hypot

cat1 = float(input("Digite o comprimento do cateto oposto deste triângulo: "))
cat2 = float(input("Digite o comprimento do cateto adjacente deste triângulo: "))

print(f"\nO comprimento da hipotenusa deste triângulo é {hypot(cat1, cat2)}!")

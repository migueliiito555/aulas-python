from math import sin, cos, tan, degrees

angulo = float(input("Insira o valor do ângulo qualquer: "))

print("=" * 20, "\n")

print(f"Seno      ≅  {degrees(sin(angulo)) :.3f}°")
print(f"Cosseno   ≅  {degrees(cos(angulo)) :.3f}°")
print(f"Tangente  ≅  {degrees(tan(angulo)) :.3f}°\n")

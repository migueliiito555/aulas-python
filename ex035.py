from cores import cor


l1 = float(input("Digite o comprimento do lado do triângulo: "))
l2 = float(input("Digite do outro lado do triângulo: "))
l3 = float(input("Agora do outro lado do triângulo: "))


print()


if l1 + l2 < l3 or l2 + l3 < l1 or l1 + l3 < l2:
    print(f"Este triângulo {cor['vr']}NÃO{cor['reset']} pode existir!")

else:
    print("Este triângulo pode existir!")

from time import sleep
from random import randint


num = randint(0, 5)


print("Pensando num número", end="")
sleep(1)
print(".", end="")
sleep(1)
print(".", end="")
sleep(1)
print(".")


print()
print("-=-" * 15, "\n")


numUser = int(input("Digite um número de 0 - 5: "))


print()
print("-=-" * 15, "\n")


if numUser == num:
    print("Você acertou!")

else:
    print("Você errou!")
    print(f"PC: {num}")
    print(f"Você: {numUser}")


print()

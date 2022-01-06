from time import sleep
from cores import Cor


cor = Cor()


print(cor.colorir("X" * 162), end = "")
print(f"{cor.n}{'FELIZ ANO NOVO' :^162}{cor.a}")
print(cor.colorir("X" * 162), cor.a)


for i in range(10, -1, -1):
    if i < 10:
        print(f"{cor.colorir(f'0{i}') :^177}")

    else:
        print(f"{cor.colorir(f'{i :2}') :^177}")


    sleep(1)

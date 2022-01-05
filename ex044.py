from time import sleep
from cores import Cor



cor = Cor()



print(f"{cor.c}*" * 162)
print(f"{cor.b + cor.n}{'PREÇO DE UM PRODUTO' :^162}")
print(f"{cor.c}*" * 162, cor.a)



print()
preco = float(input(f"Insira o valor do produto: {cor.vd}R$"))
print(cor.a)



print(f"{cor.vd}=" * 162)
print(cor.a)



metodo = int(input(f"""Agora escolha o método de pagamento:

[ {cor.vd}1{cor.a} ] - À vista
[ {cor.vd}2{cor.a} ] - Cartão
[ {cor.vd}3{cor.a} ] - 2x no cartão
[ {cor.vd}4{cor.a} ] - 3x ou + no cartão

--> """))



print()
print(f"{cor.c}=" * 162)
print(cor.a)



if metodo == 1:
    print(f"R${preco :.2f} {cor.vd}à vista{cor.a} sairá {cor.vd}R${preco * 0.9 :.2f}{cor.a}!")

elif metodo == 2:
    print(f"R${preco :.2f} no {cor.vr}cartão{cor.a} sairá {cor.vd}R${preco * 0.95 :.2f}{cor.a}!")

elif metodo == 3:
    print(f"R${preco :.2f} em {cor.mc}2x no cartão{cor.a} sairá {cor.vd}R${preco :.2f}{cor.a}!")

elif metodo == 4:
    print(f"R${preco :.2f} em {cor.m}3x ou mais no cartão{cor.a} sairá {cor.vd}R${preco * 1.2 :.2f}{cor.a}!")

else:
    print(f"{cor.vr + cor.n}[ERRO]{cor.b} OPÇÃO INVÁLIDA!{cor.a}")

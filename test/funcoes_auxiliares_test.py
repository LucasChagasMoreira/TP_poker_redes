import sys
sys.path.append('../src')

from funcoes_auxiliares import *

# Exemplo de uso:
a = [('Ás', 'Copas'), ('Ás', 'Paus')]
b = [('Ás', 'Espadas'), ('Rei', 'Ouros'), ('Rei', 'Paus')]

if possui_dupla(a+b):
    print("O jogador possui uma dupla!")
else:
    print("O jogador não possui uma dupla.")


if possui_trinca(a+b):
    print("O jogador possui uma trinca!")
else:
    print("O jogador não possui uma trinca.")


if possui_full_house(a+b):
    print("O jogador possui um Full House!")
else:
    print("O jogador não possui um Full House.")

# Exemplo de uso:
mao_jogador = [('10', 'Copas'), ('8', 'Paus'), ('9', 'Espadas'), ('7', 'Ouros'), ('6', 'Paus')]

if possui_straight(mao_jogador):
    print("O jogador possui um straight!")
else:
    print("O jogador não possui um straight.")

# Exemplo de uso:
mao_jogador = [('10', 'Copas'), ('8', 'Copas'), ('9', 'Copas'), ('7', 'Copas'), ('6', 'Copas')]

if possui_straight_flush(mao_jogador):
    print("O jogador possui um straight flush!")
else:
    print("O jogador não possui um straight flush.")


# Exemplo de uso:
mao_jogador = [('10', 'Copas'), ('Valete', 'Copas'), ('Rainha', 'Copas'), ('Rei', 'Copas'), ('Ás', 'Copas')]

if possui_royal_flush(mao_jogador):
    print("O jogador possui um Royal Flush!")
else:
    print("O jogador não possui um Royal Flush.")


# Exemplo de uso:
mao_jogador = [('Ás', 'Copas'), ('Rei', 'Paus'), ('Ás', 'Espadas'), ('Rei', 'Ouros'), ('10', 'Paus')]

if possui_dois_pares(mao_jogador):
    print("O jogador possui dois pares!")
else:
    print("O jogador não possui dois pares.")

# Exemplo de uso:
mao_jogador = [('Ás', 'Copas'), ('Rei', 'Copas'), ('10', 'Copas'), ('7', 'Copas'), ('4', 'Copas')]

if possui_flush(mao_jogador):
    print("O jogador possui um flush!")
else:
    print("O jogador não possui um flush.")



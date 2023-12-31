from Deck import Deck
from jogador import jogador

def menu():
    num = int(input("digite quantos pessoas irao jogar o jogo (de 1 a 6):\n"))
    return num

def addjogadores(mesa,num):
    for i in range(num):
        nome = input(f'digite o nome do jogador {i}:')
        aux = jogador(nome,1000,0)
        mesa.Adiciona_jogador(aux)

def exibirjogadores(mesa):
    for i in range(mesa.quantidadedejogadores()):
        print(f'jogador {i+1}: ')
        print(f'nome: {mesa._lista_de_jogadores[i].nome}')
        print(f'fichas: {mesa._lista_de_jogadores[i].fichas}')

def menu_jogada():
    print("Escolha uma opçao: \n")
    print("1 - holdar")
    print("2 - desistir")
    print("3 - call")
    print("4 - aumentar")
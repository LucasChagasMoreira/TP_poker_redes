from Deck import Deck
from jogador import jogador
from funcoes_auxiliares import *

class Mesa:
    # construtor da classe. Recebe apenas as fichas como parametro e inicializa um vetor e um Deck
    def __init__(self,fichas):
        self._cartas = Deck()
        self._lista_de_jogadores = []
        self._fichas = fichas
        
    # função que adiciona jogadores ao vetor de jogadores
    def Adiciona_jogador(self, jogador):
        self._lista_de_jogadores.append(jogador)
    # função que remove jogadores do vetor de jogadores
    def Remover_jogador(self, jogador,indice):
        self._lista_de_jogadores.pop(indice)

    #funçao pricipal do jogo
    def Iniciar_jogo(self):
        num = menu()
        addjogadores(self,num)
        exibirjogadores(self)
            
    
    def quantidadedejogadores(self):
        return len(self._lista_de_jogadores)

    @property
    def fichas(self):
        return self._fichas

    # Setter para atualizar a quantidade de fichas do jogador
    @fichas.setter
    def fichas(self, novas_fichas):
        self._fichas = novas_fichas

    def __del__(self):
        del self._cartas
        for i in range(self.quantidadedejogadores()):
            del self._lista_de_jogadores[i]


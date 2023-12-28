from Deck import Deck
from jogador import jogador
def menu():
    num = int(input("digite quantos pessoas irao jogar o jogo (de 1 a 6):\n"))
    return num

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
        print(num)
        for i in range(num):         
            aux = jogador(1000,0)
            self.Adiciona_jogador(aux)
        for i in range (num):
            print(type(self._lista_de_jogadores[i]))


mesa = Mesa(0)
mesa.Iniciar_jogo()
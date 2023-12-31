from jogador import *


class Mesa:
    # construtor da classe. Recebe apenas as fichas como parametro e inicializa um vetor e um Deck
    def __init__(self,fichas):
        self._cartas = Deck()
        self._lista_de_jogadores = []
        self._fichas = fichas
    
    def exibirjogadores(self):
        for i in range(self.quantidadedejogadores()):
            print(f'jogador {i+1}: ')
            print(f'nome: {self._lista_de_jogadores[i].nome}')
            print(f'fichas: {self._lista_de_jogadores[i].fichas}')

    # adiciona varios jogadores em sequencia
    def addjogadores(self,num):
        for i in range(num):
            nome = input(f'digite o nome do jogador {i}:')
            aux = jogador(nome,1000,0)
            self.Adiciona_jogador(aux)

    # função que adiciona jogadores ao vetor de jogadores
    def Adiciona_jogador(self, jogador):
        self._lista_de_jogadores.append(jogador)
    # função que remove jogadores do vetor de jogadores
    def Remover_jogador(self, jogador,indice):
        self._lista_de_jogadores.pop(indice)

    #funçao pricipal do jogo
    def Iniciar_jogo(self):
        num = menu()
        self.addjogadores(num)
        self.exibirjogadores()

        print(self.quantidadedejogadores())
        for i in range(self.quantidadedejogadores()):
            print(f'jogador {self._lista_de_jogadores[i].nome}:')
            self._lista_de_jogadores[i].jogada()
        print(self.quantidadedejogadores())
            
    # Exibe os jogadores
    def quantidadedejogadores(self):
        return len(self._lista_de_jogadores)

    @property
    def fichas(self):
        return self._fichas

    # Setter para atualizar a quantidade de fichas do jogador
    @fichas.setter
    def fichas(self, novas_fichas):
        self._fichas = novas_fichas

 


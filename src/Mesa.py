from jogador import *


class Mesa:
    # construtor da classe. Recebe apenas as fichas como parametro e inicializa um vetor e um Deck
    def __init__(self,fichas):
        self._cartas = Deck()
        self._lista_de_jogadores = []
        self._fichas = fichas
    
    # exibe as fichas e os nomes dos jogaores
    def exibirjogadores(self):
        for i in range(self.quantidadedejogadores()):
            print(f'jogador {i+1}: ')
            print(f'nome: {self._lista_de_jogadores[i].nome}')
            print(f'fichas: {self._lista_de_jogadores[i].fichas}')

    # adiciona varios jogadores em sequencia
    def addjogadores(self,num):
        for i in range(num):
            nome = input(f'digite o nome do jogador {i+1}:')
            aux = jogador(nome,1000,0)
            self.Adiciona_jogador(aux)

    # função que adiciona jogadores ao vetor de jogadores
    def Adiciona_jogador(self, jogador):
        self._lista_de_jogadores.append(jogador)
    # função que remove jogadores do vetor de jogadores
    def Remover_jogador(self,indice):
        self._lista_de_jogadores.pop(indice)

    #funçao pricipal do jogo
    def Iniciar_jogo(self):
        num = menu()
        maioraposta = 0
        self.addjogadores(num)
        desistentes = []

        while(True):
            for j in range(3):
                print(f'rodada:{j+1}')
                
                for i in range(self.quantidadedejogadores()):
                    
                    print(f'jogador {self._lista_de_jogadores[i].nome}:')
                    menu_jogada()
                    escolha = input()
                    if escolha == "1":
                        self._lista_de_jogadores[i].holdar()

                    elif escolha == '2':
                        self._lista_de_jogadores[i].desistir()
                        desistentes.append(self._lista_de_jogadores[i])
                        self.Remover_jogador(i)

                    elif escolha == '3':
                        self._lista_de_jogadores[i].call(maioraposta)

                    elif escolha == '4':
                        aposta = int(input("digite o valor que deseja apostar"))
                        self._lista_de_jogadores[i].aumentar_apostar(aposta)
                        maioraposta = aposta

                
                self.exibir_acoes()
                print(f"fim da rodada {i + 1}")
            
            rodada = input("deseja jogar mais uma rodada? (Y/N)")
            if rodada == "Y":
                print("começando novo set")
            else:
                print("fim de jogo")
                break

    
    # Exibe os jogadores
    def quantidadedejogadores(self):
        return len(self._lista_de_jogadores)
    
    #menu que mostra as fichas dos jogadores
    def exibir_acoes(self):
        print(f'ações feitas')
        
        desenha_linha()
        for i in range(self.quantidadedejogadores()):
            print(f'jogadores: {self._lista_de_jogadores[i].nome} | ',end="")

        print()  
        desenha_linha()

        for i in range(self.quantidadedejogadores()):
            print(f'fichas: {self._lista_de_jogadores[i].fichas} | ', end="")
        
        print()
        desenha_linha()

        for i in range(self.quantidadedejogadores()):
            print(f'Apostadas: {self._lista_de_jogadores[i].fichasapostadas} | ', end="")
        
        print()
        desenha_linha()
        

    # getter de "_fichas"
    @property
    def fichas(self):
        return self._fichas

    # Setter para atualizar a quantidade de fichas do jogador
    @fichas.setter
    def fichas(self, novas_fichas):
        self._fichas = novas_fichas

 


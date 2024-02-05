from jogador import *


class Mesa:
    # construtor da classe. Recebe apenas as fichas como parametro e inicializa um vetor e um Deck
    def __init__(self,fichas):
        self._baralho = criar_baralho()
        self._cartas = []
        self._lista_de_jogadores = []
        self._fichas = fichas
    
    # adiciona cartas a mao da mesa
    def distribuir_cartas_comunitarias(self,qtd):
        aux = distribuir_cartas(self._baralho,qtd)
        for i in range(qtd):
            self._cartas.append(aux[i])

    # distribui 2 cartas para todos os jogadores
    def distribuir_cartas_para_jogadores(self):
        for i in range(self.quantidadedejogadores()):
            self._lista_de_jogadores[i]._cartas = (distribuir_cartas(self._baralho,2))



    # exibe as fichas e os nomes dos jogaores
    def exibirjogadores(self):
        for i in range(self.quantidadedejogadores()):
            print(f'Jogador {i+1}: ')
            print(f'Nome: {self._lista_de_jogadores[i].nome}')
            print(f'Fichas: {self._lista_de_jogadores[i].fichas}')

    # adiciona varios jogadores em sequencia
    def addjogadores(self,num):
        for i in range(num):
            nome = input(f'Digite o nome do jogador {i+1}:')
            aux = jogador(nome,1000,0)
            self.Adiciona_jogador(aux)

    # função que adiciona jogadores ao vetor de jogadores
    def Adiciona_jogador(self, jogador):
        self._lista_de_jogadores.append(jogador)

    # função que remove jogadores do vetor de jogadores
    def Remover_jogador(self,indice):
        self._lista_de_jogadores.pop(indice)

    # Exibe os jogadores
    def quantidadedejogadores(self):
        return len(self._lista_de_jogadores)
    
    # faz o desconto de todas as apostas
    def descontarapostas(self):
        for i in range(self.quantidadedejogadores()):
            self._lista_de_jogadores[i].descontaraposta()

    #retorna o indice de um jogador no vetor de jogadores baseado em seu nome
    def indice_jogador(self, nome_do_jogador):
        for i in range(self.quantidadedejogadores()):
            if nome_do_jogador == self._lista_de_jogadores[i].nome:
                return i
            
    # remove desistentes da rodada
    def removerdesistentes(self,desistentes):
        for i in range(len(desistentes)):
            indice_do_desistente = self.indice_jogador(desistentes[i])
            print(f'Jogador {self._lista_de_jogadores[indice_do_desistente].nome}, desistiu.')
            self.Remover_jogador(indice_do_desistente)

    def definir_vencedor(self):
        maos_dos_jogadores = []
        for i in range(self.quantidadedejogadores()):
            maos_dos_jogadores.append(verificar_mao(self._lista_de_jogadores[i]._cartas + self._cartas))
                
        mapeamento_de_maos = {'royale_flush': 9, 'straight_flush': 8, 'quadra': 7, 'full_house': 6, 'flush': 5, 'straight':4, 'trinca':3, 'dois_pares':2, 'dupla':1, 'carta_alta':0}
        #vetor numerico representando as maos dos jogadores
        valores_numericos = [mapeamento_de_maos[valor] for valor in maos_dos_jogadores]
        return valores_numericos

    def distribuir_para_vencedores(self,lista):
        indices = indices_do_maior(lista)
        aux = []

        #caso haja empate
        if len(indices) >= 2:
            for i in range(len(indices)):
               aux.append(carta_mais_alta(self._lista_de_jogadores[indices[i]]._cartas))
            indices_desempate = indices_do_maior(aux)
            print(indices)
            print(aux)
            print(indices_desempate)
            print(f'set do(s) jogadore(s): ')
            for i in range(len(indices_desempate)):
                self._lista_de_jogadores[indices[indices_desempate[i]]].fichas += (self.fichas / len(indices_desempate))
                print(f'{self._lista_de_jogadores[indices[indices_desempate[i]]].nome} recebeu: {self.fichas / len(indices_desempate)} fichas.')
        #caso nao haja empate
        else:
            print(f'set do(s) jogadore(s): ')
            for i in range(len(indices)):
                self._lista_de_jogadores[indices[i]].fichas += (self.fichas)
                print(f'{self._lista_de_jogadores[indices[i]].nome} recebeu: {self.fichas} fichas.')
                


    #funçao pricipal do jogo
    def Iniciar_jogo(self):
        num = menu()
        maioraposta = 0
        self.addjogadores(num)
        desistentes = []

        #copiando as posiçoes originais dos jogadores
        posiçoes_iniciais = []
        for i in range(self.quantidadedejogadores()):
            posiçoes_iniciais.append(self._lista_de_jogadores[i])

        while(True):
            self.distribuir_cartas_para_jogadores()
            for j in range(3):
                
                print(f'Rodada: {j+1}')
                print(f'Aposta atual: {maioraposta}.')
                desenha_linha()
                
                for i in range(self.quantidadedejogadores()):
                   self._lista_de_jogadores[i].exibir_cartas()
                   self.exibir_cartas_comunitarias()
                   desenha_linha()
                   resultado_jogada = self._lista_de_jogadores[i].jogada(maioraposta)
                   desenha_linha()

                   if resultado_jogada[0] == '1':
                        desistentes.append(self._lista_de_jogadores[i].nome)
                   elif resultado_jogada[0] == '2':
                       self.fichas += maioraposta
                   elif resultado_jogada[0] == '3':
                       maioraposta = resultado_jogada[1]
                       self.fichas += maioraposta


                self.exibir_acoes()
                self.descontarapostas()
                
                self.removerdesistentes(desistentes)
                desistentes.clear()

                if j == 0:
                    self.distribuir_cartas_comunitarias(3)
                else:
                    self.distribuir_cartas_comunitarias(1)


                print(f'Fim da rodada {j + 1}')
            
            valores_numericos = self.definir_vencedor()
            for i in range(self.quantidadedejogadores()):
                print(self._lista_de_jogadores[i]._cartas + self._cartas)

            print(valores_numericos)
           
            self.distribuir_para_vencedores(valores_numericos)

            rodada = input("Deseja jogar mais uma rodada? (Y/N)")

            if rodada == "Y":
                print("Começando novo set")

                #resetando variaveis de jogo
                self._cartas.clear()
                self.fichas = 0
                self.maioraposta = 0

                # colocando os jogadores na ordem original
                self._lista_de_jogadores.clear()
                for i in range(len(posiçoes_iniciais)):
                    self._lista_de_jogadores.append(posiçoes_iniciais[i])

                self.exibir_acoes()
            else:
                print("Fim de jogo")
                break
    
    #menu que mostra as fichas dos jogadores
    def exibir_acoes(self):
        print(f'Ações feitas')
        
        desenha_linha()
        for i in range(self.quantidadedejogadores()):
            print(f'Jogadores: {self._lista_de_jogadores[i].nome} | ',end="")

        print()  
        desenha_linha()

        for i in range(self.quantidadedejogadores()):
            print(f'Fichas: {self._lista_de_jogadores[i].fichas} | ', end="")
        
        print()
        desenha_linha()

        for i in range(self.quantidadedejogadores()):
            print(f'Apostadas: {self._lista_de_jogadores[i].fichasapostadas} | ', end="")
        
        print()
        desenha_linha()
        
        print(f'Fichas no pote: {self.fichas}.')
        desenha_linha()
        
    def exibir_cartas_comunitarias(self):
        print(f'Fichas comunitarias: {self._cartas}')

    # getter de "_fichas"
    @property
    def fichas(self):
        return self._fichas

    # Setter para atualizar a quantidade de fichas do jogador
    @fichas.setter
    def fichas(self, novas_fichas):
        self._fichas = novas_fichas

 


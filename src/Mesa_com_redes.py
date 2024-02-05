from jogador_com_redes import *


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
            print(f'jogador {i+1}: ')
            print(f'nome: {self._lista_de_jogadores[i].nome}')
            print(f'fichas: {self._lista_de_jogadores[i].fichas}')

    # adiciona varios jogadores em sequencia
    def addjogadores(self,jogadores):

        for i in jogadores:
            aux = jogador(i[1],1000,0)
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
    def removerdesistentes(self,desistentes,jogadores_auxiliar,jogadores_desistentes):
        for i in range(len(desistentes)):
            indice_do_desistente = self.indice_jogador(desistentes[i])
            print(f'jogador {self._lista_de_jogadores[indice_do_desistente].nome}, desistiu.')
            self.Remover_jogador(indice_do_desistente)

        jogadores_auxiliar = [elemento for elemento in jogadores_auxiliar if elemento not in jogadores_desistentes]
        return jogadores_auxiliar

    def definir_vencedor(self):
        maos_dos_jogadores = []
        for i in range(self.quantidadedejogadores()):
            maos_dos_jogadores.append(verificar_mao(self._lista_de_jogadores[i]._cartas + self._cartas))
                
        mapeamento_de_maos = {'royale_flush': 9, 'straight_flush': 8, 'quadra': 7, 'full_house': 6, 'flush': 5, 'straight':4, 'trinca':3, 'dois_pares':2, 'dupla':1, 'carta_alta':0}
        #vetor numerico representando as maos dos jogadores
        valores_numericos = [mapeamento_de_maos[valor] for valor in maos_dos_jogadores]
        
        return valores_numericos

    def distribuir_para_vencedores(self,lista,jogadores):
        indices = indices_do_maior(lista)
        aux = []

        #caso haja empate
        if len(indices) >= 2:
            for i in range(len(indices)):
               aux.append(carta_mais_alta(self._lista_de_jogadores[indices[i]]._cartas))
            indices_desempate = indices_do_maior(aux)
            for i in range(len(indices_desempate)):
                
                self._lista_de_jogadores[indices[indices_desempate[i]]].fichas += (self.fichas / len(indices_desempate))
                if(len(indices_desempate) == 1):
                    envia_para_todos(f'O jogador {self._lista_de_jogadores[indices[indices_desempate[i]]].nome} ganhou no desempate com a carta mais alta:{next(chave for chave, valor in mapeamento_valores.items() if valor == max(aux))}',jogadores)
        
                envia_para_todos(f'{self._lista_de_jogadores[indices[indices_desempate[i]]].nome} venceu e recebeu: {self.fichas / len(indices_desempate)} fichas.',jogadores)
        #caso nao haja empate
        else:
            for i in range(len(indices)):
                self._lista_de_jogadores[indices[i]].fichas += (self.fichas)
                envia_para_todos(f'{self._lista_de_jogadores[indices[i]].nome} venceu e recebeu: {self.fichas} fichas.',jogadores)
                


    #funçao pricipal do jogo
    def Iniciar_jogo(self,jogadores):
        
        maioraposta = 0
        self.addjogadores(jogadores)

        envia_para_todos(desenha_linha(),jogadores)
        envia_para_todos(f"jogadores presentes na mesa:\n",jogadores)
        for i in self._lista_de_jogadores:
            envia_para_todos(f"jogador: {i.nome} -- fichas: {i.fichas}",jogadores)

        desistentes = []
        jogadores_desistentes = []
        #copiando as posiçoes originais dos jogadores
        posiçoes_iniciais = []
        jogadores_auxiliar = []
        for i in range(self.quantidadedejogadores()):
            posiçoes_iniciais.append(self._lista_de_jogadores[i])
            jogadores_auxiliar.append(jogadores[i])


        while(True):
            self.distribuir_cartas_para_jogadores()
            for j in range(3):

                envia_para_todos(desenha_linha(),jogadores_auxiliar)
                envia_para_todos("Dados da rodada:",jogadores_auxiliar)
                envia_para_todos(f'Rodada: {j+1}',jogadores_auxiliar)
                envia_para_todos(f'Aposta atual: {maioraposta}.',jogadores_auxiliar)
                envia_para_todos(desenha_linha(),jogadores_auxiliar)
                
                for i in range(self.quantidadedejogadores()):
                   
                   envia_para_todos_menos_um(f"Aguardando a jogada do jogador {jogadores_auxiliar[i][1]}",jogadores_auxiliar,jogadores_auxiliar[i])
                   envia_para_todos(desenha_linha(),jogadores_auxiliar)
                   enviar_para_jogador(jogadores_auxiliar[i],self._lista_de_jogadores[i].exibir_cartas())
                   enviar_para_jogador(jogadores_auxiliar[i],self.exibir_cartas_comunitarias())
                   enviar_para_jogador(jogadores_auxiliar[i],desenha_linha())
                   resultado_jogada = self._lista_de_jogadores[i].jogada(maioraposta,jogadores_auxiliar[i])
                   enviar_para_jogador(jogadores_auxiliar[i],desenha_linha())

                   if resultado_jogada[0] == '1':
                        desistentes.append(self._lista_de_jogadores[i].nome)
                        jogadores_desistentes.append(jogadores_auxiliar[i])
                        envia_para_todos(f"O jogador {jogadores_auxiliar[i][1]} desistiu\n",jogadores_auxiliar)
                   elif resultado_jogada[0] == '2':
                       self.fichas += maioraposta
                       envia_para_todos(f"O jogador {jogadores_auxiliar[i][1]} pagou a mesa\n",jogadores_auxiliar)
                   elif resultado_jogada[0] == '3':
                       maioraposta = resultado_jogada[1]
                       self.fichas += maioraposta
                       envia_para_todos(f"O jogador {jogadores_auxiliar[i][1]} aumentou a aposta para {maioraposta}\n",jogadores_auxiliar)

                #descontar o dinheiro gasto pelos jogadores
                envia_para_todos(self.exibir_acoes(),jogadores)
                self.descontarapostas()
                
                #removendo desistentes temporarios
                jogadores_auxiliar = self.removerdesistentes(desistentes,jogadores_auxiliar,jogadores_desistentes)
                desistentes.clear()
                jogadores_desistentes.clear()

                if j == 0:
                    self.distribuir_cartas_comunitarias(3)
                else:
                    self.distribuir_cartas_comunitarias(1)


                envia_para_todos(f'Fim da rodada {j + 1}\n',jogadores)
                envia_para_todos(desenha_linha(),jogadores)
            ##################################################################################################            
            valores_numericos = self.definir_vencedor()
            envia_para_todos("melhores maos dos jogadores:",jogadores)
            for i in range(self.quantidadedejogadores()):
                mao_correspondente = next(chave for chave, valor in mapeamento_de_maos.items() if valor == valores_numericos[i])
                envia_para_todos(f"O jogador {self._lista_de_jogadores[i].nome} possui {mao_correspondente}",jogadores)

            envia_para_todos(f"mao mais forte presente: {next(chave for chave, valor in mapeamento_de_maos.items() if valor == max(valores_numericos))}",jogadores)
            print(valores_numericos)
           
            self.distribuir_para_vencedores(valores_numericos,jogadores)

            ##################################################################################################

            #gambiarra extrema para lidar com jogadores levando a sessao
            i = 0
            while i < len(jogadores):
                envia_para_todos_menos_um(f"Aguardando a resposta do jogador: {jogadores[i][1]}...",jogadores,jogadores[i])
                enviar_para_jogador(jogadores[i],"Deseja jogar mais uma rodada? (Y/N)")
                escolha = requisita_jogada(jogadores[i])

                if escolha == 'Y':
                    envia_para_todos_menos_um(f'jogador {jogadores[i][1]} ira participar da proxima rodada',jogadores,jogadores[i])
                    i += 1
                elif escolha == 'N':
                    envia_para_todos_menos_um(f'O jogador {jogadores[i][1]} ira se retirar da seçao',jogadores,jogadores[i])
                    enviar_para_jogador(jogadores[i],"encerrando...")
                    funcao_de_encerramento(jogadores[i])
                    jogadores.pop(i)
                    posiçoes_iniciais.pop(i)
                else:
                    enviar_para_jogador(jogadores[i],"faça uma escolha valida")
            

            envia_para_todos("Começando novo set",jogadores)

            #resetando variaveis de jogo
            self._cartas.clear()
            self.fichas = 0
            maioraposta = 0

            # colocando os jogadores na ordem original
            self._lista_de_jogadores.clear()
            for i in range(len(posiçoes_iniciais)):
                self._lista_de_jogadores.append(posiçoes_iniciais[i])
            
            jogadores_auxiliar.clear()
            for i in range(len(jogadores)):
                jogadores_auxiliar.append(jogadores[i])
            
            if len(jogadores) <= 1:
                envia_para_todos("a seçao presisa de mais de 1 jogador para ocorrer, portanto ela fechara",jogadores)
                funcao_de_encerramento(jogadores[0])
                return

    #menu que mostra as fichas dos jogadores
    def exibir_acoes(self):
        mensagem = ""
        mensagem += f'ações feitas\n'
        
        mensagem  += desenha_linha()
        mensagem += "\n"
        for i in range(self.quantidadedejogadores()):
            mensagem += f'jogadores: {self._lista_de_jogadores[i].nome} | '

        mensagem += "\n"  
        mensagem += desenha_linha()
        mensagem += "\n"

        for i in range(self.quantidadedejogadores()):
            mensagem += f'fichas: {self._lista_de_jogadores[i].fichas} | '
        
        mensagem += "\n"
        mensagem += desenha_linha()
        mensagem += "\n"

        for i in range(self.quantidadedejogadores()):
            mensagem += f'Apostadas: {self._lista_de_jogadores[i].fichasapostadas} | '
        
        mensagem += '\n'
        mensagem += desenha_linha()
        mensagem += "\n"

        mensagem += f'fichas no pote: {self.fichas}.\n'
        mensagem += desenha_linha()
        return mensagem
        
    def exibir_cartas_comunitarias(self):
        return f'Fichas comunitarias: {self._cartas}'

    def lob():
        server.listen()
                

    # getter de "_fichas"
    @property
    def fichas(self):
        return self._fichas

    # Setter para atualizar a quantidade de fichas do jogador
    @fichas.setter
    def fichas(self, novas_fichas):
        self._fichas = novas_fichas


def lobby():

    server.listen()
    print(f'[LISTENING] servidor escutando em {SERVER}')
    while True:
        print(f'preparando sala {threading.active_count()-1}')
        
        grupo_de_jogadores = conectar_jogadores()

        thread = threading.Thread(target=cria_partida,args=(grupo_de_jogadores,))
        thread.start()
        print(f'[salas ativas] {threading.active_count()-1}')


def cria_partida(jogadores):
    mesa = Mesa(0) 
    mesa.Iniciar_jogo(jogadores)

lobby()


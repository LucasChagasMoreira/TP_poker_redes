from funcoes_auxiliares import *  # Importa a classe Deck de um módulo chamado Deck
from simulaçao_do_server import *

class jogador():
    def __init__(self, nome, fichas, fichasapostadas):
        self._cartas = []  # Inicializa a variável cartas com uma instância da classe Deck
        self._nome = nome  # Atributo privado para armazenar o nome do jogador
        self._fichas = fichas  # Atributo privado para armazenar a quantidade de fichas do jogador
        self._fichasapostadas = fichasapostadas  # Atributo privado para armazenar as fichas apostadas pelo jogador

    # Propriedade para obter o nome do jogador
    @property
    def nome(self):
        return self._nome
    
    # Setter para atualizar o nome do jogador
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    # Propriedade para obter a quantidade de fichas do jogador
    @property
    def fichas(self):
        return self._fichas

    # Setter para atualizar a quantidade de fichas do jogador
    @fichas.setter
    def fichas(self, novas_fichas):
        self._fichas = novas_fichas

    # Propriedade para obter a quantidade de fichas apostadas pelo jogador
    @property
    def fichasapostadas(self):
        return self._fichasapostadas

    # Setter para atualizar a quantidade de fichas apostadas pelo jogador
    @fichasapostadas.setter
    def fichasapostadas(self, fichasapostadas_novas):
        self._fichasapostadas = fichasapostadas_novas

    # nao aposta e nao desiste        
    

    # desiste ate outro set
    def desistir(self):
        return "desistiu, voce so ira poder jogar novamente em um proximo set, aguarde este acabar\n"

    # aposta um valor maior que a aposta atual
    def aumentar_apostar(self,jogador):
        while(True):
            enviar_para_jogador(jogador,"digite o valor que deseja apostar:\n")
            aposta = int(requisita_jogada(jogador))
            if aposta > self.fichas:
                enviar_para_jogador(jogador,"quantidade de fichas invalida, insira outro valor\n")
            else:
                self.fichasapostadas = aposta
                return aposta

    def exibir_cartas(self):
        return f'cartas do jogador: {self._cartas}\n'

    # aposta um valor identico a aposta atual
    def call(self,aposta_atual):
        self.fichasapostadas = aposta_atual

    # funçao que reune todas as funçoes de envolvendo jogadas
    def jogada(self,maioraposta,jogador):
        print(f'jogador {self.nome}:')
        while(True):
            enviar_para_jogador(jogador,menu_jogada())
            escolha = requisita_jogada(jogador)
            print(escolha)

            if escolha == '1':
                enviar_para_jogador(jogador,self.desistir())
                return '1' , 0

            elif escolha == '2':
                if self.fichas < maioraposta:
                    enviar_para_jogador(jogador,"fichas insuficientes.\n")
                else:
                    self.call(maioraposta)
                    enviar_para_jogador(jogador,f"voce pagou a mesa.(valor:{maioraposta})\n")
                    return '2',maioraposta

            elif escolha == '3':
                while(True):
                    aposta = self.aumentar_apostar(jogador)
                    if aposta <= maioraposta:
                        enviar_para_jogador(jogador,f"voce deve apostar um valor maior que {maioraposta}.\n") 
                    else:
                        return '3', aposta
            
            else:
                enviar_para_jogador(jogador,"escolha invalida, digite novamente\n")
    

    # subtrai o valor da aposta das fichas
    def descontaraposta(self):
        self.fichas = (self.fichas) - (self.fichasapostadas) 
        self.fichasapostadas = 0
  
from funcoes_auxiliares import *  # Importa a classe Deck de um módulo chamado Deck


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
    def holdar(self):
        print("holdou")    

    # desiste ate outro set
    def desistir(self):
        print("desistiu, voce so ira poder jogar novamente em um proximo set")

    # aposta um valor maior que a aposta atual
    def aumentar_apostar(self):
        while(True):
            aposta = int(input("digite o valor que deseja apostar:"))
            if aposta > self.fichas:
                print("quantidade de fichas invalida, insira outro valor")
            else:
                self.fichasapostadas = aposta
                return aposta

    def exibir_cartas(self):
        print(f'cartas do jogador: {self._cartas}')

    # aposta um valor identico a aposta atual
    def call(self,aposta_atual):
        self.fichasapostadas = aposta_atual

    # funçao que reune todas as funçoes de envolvendo jogadas
    def jogada(self,maioraposta):
        print(f'jogador {self.nome}:')
        while(True):
            menu_jogada()
            escolha = input()
            if escolha == "1":
                self.holdar()
                return 0,0

            elif escolha == '2':
                self.desistir()
                return '2' , 0

            elif escolha == '3':
                if self.fichas < maioraposta:
                    print("fichas insuficientes.\n")
                else:
                    self.call(maioraposta)
                    return '3',maioraposta

            elif escolha == '4':
                while(True):
                    aposta = self.aumentar_apostar()
                    if aposta <= maioraposta:
                        print(f"voce deve apostar um valor maior que {maioraposta}.\n") 
                    else:
                        return '4', aposta
            
            else:
                print("escolha invalida, digite novamente")
    

    # subtrai o valor da aposta das fichas
    def descontaraposta(self):
        self.fichas = (self.fichas) - (self.fichasapostadas) 
        self.fichasapostadas = 0
  
from Deck import Deck  # Importa a classe Deck de um módulo chamado Deck

class jogador():
    def __init__(self, nome, fichas, fichasapostadas):
        self.cartas = Deck()  # Inicializa a variável cartas com uma instância da classe Deck
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

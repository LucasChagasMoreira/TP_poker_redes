import random
mapeamento_de_maos = {'royale_flush': 9, 'straight_flush': 8, 'quadra': 7, 'full_house': 6, 'flush': 5, 'straight':4, 'trinca':3, 'dois_pares':2, 'dupla':1, 'carta_alta':0}
mapeamento_valores = {'Ás': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valete': 11, 'Rainha': 12, 'Rei': 13}

def titulo():
    print("************************************")
    print("**  Bem-vindo a Partida de Poker  **")
    print("**        Texas no Limit          **")
    print("************************************")

def desenha_linha():
    return "==================================================================="

def menu():
    num = int(input("digite quantos pessoas irao jogar o jogo (de 1 a 6):\n"))
    return num

def menu_jogada():
    return("Escolha uma opção: \n\n1 - desistir\n2 - pagar a mesa\n3 - aumentar")

def criar_baralho():
        naipes = ['Copas', 'Paus', 'Espadas', 'Ouros']
        valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Rainha', 'Rei']

        baralho = []

        for naipe in naipes:
            for valor in valores:
                carta = (valor, naipe)
                baralho.append(carta)

        return baralho
    
def distribuir_cartas(baralho, quantidade):
    # Embaralhar o baralho
    random.shuffle(baralho)
        
    # Verificar se a quantidade de cartas a ser distribuída é maior que o tamanho do baralho
    if quantidade > len(baralho):
        baralho = criar_baralho()
        random.shuffle(baralho)

    cartas_distribuidas = []
        
    for _ in range(quantidade):
        carta = baralho.pop(0)
        cartas_distribuidas.append(carta)
        
    return cartas_distribuidas

def possui_dupla(mao):
    valores_mao = [carta[0] for carta in mao]
    
    # Usando um conjunto (set) para identificar valores únicos
    valores_unicos = set(valores_mao)
    
    for valor in valores_unicos:
        # Se houver duas cartas com o mesmo valor, o jogador possui uma dupla
        if valores_mao.count(valor) == 2:
            return True
    
    # Se não encontrar uma dupla, retorna False
    return False

def possui_dois_pares(mao):
    valores_mao = [carta[0] for carta in mao]

    # Conta a ocorrência de cada valor
    contagem_valores = {valor: valores_mao.count(valor) for valor in set(valores_mao)}

    # Verifica se há dois pares distintos
    pares_encontrados = sum(contagem == 2 for contagem in contagem_valores.values())

    return pares_encontrados == 2


def possui_trinca(mao):
    valores_mao = [carta[0] for carta in mao]
    
    for valor in valores_mao:
        # Se houver três cartas com o mesmo valor, o jogador possui uma trinca
        if valores_mao.count(valor) == 3:
            return True
    
    # Se não encontrar uma trinca, retorna False
    return False

def possui_flush(mao):
    naipes_mao = [carta[1] for carta in mao]

    # Verifica se todos os naipes são iguais
    return all(n == naipes_mao[0] for n in naipes_mao)


def possui_full_house(mao):
    valores_mao = [carta[0] for carta in mao]
    
    # Usando um conjunto (set) para identificar valores únicos
    valores_unicos = set(valores_mao)
    
    trinca_encontrada = False
    par_encontrado = False
    
    for valor in valores_unicos:
        # Se houver uma trinca, definir a variável trinca_encontrada como True
        if valores_mao.count(valor) == 3:
            trinca_encontrada = True
        # Se houver um par, definir a variável par_encontrado como True
        elif valores_mao.count(valor) == 2:
            par_encontrado = True
    
    # Se ambas trinca e par foram encontrados, o jogador possui um Full House
    return trinca_encontrada and par_encontrado


def possui_quadra(mao):
    valores_mao = [carta[0] for carta in mao]
    
    for valor in valores_mao:
        # Se houver quatro cartas com o mesmo valor, o jogador possui uma quadra
        if valores_mao.count(valor) == 4:
            return True
    
    # Se não encontrar uma quadra, retorna False
    return False

def possui_straight(mao):
    valores_mao = [carta[0] for carta in mao]

    # Mapeia os valores das cartas para números para facilitar a verificação de sequência
    mapeamento_valores = {'Ás': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valete': 11, 'Rainha': 12, 'Rei': 13}

    valores_numeros = [mapeamento_valores[valor] for valor in valores_mao]

    # Ordena os valores
    valores_numeros.sort()

    # Verifica se há uma sequência consecutiva de cinco valores
    for i in range(len(valores_numeros) - 4):
        if valores_numeros[i:i+5] == list(range(valores_numeros[i], valores_numeros[i]+5)):
            return True

    # Se não encontrar um straight, retorna False
    return False

def possui_straight_flush(mao):
    naipes_mao = [carta[1] for carta in mao]
    valores_mao = [carta[0] for carta in mao]
    
    # Mapeia os valores das cartas para números para facilitar a verificação de sequência
    mapeamento_valores = {'Ás': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valete': 11, 'Rainha': 12, 'Rei': 13}
    
    valores_numeros = [mapeamento_valores[valor] for valor in valores_mao]
    
    # Ordena os valores
    valores_numeros.sort()
    
    # Verifica se há uma sequência consecutiva do mesmo naipe
    for i in range(len(valores_numeros) - 4):
        if valores_numeros[i] == valores_numeros[i + 1] - 1 == valores_numeros[i + 2] - 2 == valores_numeros[i + 3] - 3 == valores_numeros[i + 4] - 4 and all(n == naipes_mao[i] for n in naipes_mao[i:i+5]):
            return True
    
    # Se não encontrar um straight flush, retorna False
    return False

def possui_royal_flush(mao):
    naipes_mao = [carta[1] for carta in mao]
    valores_mao = [carta[0] for carta in mao]

    # Mapeia os valores das cartas para números para facilitar a verificação de sequência
    mapeamento_valores = {'Ás': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valete': 11, 'Rainha': 12, 'Rei': 13}

    valores_numeros = [mapeamento_valores[valor] for valor in valores_mao]

    # Ordena os valores
    valores_numeros.sort()

    # Verifica se há uma sequência consecutiva do mesmo naipe começando do 10 até o Ás
    return all(n == naipes_mao[0] for n in naipes_mao) and valores_numeros == [10, 11, 12, 13, 14]



def indices_do_maior(lista):
    if not lista:
        return []  # Retorna None se a lista estiver vazia

    maior_valor = max(lista)
    indices_maior = [i for i, valor in enumerate(lista) if valor == maior_valor]
    
    return indices_maior

def carta_mais_alta(mao):
    valores_mao = [carta[0] for carta in mao]

    # Mapeia os valores das cartas para números para facilitar a comparação
    mapeamento_valores = {'Ás': 14, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valete': 11, 'Rainha': 12, 'Rei': 13}

    # Converte os valores para números
    valores_numeros = [mapeamento_valores[valor] for valor in valores_mao]

    # Encontra o valor mais alto
    maior_valor = max(valores_numeros)

    return maior_valor



def verificar_mao(mao):
    if possui_royal_flush(mao):
        return 'royale_flush'
    elif possui_straight_flush(mao):
        return 'straight_flush'
    elif possui_quadra(mao):
        return 'quadra'
    elif possui_full_house(mao):
        return 'full_house'
    elif possui_flush(mao):
        return 'flush'
    elif possui_straight(mao):
        return 'straight'
    elif possui_trinca(mao):
        return 'trinca'
    elif possui_dois_pares(mao):
        return 'dois_pares'
    elif possui_dupla(mao):
        return 'dupla'
    else:
        return 'carta_alta'














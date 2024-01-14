import sys
sys.path.append('../src')

from jogador import jogador
from funcoes_auxiliares import *
from Mesa import Mesa

mesa = Mesa(0)

braz = jogador("braz",1000,0)
mesa.Adiciona_jogador(braz)

assert mesa.quantidadedejogadores() == 1

mesa.Remover_jogador(0)

assert mesa.quantidadedejogadores() == 0

assert mesa.fichas == 0

braz.fichas = 900

assert braz.fichas == 900

mesa.Iniciar_jogo()             
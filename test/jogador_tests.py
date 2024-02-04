import sys
sys.path.append('../src')

from jogador import jogador

#assert dos getters e construtores
braz = jogador("braz",1000,0)
assert braz.nome == "braz"

assert braz.fichas == 1000

assert braz.nome == "braz"

assert braz.fichasapostadas == 0

#assert dos setters
braz.nome = "felipe"
assert braz.nome == "felipe"

braz.fichas = 20
assert braz.fichas == 20

braz.fichasapostadas = 10
assert braz.fichasapostadas == 10

del braz
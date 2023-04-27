# Importações
import random

# Adicione o nome de cada jogador
jogadores = ['Jogador1', 'Jogador2', 'Jogador3', 'Jogador4', 'Jogador5', 'Jogador6','Jogador7']

# Lista de insignias para cada geração
insignias = [
    # Geração 1
    ['Boulder Badge', 'Cascade Badge', 'Thunder Badge', 'Rainbow Badge', 'Marsh Badge', 'Soul Badge', 'Volcano Badge', 'Earth Badge'],
    # Geração 2
    ['Zephyr Badge', 'Hive Badge', 'Plain Badge', 'Fog Badge', 'Storm Badge', 'Mineral Badge', 'Glacier Badge', 'Rising Badge'],
    # Geração 3
    ['Stone Badge', 'Knuckle Badge', 'Dynamo Badge', 'Heat Badge', 'Balance Badge', 'Feather Badge', 'Mind Badge', 'Rain Badge'],
    # Geração 4
    ['Coal Badge', 'Forest Badge', 'Cobble Badge', 'Fen Badge', 'Relic Badge', 'Mine Badge', 'Icicle Badge', 'Beacon Badge'],
    # Geração 5
    ['Basic Badge', 'Insect Badge', 'Bolt Badge', 'Quake Badge', 'Jet Badge', 'Freeze Badge', 'Legend Badge', 'Toxic Badge', 'Wave Badge', 'Trio Badge'],
    # Geração 6
    ['Bug Badge', 'Cliff Badge', 'Rumble Badge', 'Plant Badge', 'Voltage Badge', 'Fairy Badge', 'Psychic Badge', 'Iceberg Badge']
]

# Gerar número aleatório de 1 a 6 para representar a geração
geracao = random.randint(1, 6)

# Exibir o jogador sorteado
print('Jogador: ' + jogadores[random.randrange(len(jogadores))])

# Exibir a geração e a insígnia sorteada
print('Geração: {}'.format(geracao))
print('Insignia: ' + insignias[geracao-1][random.randrange(len(insignias[geracao-1]))])
